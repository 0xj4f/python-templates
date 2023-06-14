import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class AmazonSESEmailSender:
    def __init__(self, smtp_username, smtp_password, smtp_server, port):
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self, sender, recipient, subject, body):
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls()
        server.login(self.smtp_username, self.smtp_password)
        text = msg.as_string()
        response=server.sendmail(sender, recipient, text)
        # no response
        print(response)

        server.quit()

if __name__ == "__main__":
    smtp_username = "xxxxxxxxxxxxx"
    smtp_password = "xxxxxxxxxxxxx"
    smtp_server = "email-smtp.ap-southeast-X.amazonaws.com"
    port = 587  # Amazon SES SMTP uses port 587 or 465

    sender = "devsecops@mail.com"
    recipient = "devsecops@mail.com"
    subject = "SMTP Test Email"
    body = "Hello, this is a test email from Amazon SES."

    email_sender = AmazonSESEmailSender(smtp_username, smtp_password, smtp_server, port)
    email_sender.send_email(sender, recipient, subject, body)
