from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
    RemovalPolicy,
    aws_events as events_,

    # aws_sqs as sqs,
)
from constructs import Construct

class CeciliaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_lambda/Function.html

        fn = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="index.handler",
            code=lambda_.Code.from_asset("./resources")
        )
        fn.apply_removal_policy(RemovalPolicy.DESTROY)

        # TODO: Make Event
        # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_events/README.html       
        
