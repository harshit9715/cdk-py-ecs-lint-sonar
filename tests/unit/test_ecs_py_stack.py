import aws_cdk as core
import aws_cdk.assertions as assertions

from ecs_py.ecs_py_stack import EcsPyStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ecs_py/ecs_py_stack.py


def test_sqs_queue_created():
    app = core.App()
    stack = EcsPyStack(app, "ecs-py")
    template = assertions.Template.from_stack(stack)

    template.to_json()
    # template.has_resource_properties("AWS::SQS::Queue", {
    #     "VisibilityTimeout": 300
    # })
