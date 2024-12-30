import boto3
import os

dynamodb = boto3.resource("dynamodb", region_name=os.getenv("AWS_REGION", "us-east-1"))
users_table = dynamodb.Table("Users")
