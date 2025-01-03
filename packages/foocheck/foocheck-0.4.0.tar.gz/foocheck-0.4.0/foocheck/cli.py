import click
import asyncio
from rich.console import Console
from rich.table import Table
from rich.spinner import Spinner
from rich.live import Live
import time
from .utils import check_username
from .networks import (
    SOCIAL,
    DEV,
    STREAMING,
    GAMING,
    FORUMS,
    OTHER,
    PAYMENT,
    PRO
)

console = Console()

# Map categories to their respective lists
CATEGORIES = {
    "social": SOCIAL,
    "dev": DEV,
    "streaming": STREAMING,
    "gaming": GAMING,
    "forums": FORUMS,
    "other": OTHER,
    "all": SOCIAL
    + DEV
    + STREAMING
    + GAMING
    + FORUMS
    + OTHER,
}

async def check_all_networks(username, networks):
    """Check username availability across a list of networks in parallel.

    Args:
        username (str): The username to check.
        networks (list): A list of networks to check.
        protocol (str): The protocol to use ("http2" or "http3").

    Returns:
        list: A list of tuples containing the network name and status.
    """
    tasks = [check_username(username, network["url"]) for network in networks]

    # Display a spinner while waiting for results
    with Live(Spinner("dots", text="Checking websites..."), console=console, transient=True):
        results = await asyncio.gather(*tasks)

    return [(networks[i]["name"], results[i]) for i in range(len(networks))]

def display_single_result(network_name, status):
    """Display the result for a single network.

    Args:
        network_name (str): The name of the network.
        status (str): The status of the username ("Taken", "Available", "Unknown", or "Error").
    """
    if status == "Available":
        console.print(f"[green][✓] {network_name}[/green]")
    elif status == "Taken":
        console.print(f"[red][✗] {network_name}[/red]")
    else:
        console.print(f"[yellow][?] {network_name}[/yellow]")

def display_results(username, results):
    """Display the summary of username availability checks.

    Args:
        username (str): The username to check.
        results (list): A list of tuples containing the network name and status.
    """
    sorted_results = sorted(results, key=lambda x: x[0])
    for name, status in sorted_results:
        time.sleep(0.5)
        display_single_result(name, status)

@click.command()
@click.argument("username")
@click.option(
    "--category",
    type=click.Choice(["social", "dev", "streaming", "gaming", "forums", "other", "all"], case_sensitive=False),
    default="all",
    help="Category of platforms to check (default: all).",
)
def main(username, category):
    """Check if a username is taken on various social networks and platforms.

    Args:
        username (str): The username to check.
        category (str): The category of platforms to check.
    """
    # console.print(f"[bold]Foocheck - Checking username: {username}[/bold]\n")
    networks = CATEGORIES.get(category, CATEGORIES["all"])
    results = asyncio.run(check_all_networks(username, networks))
    display_results(username, results)

if __name__ == "__main__":
    main()
