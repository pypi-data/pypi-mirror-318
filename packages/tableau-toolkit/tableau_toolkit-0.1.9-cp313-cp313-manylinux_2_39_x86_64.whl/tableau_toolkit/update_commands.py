import logging
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import click
import tableauserverclient as TSC
from .cli_utils import load_config
from .cli_utils import authenticate
from .cli_utils import get_csv_data
from .logging_config import configure_logging, get_logger

# Configure logging for this module
configure_logging(output_dir="output", module_name=__name__)
logger = get_logger(__name__)


@click.group()
def update():
    """Update various Tableau resources"""


@update.group()
def users():
    """Update user attributes"""


@users.command()
@click.option("--file", type=click.Path(exists=True), help="Path to the CSV file")
@click.option("--stdin", is_flag=True, help="Read from stdin instead of a file")
@click.option("--delimiter", default="\t", help="Delimiter used in the CSV file")
@click.option("--site-luid-col", default="site_luid", help="Column name for Site LUID")
@click.option(
    "--user-luid-col", default="object_luid", help="Column name for User LUID"
)
@click.option(
    "--val-col", default="object_email", help="Column name containing the new site role values"
)
@click.option("--threads", default=1, type=int, help="Number of concurrent threads for updates")
@click.pass_context
def email(ctx, file, stdin, delimiter, site_luid_col, user_luid_col, val_col, threads):
    """Update user email addresses"""
    update_user_attribute(
        ctx, file, stdin, delimiter, site_luid_col, user_luid_col, val_col, "email", threads
    )


def update_user_attribute(
    ctx, file, stdin, delimiter, site_luid_col, user_luid_col, val_col, attribute, threads
):
    config = load_config(ctx.obj["config"])
    server = authenticate(config)
    csv_data = get_csv_data(file, stdin, delimiter)

    # Group data by site
    site_groups = defaultdict(list)
    for row in csv_data:
        site_luid = row[site_luid_col]
        site_groups[site_luid].append(row)

    def update_user(server: TSC.Server, site, user_luid, new_value, attribute):
        try:
            user = server.users.get_by_id(user_luid)
            setattr(user, attribute, new_value)
            server.users.update(user)
            logger.info("User attribute updated", 
                        attribute=attribute, 
                        user_name=user.name, 
                        user_luid=user_luid, 
                        site_name=site.name, 
                        site_id=site.id)
            return f"Updated {attribute} for user {user.name} ({user_luid}) on site {site.name} ({site.id})"
        except TSC.ServerResponseError as e:
            logger.error("Error updating user", 
                         user_luid=user_luid, 
                         error=str(e))
            return f"Error updating user {user_luid}: {str(e)}"
        except Exception as e:
            logger.exception("Unexpected error updating user", 
                             user_luid=user_luid)
            return f"Unexpected error updating user {user_luid}: {str(e)}"

    for site_luid, site_data in site_groups.items():
        try:
            site = next((site for site in TSC.Pager(server.sites) if site.id == site_luid), None)
            if not site:
                logger.error("Site not found", site_luid=site_luid)
                continue
            
            server.auth.switch_site(site)
            
            with ThreadPoolExecutor(max_workers=threads) as executor:
                futures = [executor.submit(update_user, server, site, row[user_luid_col], row[val_col], attribute) for row in site_data]
                
                for future in as_completed(futures):
                    result = future.result()
                    logger.info(result)
        
        except Exception as e:
            logger.exception("Error processing site", site_luid=site_luid)

    server.auth.sign_out()
