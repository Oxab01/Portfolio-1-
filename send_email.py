import smtplib
from email.message import EmailMessage

def send_email(name, email, message):
    # Set up email content
    subject = "New Contact Form Submission"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    # Create EmailMessage object
    email_message = EmailMessage()
    email_message.set_content(body)

    email_message['Subject'] = subject
    email_message['From'] = email
    email_message['To'] = "getinformationformyweb@gmail.com"

    try:
        # Connect to the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "your-email@gmail.com"  # Replace with your Gmail address
        smtp_password = "your-password"  # Replace with your Gmail password

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(email_message)
        
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email.", str(e))

# Example usage:
name = "John Doe"
email = "johndoe@example.com"
message = "Hello, this is a test email!"

send_email(name, email, message)
