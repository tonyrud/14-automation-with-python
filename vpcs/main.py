import boto3

def vpcs(region_name='us-east-2'):
    ec2 = boto3.client('ec2', region_name=region_name)

    response = ec2.describe_vpcs()

    vpcs = response["Vpcs"]

    for vpc in vpcs:
        print("VPC ID :")
        print(vpc["VpcId"])
        print(vpc["CidrBlock"])
        cidr_block_sets = vpc["CidrBlockAssociationSet"]

        print("CidrBlockAssociationSet :")
        for cidr_block_set in cidr_block_sets:
            print(cidr_block_set["CidrBlock"])
            print(cidr_block_set["AssociationId"])
            print(cidr_block_set["CidrBlockState"]["State"])
        
        print("\n")

vpcs()