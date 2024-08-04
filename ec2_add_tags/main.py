import boto3

ec2_client_east_2 = boto3.client('ec2', region_name="us-east-2")
ec2_resource_east_2 = boto3.resource('ec2', region_name="us-east-2")

ec2_client_east_1 = boto3.client('ec2', region_name="us-east-1")
ec2_resource_east_1 = boto3.resource('ec2', region_name="us-east-1")

instance_ids_east_2 = []
instance_ids_east_1 = []

reservations_east_2 = ec2_client_east_2.describe_instances()['Reservations']
for res in reservations_east_2:
    instances = res['Instances']
    for ins in instances:
        instance_ids_east_2.append(ins['InstanceId'])


response = ec2_resource_east_2.create_tags(
    Resources=instance_ids_east_2,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

reservations_east_1 = ec2_client_east_1.describe_instances()['Reservations']
for res in reservations_east_1:
    instances = res['Instances']
    for ins in instances:
        instance_ids_east_1.append(ins['InstanceId'])


response = ec2_resource_east_1.create_tags(
    Resources=instance_ids_east_1,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
