# CodeBuild Polyglot Application

Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0

***

With microservices becoming new normal, it's natural to use multiple different programming languages for different microservices in the same application. [AWS CodeBuild adds support for polyglot build](https://aws.amazon.com/about-aws/whats-new/2019/07/aws-codebuild-adds-support-for-polyglot-builds/) using runtime versions. This repo contains 3 different microservices named microservices-greeting(*Python*), microservices-name(*JavaScript*) and microservices-webapp(*Java*) written in different programming languages. Using one CodeBuild project all these microservices can be built and packaged ready to be deployed using AWS CloudFormation.

Once the microservices are built successfully, it will get deployed locally using [AWS SAM CLI local](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-api.html_) command all the microservices will be launched locally connecting to [DynamoDB on Docker](https://hub.docker.com/r/amazon/dynamodb-local) locally. CodeBuild includes headless browsers as part of it's containers and using those headless browsers UI testing will be performed to validate the build.

***

### Steps to deploy this Application

Step 1: Create an AWS CodeCommit repository following [the documentation](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html) and checkout the newly create repository.

Step 2: Copy the content of this GitHub repository to your newly created CodeCommit repository and run `git push` to upload the content to the remote repostiory.

Step 3: Create a CloudFormation stack using the `polyglot-app-pipeline.yaml` template to launch the pipeline in AWS CodePipeline.