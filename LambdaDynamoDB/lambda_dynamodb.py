import json
import boto3
from botocore.exceptions import ClientError

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('user-details')  # Replace with your table name

def lambda_handler(event, context):
    # User details to be saved
    user_details = {
        'email': event['email'],  # Partition key
        'firstname': event['firstname'],
        'lastname': event['lastname'],
        'age': event['age'],
        'location': event['location']
    }
    
    # Put item into DynamoDB
    try:
        table.put_item(Item=user_details)
        return {
            'statusCode': 200,
            'body': json.dumps('User details saved successfully!')
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Failed to save user details: {e.response['Error']['Message']}")
        }
        