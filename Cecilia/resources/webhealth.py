import json
from aws_cdk import aws_cloudwatch as cloudwatch
def lambda_handler(event, context):
    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch/Metric.html

    # metric = cloudwatch.Metric("","")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
