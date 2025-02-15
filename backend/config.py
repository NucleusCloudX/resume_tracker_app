import os

class Config:
    # Use 'db' as the hostname for MySQL when running in Docker Compose.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "mysql+pymysql://root:password@db/resume_matcher"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AWS_SES_REGION = "us-east-1"
    AWS_SES_SENDER = "your-email@example.com"
