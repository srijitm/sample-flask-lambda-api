# Instructions

- Activate venv

- Download and configure AWS CLI (if not done already): 
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

- Install Serverless Framework and plugins

```bash
npm install -g serverless
npm install serverless-wsgi serverless-python-requirements --save-dev
```

- Deploy (from root dir)

```bash
sls deploy
```
