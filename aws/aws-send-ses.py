import boto3
from botocore.exceptions import BotoCoreError, ClientError

"""
pip3 install boto3
"""

class SESEmailSender:
    def __init__(self, region_name, aws_access_key_id, aws_secret_access_key):
        self.client = boto3.client(
            'ses',
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    def send_email(self, source, to_addresses, subject, body):
        try:
            response = self.client.send_email(
                Destination={
                    'ToAddresses': to_addresses,
                },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': 'UTF-8',
                            'Data': body,
                        },
                    },
                    'Subject': {
                        'Charset': 'UTF-8',
                        'Data': subject,
                    },
                },
                Source=source,
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])

def main():
    sender = SESEmailSender(
        region_name='ap-southeast-1', 
        aws_access_key_id='XXXXXXXXXX', 
        aws_secret_access_key='XXXXXXXXXX' 
    )

    sender_email = 'devsecops@gmail.com'
    send_to = 'test@mail.com'
    subject = 'AWS TEST SES EMAIL'
    body = """
    Hello, 

    This is a test email being sent via Amazon Simple Email Service (SES).
    We are utilizing this service to streamline our email processes and improve our communication strategies.

    Kind Regards,
    DevSecOps
    """

    sender.send_email(
        source=sender_email,
        to_addresses=[send_to], 
        subject=subject, 
        body=body
    )

if __name__ == "__main__":
    main()
