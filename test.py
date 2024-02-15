def lambda_handler(event, context):
    # Change the greeting message as per your requirement
    message = "Hello, world!"
    return {
        'statusCode': 200,
        'body': message
    }
