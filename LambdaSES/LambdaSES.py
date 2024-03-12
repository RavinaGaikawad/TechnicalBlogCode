import boto3

def lambda_handler(event, context):
    # Extract the message from the event
    user_message = event.get('user_message')

    # Add additional details to the message
    enhanced_message = add_details(user_message)

    # Send the enhanced message via email using SES
    send_email(enhanced_message)

    return {
        'statusCode': 200,
        'body': 'Execution successful!'
    }

def add_details(message):
    # Add your logic to enhance the message here
    # For example, adding details like greetings
    enhanced_message = f"Greetings! {message} - Additional details added."

    return enhanced_message

def send_email(message):
    # AWS SES configuration
    aws_region = 'your_aws_region'
    sender_email = 'your_sender_email@example.com'
    recipient_email = 'recipient@example.com'

    # Create an SES client
    ses_client = boto3.client('ses', region_name=aws_region)

    # Try to send the email
    try:
        # Provide the contents of the email
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [recipient_email],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': message,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'Enhanced Message',
                },
            },
            Source=sender_email,
        )
        print("Email sent successfully! Message ID:", response['MessageId'])
    except Exception as e:
        print(f"Error sending email: {e}")