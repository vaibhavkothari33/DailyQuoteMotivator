import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import requests

def get_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    else:
        return "Failed to fetch quote"

def send_email(quote):
    from_addr = ''  # Sender's email address
    to_addr = ''  # Recipient's email address
    subject = 'Your Daily Powerful Quote'

    # Email configuration
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(quote, 'plain'))
     # Connect to SMTP server at 587 port
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, '')  # Enter your email password here

    # Send email
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

    print("Email sent successfully")

def send_daily_quote():
    quote = get_quote()
    send_email(quote)

# Schedule the email to be sent daily at a specific time (e.g., 8:00 AM)
schedule.every().day.at("23:47").do(send_daily_quote)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
