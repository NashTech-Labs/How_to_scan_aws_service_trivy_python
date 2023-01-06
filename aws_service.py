import os
import sys
print("Aws Service you want to scan")
options=["ec2" , "s3" , "sqs" , "sns" , "eks"]
print(options)
awsservice = input ("Enter aws service")
print(awsservice)
d=awsservice
cmd = 'sudo trivy aws --service' +d
os.system(cmd)
