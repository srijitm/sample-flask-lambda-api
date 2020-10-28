# Sample Flask Fargate API
**Note: This is not Production grade and simply meant as a demo**

## Description

This project demonstrates how a Flask application can be deployed to Lambda without re-writing. An API Gateway sits infront and simply routes all requests to the Lambda function. The Lambda function itself uses the routes (as defined in Flask). This application provides endpoints to upload/download an image (jpeg) to/from S3.

## Usage

Postman collection is included. Just update the URL to point to your API Gateway endpoint. The sls deploy command output will contain the endpoint.

## Instructions

- Activate venv

- Download and configure AWS CLI (if not done already): 
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

- Install Serverless Framework and plugins

```bash
npm install -g serverless
npm install serverless-wsgi serverless-python-requirements --save-dev
```

- Update app.py (line 7) to point to an existing S3 bucket 
```py
bucket = 'my-playpen'
```

- Deploy (from root dir)

```bash
sls deploy
```
