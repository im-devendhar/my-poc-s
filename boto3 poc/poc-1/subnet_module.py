import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")

def create_subnet(vpc_id):
    response = ec2.create_subnet(
        VpcId=vpc_id,
        CidrBlock="10.0.1.0/24",
        AvailabilityZone="us-east-1a"
    )

    subnet_id = response["Subnet"]["SubnetId"]

    print(f"Subnet Created: {subnet_id}")
    return subnet_id

