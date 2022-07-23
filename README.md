# Cobol in AWS Lambda

This is probably totally useless in a production setting, but still a good exercise to understand what you can do with containers in AWS Lambda.

## What are you getting?

This code uses a python lambda handler to call an underlying Cobol program. In practical terms this is an adaptation of your typical container deployment of a lambda function (see [tutorial](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)), whereby the [AWS Runtime Interface Client](https://github.com/aws/aws-lambda-python-runtime-interface-client)) calls the (python) handler function that has been defined. In this case the extra twist comes from the fact the python handler then calls the Cobol program under test and collects the output.

Note that this is by no means optimized or production-ready. More than anything else it is an experiment to see what can be done with containers + AWS Lambda.

## Deployment to AWS Lambda:

In order to deploy this to AWS Lambda you need to first upload the docker image to ECR, and then use that image as the basis for the Lambda function.
This container image uses the `x86_64` architecture.

### Pre-requisites

- AWS Account
- AWS CLI installed on your machine
- Docker installed on your machine

### Uploading the docker image to ECR

- Build the docker image: `docker build -t container-lambda:latest .`
- Login to ECR (see [full example](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html#cli-authenticate-registry)): `aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com` (replace `region` and `aws_account_id` with the appropriate values)
- Tag the image: `docker tag container-lambda:latest aws_account_id.dkr.ecr.region.amazonaws.com/container-lambda:latest`
- Push the image: `docker push aws_account_id.dkr.ecr.region.amazonaws.com/container-lambda:latest`

### Creating a Lambda from your image:

- Follow this [tutorial](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-images.html#configuration-images-create)
