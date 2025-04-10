import os
import random
import pandas as pd
from rich.console import Console
from rich.prompt import Prompt

console = Console()

company_names = [
    "Google", "Microsoft", "Apple", "Amazon", "Facebook", "Tesla", "Adobe", "Oracle", "Spotify", "Netflix"
]


if not os.path.exists('Analytics'):
    os.makedirs('Analytics')

def generate_sample_analytics():
    leads = [f'Lead {i+1}' for i in range(50)]  
    opened_email = [random.random() < 0.4 for _ in range(50)]
    clicked_cta = [random.random() < 0.3 if open_status else False for open_status in opened_email]
    response = [random.random() < 0.2 if click_status else False for click_status in clicked_cta]
    company = [random.choice(company_names) for _ in range(50)]
    contact_email = [f"{company[i].lower()}@example.com" for i in range(50)]
    
    data = {
        'Lead': leads,
        'Company': company,
        'Contact Email': contact_email,
        'Opened Email': opened_email,
        'Clicked CTA': clicked_cta,
        'Response': response,
    }
    
    return pd.DataFrame(data)

def categorize_leads(df):
    df['Lead Category'] = df.apply(
        lambda row: 'Hot' if row['Opened Email'] and row['Clicked CTA'] else 'Cold', axis=1
    )
    return df

def simulate_email_analytics():
    df = generate_sample_analytics()  
    categorized_leads = categorize_leads(df)  
    
    total_sent = len(df)
    total_opened = df['Opened Email'].sum()
    total_clicked = df['Clicked CTA'].sum()
    total_responses = df['Response'].sum()

    hot_leads = categorized_leads[categorized_leads['Lead Category'] == 'Hot'].shape[0]
    cold_leads = categorized_leads[categorized_leads['Lead Category'] == 'Cold'].shape[0]

    # Calculate metrics
    open_rate = total_opened / total_sent * 100
    click_through_rate = total_clicked / total_sent * 100
    response_rate = total_responses / total_sent * 100

    # Summary of Analytics
    summary_data = {
        'Total Emails Sent': total_sent,
        'Open Rate (%)': open_rate,
        'Click-Through Rate (%)': click_through_rate,
        'Response Rate (%)': response_rate,
        'Hot Leads': hot_leads,
        'Cold Leads': cold_leads,
    }

    console.print("\n[bold green]Email Campaign Analytics Summary[/bold green]")
    console.print(f"Total Emails Sent: {total_sent}")
    console.print(f"Open Rate: {open_rate:.2f}%")
    console.print(f"Click-Through Rate: {click_through_rate:.2f}%")
    console.print(f"Response Rate: {response_rate:.2f}%")
    console.print(f"Hot Leads: {hot_leads}")
    console.print(f"Cold Leads: {cold_leads}")

    
    summary_df = pd.DataFrame([summary_data])
    
    
    output_file = os.path.join('Analytics', 'email_campaign_analytics_full_details.csv')
    categorized_leads.to_csv(output_file, index=False)

   
    summary_file = os.path.join('Analytics', 'email_campaign_analytics_summary.csv')
    summary_df.to_csv(summary_file, index=False)

    console.print(f"[bold cyan]Analytics report saved as {output_file}[/bold cyan]")
    console.print(f"[bold cyan]Summary saved as {summary_file}[/bold cyan]")

def real_email_analytics():
    console.print("[bold green]Real Email Campaign Analytics[/bold green]")
    df = generate_sample_analytics()  
    categorized_leads = categorize_leads(df)

    total_sent = len(df)
    total_opened = df['Opened Email'].sum()
    total_clicked = df['Clicked CTA'].sum()
    total_responses = df['Response'].sum()

    hot_leads = categorized_leads[categorized_leads['Lead Category'] == 'Hot'].shape[0]
    cold_leads = categorized_leads[categorized_leads['Lead Category'] == 'Cold'].shape[0]

    
    open_rate = total_opened / total_sent * 100
    click_through_rate = total_clicked / total_sent * 100
    response_rate = total_responses / total_sent * 100

    
    summary_data = {
        'Total Emails Sent': total_sent,
        'Open Rate (%)': open_rate,
        'Click-Through Rate (%)': click_through_rate,
        'Response Rate (%)': response_rate,
        'Hot Leads': hot_leads,
        'Cold Leads': cold_leads,
    }

    console.print(f"\n[bold green]Real Campaign Analytics Summary[/bold green]")
    console.print(f"Total Emails Sent: {total_sent}")
    console.print(f"Open Rate: {open_rate:.2f}%")
    console.print(f"Click-Through Rate: {click_through_rate:.2f}%")
    console.print(f"Response Rate: {response_rate:.2f}%")
    console.print(f"Hot Leads: {hot_leads}")
    console.print(f"Cold Leads: {cold_leads}")

    
    summary_df = pd.DataFrame([summary_data])
    
    
    output_file = os.path.join('Analytics', 'real_email_campaign_analytics_full_details.csv')
    categorized_leads.to_csv(output_file, index=False)

    
    summary_file = os.path.join('Analytics', 'real_email_campaign_analytics_summary.csv')
    summary_df.to_csv(summary_file, index=False)

    console.print(f"[bold cyan]Real campaign analytics summary saved as {output_file}[/bold cyan]")
    console.print(f"[bold cyan]Real campaign summary saved as {summary_file}[/bold cyan]")

def email_campaign_analytics_mode():
    mode = Prompt.ask("[bold cyan]Choose Email Campaign Analytics Mode:\n1. Simulate Analytics\n2. Real Analytics[/bold cyan]")

    if mode == "1":
        simulate_email_analytics()
    elif mode == "2":
        real_email_analytics()
    else:
        console.print("[bold red]Invalid choice.[/bold red]")

def main():
    email_campaign_analytics_mode()

if __name__ == "__main__":
    main()
