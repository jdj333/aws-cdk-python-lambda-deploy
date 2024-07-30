#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_apigateway as apigateway

class MyApiStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda function
        my_lambda = lambda_.Function(self, "MyLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="lambda_function.lambda_handler",
            code=lambda_.Code.from_asset("lambda")
        )

        # Define the API Gateway
        api = apigateway.LambdaRestApi(self, "MyApi",
            handler=my_lambda,
            proxy=False
        )

        items = api.root.add_resource("items")
        items.add_method("GET")    # GET /items
        items.add_method("POST")   # POST /items

app = cdk.App()
MyApiStack(app, "MyApiStack")
app.synth()
