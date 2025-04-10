import smtplib
import pandas as pd
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from datetime import datetime

console = Console()

# -------------------- Step 1: Define Email Templates --------------------

# Template 1: Formal Email
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
        <p>I hope you're doing well. I wanted to reach out because I believe your company, {company_name}, could benefit from our services at {your_company}.</p>
        <p>We specialize in [mention service/product], and we've helped similar businesses in [industry] like {company_name} with [describe the benefits your service/product provides].</p>
        <p>If this sounds interesting, I’d love to schedule a call or answer any questions you may have. Feel free to <a href="mailto:{contact_email}">contact us</a> directly or click [your calendar link] to book a meeting with me.</p>
        <p>Looking forward to connecting!</p>
        <p>Sincerely,<br>{your_name}<br>{your_position}<br>{your_company}</p>
    </div>
</body>
</html>
"""

# Define other templates similarly (casual_template, direct_approach_template, informal_template)

# -------------------- Step 2: Get User Input for Sender's Details --------------------

def get_sender_details():
    """ Prompt user for sender's details (name, position, company) """
    your_name = input("Enter your name: ").strip()
    your_position = input("Enter your position: ").strip()
    your_company = input("Enter your company name: ").strip()

    return your_name, your_position, your_company

# -------------------- Step 3: Get Template Choice --------------------

def get_template_choice():
    console.print("[bold cyan]Choose your email template style:[/bold cyan]")
    console.print("[bold green]1.[/bold green] Formal Email Template")
    console.print("[bold green]2.[/bold green] Casual Email Template")
    console.print("[bold green]3.[/bold green] Direct Approach Template")
    console.print("[bold green]4.[/bold green] Informal Email Template")

    choice = Prompt.ask("[bold cyan]Enter the number of your choice[/bold cyan]: ")

    if choice == '1':
        return formal_template
    else:
        console.print("[bold red]Invalid choice, defaulting to Formal Template.[/bold red]")
        return formal_template

# -------------------- Step 4: Read Data from All Excel Files --------------------

def read_all_excel_files():
    """ Read and combine data from all Excel files in the output folder """
    output_folder = os.path.join(os.getcwd(), "output")
    all_files = [f for f in os.listdir(output_folder) if f.endswith('.xlsx')]
    
    data_frames = []
    for file in all_files:
        file_path = os.path.join(output_folder, file)
        df = pd.read_excel(file_path)
        data_frames.append(df)
    
    # Combine all data into one DataFrame
    combined_data = pd.concat(data_frames, ignore_index=True)
    return combined_data

# -------------------- Step 5: Generate Emails --------------------

def generate_email_template(data, template, your_name, your_position, your_company):
    """ Create personalized emails for each recipient from the data """
    emails = []
    valid_email_count = 0
    invalid_email_count = 0

    for index, row in data.iterrows():
        recipient_name = row['Contact Person'] if row['Contact Person'] else "Dear Sir/Mam"
        company_name = row['Company Name']
        contact_email = row['Contact Email']

        # Skip if the email is missing or invalid
        if not contact_email or pd.isnull(contact_email):
            invalid_email_count += 1
            continue

        valid_email_count += 1
        # Replace placeholders with actual data
        email_body = template.format(
            recipient_name=recipient_name,
            company_name=company_name,
            contact_email=contact_email,
            your_name=your_name,
            your_position=your_position,
            your_company=your_company
        )
        emails.append({
            'email_body': email_body,
            'company_name': company_name,
            'recipient_email': contact_email
        })

    return emails, valid_email_count, invalid_email_count

# -------------------- Step 6: Send Email --------------------

def send_email(subject, email_body, recipient_email, sender_email, sender_password):
    """ Send an email with the given subject and body """
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(email_body, 'html'))

        # Establish connection to SMTP server (Gmail in this case)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        console.print(f"[red]Error sending email to {recipient_email}: {e}[/red]")
        return False

# Function to send bulk emails in batches
def send_bulk_emails(emails, sender_email, sender_password, batch_size=10, delay=3):
    total_sent = 0
    total_failed = 0

    for i in range(0, len(emails), batch_size):
        batch = emails[i:i + batch_size]
        for email in batch:
            subject = f"Hi {email['company_name']}, Here's a message from {sender_email}"
            sent = send_email(subject, email['email_body'], email['recipient_email'], sender_email, sender_password)
            if sent:
                total_sent += 1
            else:
                total_failed += 1

        # Introduce delay between batches
        time.sleep(delay)

    # Summary of sent and failed emails
    console.print(f"\n[bold green]Total emails sent: {total_sent}[/bold green]")
    console.print(f"[bold red]Total emails failed: {total_failed}[/bold red]")

# -------------------- Step 7: Main Program --------------------

def main():
    console.print(Panel("[bold cyan]Email Campaign Automation[/bold cyan]", style="bold white", expand=False))

    # Gather sender's details
    your_name, your_position, your_company = get_sender_details()
    
    # Read data from all Excel files in the output folder
    data = read_all_excel_files()
    
    # Get the user's chosen email template
    template_choice = get_template_choice()
    
    # Generate personalized emails
    emails, valid_email_count, invalid_email_count = generate_email_template(
        data, template_choice, your_name, your_position, your_company
    )
    
    # Display summary of valid/invalid emails
    console.print(f"\n[bold green]Valid emails to be sent: {valid_email_count}[/bold green]")
    console.print(f"[bold red]Invalid emails (missing or invalid): {invalid_email_count}[/bold red]")
    
    # Save the generated emails to an Excel file
    output_folder = os.path.join(os.getcwd(), "output", f"Generated_Emails_{datetime.now().strftime('%Y_%m_%d')}")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_path = os.path.join(output_folder, "Generated_Emails.xlsx")
    email_df = pd.DataFrame(emails)
    email_df.to_excel(file_path, index=False)

    console.print(f"\n[bold cyan]Emails saved to {file_path}[/bold cyan]")

    # Ask the user to send the emails
    send_choice = Prompt.ask("[bold green]Do you want to send the emails? (y/n)[/bold green]")

    if send_choice.lower() == 'y':
        sender_email = Prompt.ask("[bold green]Enter your email address (sender):[/bold green]")
        sender_password = Prompt.ask("[bold green]Enter your email password:[/bold green]")
        
        # Send emails in batches
        send_bulk_emails(emails, sender_email, sender_password)

if __name__ == "__main__":
    main()
