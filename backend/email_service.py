import boto3
from config import Config

def send_email(to_email, match_score):
    client = boto3.client("ses", region_name=Config.AWS_SES_REGION)
    subject = "Your Resume Match Score"
    body = f"Your resume matches the job description with a score of {match_score}%."
    
    response = client.send_email(
        Source=Config.AWS_SES_SENDER,
        Destination={"ToAddresses": [to_email]},
        Message={
            "Subject": {"Data": subject},
            "Body": {"Text": {"Data": body}}
        }
    )
    return response
