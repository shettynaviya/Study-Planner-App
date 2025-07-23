import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    from_email = "your_email@example.com"
    password = "your_password"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, password)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)