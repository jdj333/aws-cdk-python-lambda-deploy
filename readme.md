# My AWS CDK Python Project

This project contains an AWS CDK stack that deploys an API Gateway backed by a Lambda function. The Lambda function is written in Python and handles HTTP GET and POST requests.

## Project Structure

```
cdk_project/
├── app.py
├── lambda/
│   └── lambda_function.py
├── requirements.txt
└── .github/
    └── workflows/
        └── deploy.yml
```

## Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured.
- [Node.js](https://nodejs.org/) (for AWS CDK) installed.
- [Python 3.9](https://www.python.org/downloads/) installed.
- [AWS CDK](https://aws.amazon.com/cdk/) installed globally.

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name/cdk_project
    ```

2. **Install dependencies:**

    ```sh
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    npm install -g aws-cdk
    ```

3. **Bootstrap your environment (if not already done):**

    ```sh
    cdk bootstrap aws://ACCOUNT-NUMBER/REGION
    ```

## CDK Commands

1. **Synthesize the CloudFormation template:**

    ```sh
    cdk synth
    ```

2. **Deploy the stack:**

    ```sh
    cdk deploy
    ```

3. **Destroy the stack:**

    ```sh
    cdk destroy
    ```

4. **Check the diff between deployed stack and local changes:**

    ```sh
    cdk diff
    ```

## Lambda Function

The Lambda function code is located in the `lambda/` directory. The function handles GET and POST requests.

**Relative Path: `cdk_project/lambda/lambda_function.py`**

```python
import json

def lambda_handler(event, context):
    method = event['httpMethod']
    
    if method == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps('GET method called')
        }
    elif method == 'POST':
        return {
            'statusCode': 200,
            'body': json.dumps('POST method called')
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Unsupported method: {method}')
        }
```

## GitHub Actions Deployment

This project includes a GitHub Actions workflow for automatic deployment.

**Relative Path: `.github/workflows/deploy.yml`**

```yaml
name: Deploy CDK Stack

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          npm install -g aws-cdk

      - name: CDK Deploy
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_DEFAULT_REGION: 'us-west-2'
        run: cdk deploy --require-approval never
```

## Setting Up GitHub Secrets

Ensure you have the following secrets set up in your GitHub repository:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

## Useful Links

- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/index.html)
- [AWS API Gateway Documentation](https://docs.aws.amazon.com/apigateway/index.html)
