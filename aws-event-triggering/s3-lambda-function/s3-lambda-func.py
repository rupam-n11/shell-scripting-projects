import boto3
import json

def lambda_handler(event, context):
    # Extract relevant information from the S3 event trigger
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['objects']['key']

    # Perfrom desired operations with the uploaded file
    print(f"File '{object_key}' was uploaded to bucket '{bucket_name}'")

    # Example: Send a notification via SNS
    sns_client = boto3.client('sns')
    topic_arn = 'arn:aws:sns:ap-south-1:940482450806:s3-lambda-sns'
    sns_client.publish(
            TopicArn=topic_arn,
            Subject='S3 Object Created',
            Message=f"File '{object_key}' was uploaded to bucket '{bucket_name}'
    )

    # Example: Trigger another lambda function
    # lambda_client = boto3.client('lambda')
    # target_function_name = 'my-another-lambda-function'
    # lambda_client.invoke(
    #    FunctionName=target_function_name,
    #    InvocationType='Event',
    #    Payload=json.dumps({'bucket_name': bucket_name, 'object_key': object_key})
    # )

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully')
    }

