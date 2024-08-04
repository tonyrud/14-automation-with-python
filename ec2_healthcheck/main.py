import boto3

def ec2_healthcheck(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)
    return response


ec2_healthcheck({}, {})