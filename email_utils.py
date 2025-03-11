# email_utils.py

import smtplib
from email.message import EmailMessage
import ssl

def send_email(subject, body, sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password):
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Connect to the SMTP server
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            # Login to the SMTP server using provided credentials
            server.login(smtp_username, smtp_password)

            # Create the email message
            message = f"Subject: {subject}\n\n{body}"

            # Send the email
            server.sendmail(sender_email, receiver_email, message)

        print("Email sent successfully.")

    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Example usage of the send_email function
if __name__ == "__main__":
    sender_email = "abarnaraj54@gmail.com"
    receiver_email = "abarnaabar05@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    smtp_username = "abarnaraj54@gmail.com"
    smtp_password = "#hope@9342"
    subject = "Test Email"
    body = "This is a test email sent using Python."

    send_email(subject, body, sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password)
