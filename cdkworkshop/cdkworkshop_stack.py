from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)

class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='hello.handler'
        )

        apigw.LambdaRestApi(self, 'Endpoint', handler=hello_lambda)
