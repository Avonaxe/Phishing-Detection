import imaplib
import email

# Gmail account details
EMAIL = "your-gmail-account@gmail.com"  # Replace with your Gmail address
PASSWORD = "your-app-password"  # Replace with your app password or regular password if no 2FA
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993

# Suspicious keywords
suspicious_keywords = ["urgent", "login now", "bank account", "click here", "bit.ly", "verify", "password"]

def check_emails():
    # Connect to Gmail
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")  # Select the inbox

    # Search for all emails
    status, data = mail.search(None, "ALL")
    email_ids = data[0].split()

    for email_id in email_ids[-5:]:  # Check the 5 most recent emails (adjust as needed)
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Extract subject and body
        subject = msg["subject"]
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = msg.get_payload(decode=True).decode()

        # Check for suspicious keywords
        matches = sum(keyword in (subject.lower() + body.lower()) for keyword in suspicious_keywords)
        if matches >= 2:
            print(f"WARNING: Potential phishing email (ID: {email_id.decode()}):")
            print(f"Subject: {subject}")
            print(f"Matches: {matches} suspicious terms\n")
        else:
            print(f"Email (ID: {email_id.decode()}) seems safe. Matches: {matches}\n")

    mail.logout()

if __name__ == "__main__":
    check_emails()
