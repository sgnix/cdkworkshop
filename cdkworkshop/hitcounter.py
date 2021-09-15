from aws_cdk import (
    aws_lambda as _lambda,
    core
)

class HitCounter(core.Construct):

    def __init__(self, scope: core.Construct, id: str, downstream: _lambda.IFunction, **kwargs) -> None:
        super().__init__(scope, id, kwargs)