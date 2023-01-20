import aws_cdk as core
import aws_cdk.assertions as assertions

from ecs_py.ecs_py_stack import EcsPyStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ecs_py/ecs_py_stack.py
app = core.App()
stack = EcsPyStack(app, "ecs-py")
template = assertions.Template.from_stack(stack)


def test_vpc_created():
    template.resource_count_is("AWS::EC2::VPC", 1)


def test_nat_created():
    template.resource_count_is("AWS::EC2::NatGateway", 2)


def test_igw_created():
    template.resource_count_is("AWS::EC2::InternetGateway", 1)


def test_subnets_are_created():
    template.resource_count_is("AWS::EC2::Subnet", 4)
