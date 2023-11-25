import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_notification(subject,message):
    # Set your email and password
    sender_email = "yourmail@gmail.com"
    sender_password = ""
    to_email="yourmail@gmail.com"
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server (in this example, using Gmail)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, to_email, msg.as_string())
        print("Notification email sent successfully!")
    except Exception as e:
        print(f"Error sending email notification: {str(e)}")
    finally:
        server.quit()

# Example usage
#def notify(chat_id, category, remaining_amount):
 #   subject = f"Budget Notification - {category}"
 #   message = f"Your remaining budget for {category} is ${remaining_amount}."
 #   to_email = "recipient@example.com"  # Replace with the recipient's email address
 #   send_email_notification(subject, message, to_email)
