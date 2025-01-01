import argparse
import os
import smtplib
import getpass
import json
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CONFIG_DIR = Path.home() / '.config' / 'pysend'
CONFIG_FILE = CONFIG_DIR / 'config.json'

def save_credentials(email, password):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump({'email': email, 'password': password}, f)

def load_credentials():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def handle_login():
    email = input("Enter your Gmail address: ")

    print("\nPysend Gmail Login Setup")
    print("\nTo use Gmail with this app, you'll need an 'App Password'. Here's how to get one:")
    print("1. Go to https://myaccount.google.com/security")
    print("2. Enable 2-Step Verification if you haven't already")
    print("3. Go to 'App passwords' (search for 'App Password' to find it)")
    print("4. Create a new App Password named 'pysend'\n")
    password = getpass.getpass("Enter your App Password (16 characters): ")
    
    save_credentials(email, password)
    print("\nCredentials saved successfully!")

def send_email(body, subject=None):
    creds = load_credentials()
    if not creds or not creds['email'] or not creds['password']:
        print("No credentials found. Please run 'pysend login' first.")
        return

    sender_email = creds['email']
    sender_password = creds['password']
    receiver_email = sender_email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    if subject:
        msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(sender_email, sender_password)
            s.send_message(msg)
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
        if "Invalid login credentials" in str(e):
            print("\nTip: If you're using your regular Gmail password, you need to switch to an App Password.")
            print("Run 'pysend login' again to set up an App Password.")

def main():
    parser = argparse.ArgumentParser(description='Send an email to yourself')
    parser.add_argument('command', help='Command to execute (send a link or "login" to set credentials)')
    parser.add_argument('-s', '--subject', help='Subject of the email')
    
    args = parser.parse_args()
    
    if args.command.lower() == 'login':
        handle_login()
    else:
        send_email(args.command, args.subject)