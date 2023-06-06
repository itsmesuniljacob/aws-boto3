import boto3

def get_worker_nodes(cluster_name):
    eks_client = boto3.client('eks')
    response = eks_client.describe_nodegroup(clusterName=cluster_name, nodegroupName='your-nodegroup-name')
    return response['nodegroup']['nodegroupArn']

def get_worker_node_instances(nodegroup_arn):
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'tag:aws:eks:nodegroup-name',
                'Values': [nodegroup_arn]
            }
        ]
    )
    return response['Reservations']

def check_ami(worker_nodes, required_ami):
    for reservation in worker_nodes:
        for instance in reservation['Instances']:
            if instance['ImageId'] != required_ami:
                return False
    return True

def main():
    cluster_name = 'your-cluster-name'
    required_ami = 'your-required-ami-id'

    nodegroup_arn = get_worker_nodes(cluster_name)
    worker_nodes = get_worker_node_instances(nodegroup_arn)

    if check_ami(worker_nodes, required_ami):
        print("All worker nodes have the required AMI.")
    else:
        print("Not all worker nodes have the required AMI.")

if __name__ == '__main__':
    main()
