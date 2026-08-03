import aws_cdk as core
import aws_cdk.assertions as assertions

from 22079314.22079314_stack import 22079314Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in 22079314/22079314_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 22079314Stack(app, "22079314")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
