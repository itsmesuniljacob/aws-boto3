# AWS Boto3

`Boto3` is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts.

## Usage

To install Boto3 on your computer, go to your terminal and run the following:

```$ pip install boto3```

You’ve got the SDK. But, you won’t be able to use it right now, because it doesn’t know which AWS account it should connect to.

To make it run against your AWS account, you’ll need to provide some valid credentials. If you already have an IAM user that has full permissions to S3, you can use those user’s credentials (their access key and their secret access key) without needing to create a new user. Otherwise, the easiest way to do this is to create a new AWS user and then store the new credentials.

This repo houses some Python Boto3 scripts for AWS.

#Placeholder-More details to follow
