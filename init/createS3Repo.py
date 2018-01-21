##Create S3 repo to store Jenkins Plugins.

import boto3

bucketName = "JenkinsPlugins"

def createBucket(bucketName):
	#Create an S3 bucket
	s3.create_bucket(Bucket=bucketName)
	
s3 = boto3.client('s3')
s3.upload_file("jenkinsPlugins.py", "JenkinsPlugins", "jenkinsPlugins.py")