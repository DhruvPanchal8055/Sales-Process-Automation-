import pandas as pd
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

console = Console()

# -------------------- Step 1: Define Email Templates --------------------

# Formal Email
formal_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formal Email Template</title>
</head>
<body>
    <div style="font-family: Arial, sans-serif; color: #333; max-width: 600px; margin: auto;">
        <h2>Dear {recipient_name},</h2>
        <p>I hope you're doing well. I wanted to reach out to you because I believe your company, {company_name}, could benefit from our services at {your_company}.</p>
        <p>We specialize in [mention service/product], and we've helped similar businesses in [industry] like {company_name} with [describe the benefits your service/product provides].</p>
        <p>If this sounds interesting, I’d love to schedule a call or answer any questions you may have. Feel free to <a href="mailto:{your_email}">contact us</a> directly or click [your calendar link] to book a meeting with me.</p>
        <p>Looking forward to connecting!</p>
        <p>Sincerely,<br>{your_name}<br>{your_position}<br>{your_company}</p>
    </div>
</body>
</html>
"""

# -------------------- Step 2: Get Sender Details --------------------
def get_sender_details():
    """ Prompt user for sender's details (name, position, company, and email) """
    console.print("[bold cyan]Enter your details[/bold cyan]")
    your_name = input("Enter your name: ").strip()
    your_position = input("Enter your position: ").strip()
    your_company = input("Enter your company name: ").strip()
    your_email = input("Enter your email: ").strip()

    return your_name, your_position, your_company, your_email

# -------------------- Step 3: Get Template Choice --------------------
def get_template_choice():
    console.print("[bold cyan]Choose your email template style:[/bold cyan]")
    console.print("[bold green]1.[/bold green] Formal Template")

    choice = Prompt.ask("[bold cyan]Enter the number of your choice[/bold cyan]: ")

    if choice == '1':
        return formal_template
    else:
        console.print("[bold red]Invalid choice, defaulting to Formal Template.[/bold red]")
        return formal_template

# -------------------- Step 4: Read Data from All Excel Files --------------------
def read_all_excel_files():
    """ Read all Excel files in the output folder """
    output_folder = os.path.join(os.getcwd(), "output")
    all_files = [f for f in os.listdir(output_folder) if f.endswith('.xlsx')]
    
    data_frames = []
    for file in all_files:
        file_path = os.path.join(output_folder, file)
        df = pd.read_excel(file_path)
        data_frames.append(df)
    
    
    combined_data = pd.concat(data_frames, ignore_index=True)
    return combined_data

# -------------------- Step 5: Generate Emails --------------------
def generate_email_template(data, template, your_name, your_position, your_company, your_email):
    """ Generate personalized emails based on data """
    emails = []
    valid_email_count = 0
    invalid_email_count = 0

    for index, row in data.iterrows():
        recipient_name = row['Contact Person'] if row['Contact Person'] else "Dear Sir/Mam"
        company_name = row['Company Name']
        contact_email = row['Contact Email']

        
        if not contact_email or pd.isnull(contact_email):
            invalid_email_count += 1
            continue

        valid_email_count += 1
        
        subject = f"Exciting Opportunities for {company_name} with {your_company}"

        
        email_body = template.format(
            recipient_name=recipient_name,
            company_name=company_name,
            your_email=your_email,  
            your_name=your_name,
            your_position=your_position,
            your_company=your_company
        )
        emails.append({
            'email_body': email_body,
            'company_name': company_name,
            'recipient_email': contact_email,
            'subject': subject
        })

    return emails, valid_email_count, invalid_email_count

# -------------------- Step 6: Simulate Email Sending --------------------
def simulate_send_email(emails):
    """ Simulate sending emails by printing them to the console """
    for email in emails:
        console.print(f"\n[bold cyan]Simulating sending email to {email['recipient_email']}[/bold cyan]")
        console.print(f"[bold green]Subject:[/bold green] {email['subject']}")
        console.print(f"[bold green]Email Body:[/bold green]\n{email['email_body']}")
        console.print(f"\n[bold cyan]--- End of Email ---[/bold cyan]")

# -------------------- Step 7: Main Program --------------------

def main():
    console.print("[bold cyan]Email Template Generator and Sender Simulation[/bold cyan]", style="bold cyan")

  
    your_name, your_position, your_company, your_email = get_sender_details()

    
    data = read_all_excel_files()

    
    template_choice = get_template_choice()

    
    emails, valid_email_count, invalid_email_count = generate_email_template(
        data, template_choice, your_name, your_position, your_company, your_email
    )

    
    simulate_send_email(emails)

    console.print(f"\n[bold green]Total valid emails: {valid_email_count}[/bold green]")
    console.print(f"[bold red]Total invalid emails (missing or invalid): {invalid_email_count}[/bold red]")

if __name__ == "__main__":
    main()
