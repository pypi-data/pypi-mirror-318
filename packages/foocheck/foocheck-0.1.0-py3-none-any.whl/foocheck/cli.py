import click
import asyncio
from rich.console import Console
from rich.table import Table
from .utils import check_username
from .networks import (
    SOCIAL_NETWORKS,
    DEVELOPER_PLATFORMS,
    STREAMING_PLATFORMS,
    GAMING_PLATFORMS,
    ECOMMERCE_PLATFORMS,
    FORUMS_COMMUNITIES,
    OTHER_PLATFORMS,
)

console = Console()

# Map categories to their respective lists
CATEGORIES = {
    "social": SOCIAL_NETWORKS,
    "developer": DEVELOPER_PLATFORMS,
    "streaming": STREAMING_PLATFORMS,
    "gaming": GAMING_PLATFORMS,
    "ecommerce": ECOMMERCE_PLATFORMS,
    "forums": FORUMS_COMMUNITIES,
    "other": OTHER_PLATFORMS,
    "all": SOCIAL_NETWORKS
    + DEVELOPER_PLATFORMS
    + STREAMING_PLATFORMS
    + GAMING_PLATFORMS
    + ECOMMERCE_PLATFORMS
    + FORUMS_COMMUNITIES
    + OTHER_PLATFORMS,
}

async def check_all_networks(username, networks):
    """Check username availability across a list of networks in parallel.

    Args:
        username (str): The username to check.
        networks (list): A list of networks to check.

    Returns:
        list: A list of tuples containing the network name and status.
    """
    tasks = [check_username(username, network["url"]) for network in networks]
    results = await asyncio.gather(*tasks)
    return [(networks[i]["name"], results[i]) for i in range(len(networks))]

def display_results(username, results):
    """Display the results of username availability checks in a table.

    Args:
        username (str): The username to check.
        results (list): A list of tuples containing the network name and status.
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Social Network", style="dim", width=20)
    table.add_column("Status")

    for name, status in results:
        table.add_row(name, f"[green]{status}[/green]" if status == "Available" else f"[red]{status}[/red]")

    console.print(table)

@click.command()
@click.argument("username")
@click.option(
    "--category",
    type=click.Choice(["social", "developer", "streaming", "gaming", "ecommerce", "forums", "other", "all"], case_sensitive=False),
    default="all",
    help="Category of platforms to check (default: all).",
)
def main(username, category):
    """Check if a username is taken on various social networks and platforms.

    Args:
        username (str): The username to check.
        category (str): The category of platforms to check.
    """
    console.print(f"[bold]Foocheck - Checking username: {username}[/bold]\n")
    networks = CATEGORIES.get(category, CATEGORIES["all"])
    results = asyncio.run(check_all_networks(username, networks))
    display_results(username, results)

if __name__ == "__main__":
    main()
