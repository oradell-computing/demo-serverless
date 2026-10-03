import aws_cdk as core
import aws_cdk.assertions as assertions

from demo_serverless.demo_serverless_stack import DemoServerlessStack

# example tests. To run these tests, uncomment this file along with the example
# resource in demo_serverless/demo_serverless_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DemoServerlessStack(app, "demo-serverless")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
