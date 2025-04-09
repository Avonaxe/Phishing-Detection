# Email Phishing Detection Tool

A simple Python script that scans your Gmail inbox for potential phishing emails by detecting suspicious keywords and patterns.

## Features

- Connects to Gmail via IMAP
- Scans the most recent emails in your inbox
- Identifies potential phishing attempts based on suspicious keywords
- Provides a simple report for each scanned email

## Requirements

- Python 3.x
- Internet connection
- Gmail account
- App password (if 2-factor authentication is enabled)

## Setup

1. Make sure you have Python 3.x installed on your system
2. If you have 2-factor authentication enabled on your Gmail account:
   - Go to your Google Account → Security
   - Under "Signing in to Google," select "App passwords"
   - Generate a new app password for the script
3. If you don't have 2-factor authentication, you'll need to enable "Less secure app access" in your Google account settings

## Configuration

Edit the script to include your Gmail credentials:

```python
EMAIL = "your.email@gmail.com"  # Replace with your Gmail address
PASSWORD = "your-password-here"  # Replace with your app password or regular password
```

You can also customize the suspicious keywords list:

```python
suspicious_keywords = ["urgent", "login now", "bank account", "click here", "bit.ly", "verify", "password"]
```

## Usage

Run the script from your terminal or command prompt:

```
python phishing_detector.py
```

The script will:
1. Connect to your Gmail account
2. Scan the 5 most recent emails (configurable)
3. Print a report for each email, indicating whether it seems safe or potentially suspicious

## Security Note

- This script stores your email and password in plain text. Ensure the script is stored securely.
- Consider using environment variables or a secure configuration file for credentials in production.
- This is a basic detection tool and should not replace proper security practices or professional anti-phishing solutions.

## Customization

- Adjust the number of emails to scan by changing the slice in `email_ids[-5:]`
- Modify the threshold for suspicious emails by changing the condition `if matches >= 2:`
- Add more suspicious keywords to improve detection

## License

This project is available under the MIT License.
