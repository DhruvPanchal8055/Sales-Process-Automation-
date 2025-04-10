import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

console = Console()

# ------------------ Main Menu ------------------

def display_menu():
    """Display the main menu with options."""
    
    # Big Flashy Title with API info and your name
    console.print(
        Panel(
            f"[bold cyan]Sales Automation Tool[/bold cyan]\n"
            f"[bold green]API Used: SerpAPI & ScrapingDog[/bold green]\n"
            f"[bold yellow]Created by: Dhruv Panchal[/bold yellow]\n"
            f"[bold red]GitHub:[/bold red]", 
            style="bold white", expand=False
        )
    )

    console.print("\n[bold yellow]Choose an option:[/bold yellow]")
    console.print("[bold magenta]1.[/bold magenta] Scraper Module")
    console.print("[bold magenta]2.[/bold magenta] Email Campaign Module (Need Smtp Credentials)")
    console.print("[bold red]3.[/bold red] Email Campaign Analytics Module (Simulation For Now)")
    console.print("[bold red]4.[/bold red] Exit")

def run_scraper_module():
    """Run the scraper module script."""
    console.print("\n[bold yellow]Running Scraper Module...[/bold yellow]")
    subprocess.run(["python", "Scripts/scraper.py"])

def run_email_campaign_module():
    """Run the email campaign module script."""
    console.print("\n[bold yellow]Running Email Campaign Module...[/bold yellow]")
    subprocess.run(["python", "Scripts/email_campaign.py"])

def run_email_campaign_analytic():
    """Run the email campaign module script."""
    console.print("\n[bold yellow]Running Email Campaign Module...[/bold yellow]")
    subprocess.run(["python", "Scripts/email_campaign_analytics.py"])

def main():
    while True:
        
        display_menu()

        choice = Prompt.ask("[bold cyan]Choose an option (1, 2, 3 or 4):[/bold cyan]")

        if choice == '1':
            run_scraper_module()
        elif choice == '2':
            run_email_campaign_module()
        elif choice == '3':
            run_email_campaign_analytic()
        elif choice == '4':
            console.print("\n[bold red]Exiting program...[/bold red]")
            break
        else:
            console.print("[bold red]Invalid choice. Please choose a valid option.[/bold red]")

if __name__ == "__main__":
    main()
