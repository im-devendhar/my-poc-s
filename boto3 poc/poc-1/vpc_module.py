import boto3

# Create EC2 client in N. Virginia region
ec2 = boto3.client("ec2", region_name="us-east-1")

def create_vpc():
    # Step 1: Create VPC
    response = ec2.create_vpc(
        CidrBlock="10.0.0.0/16"
    )
    vpc_id = response["Vpc"]["VpcId"]

    # Step 2: Enable DNS features
    ec2.modify_vpc_attribute(
        VpcId=vpc_id,
        EnableDnsSupport={"Value": True}
    )

    ec2.modify_vpc_attribute(
        VpcId=vpc_id,
        EnableDnsHostnames={"Value": True}
    )

    print(f"VPC Created: {vpc_id}")
    return vpc_id

