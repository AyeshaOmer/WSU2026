from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as lambda_,
    # aws_sqs as sqs,
)
from constructs import Construct

class CeciliaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="index.handler",
            code=lambda_.Code.from_asset("./resources")
)
        fn.apply_removal_policy(RemovalPolicy.DESTROY)
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CeciliaQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
