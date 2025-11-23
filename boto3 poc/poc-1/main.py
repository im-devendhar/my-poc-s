from vpc_module import create_vpc
from subnet_module import create_subnet
from ec2_module import create_ec2

def main():
    print("\n--- AWS Automation Started ---")

    # Step 1: Create VPC
    vpc_id = create_vpc()

    # Step 2: Create subnet inside the VPC
    subnet_id = create_subnet(vpc_id)

    # Step 3: Create EC2 instance in the subnet
    instance_id = create_ec2(subnet_id)

    print("\n--- Final Results ---")
    print("VPC ID:", vpc_id)
    print("Subnet ID:", subnet_id)
    print("EC2 Instance ID:", instance_id)

main()

