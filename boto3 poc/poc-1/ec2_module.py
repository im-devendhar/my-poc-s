import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")

def create_ec2(subnet_id):
    response = ec2.run_instances(
        ImageId="ami-04b70fa74e45c3917",   
        InstanceType="t3.micro",
        MaxCount=1,
        MinCount=1,
        SubnetId=subnet_id
    )

    instance_id = response["Instances"][0]["InstanceId"]

    print(f"EC2 Instance Launched: {instance_id}")
    return instance_id

