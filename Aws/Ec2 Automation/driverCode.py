import boto3
from ec2_runner import EC2Runner

# Replace with your AWS access key ID and secret access key
aws_access_key_id = 'your-access-key-id'
aws_secret_access_key = 'your-secret-access-key'

# Replace with the region where your instances are located
region = 'your-region'

# Replace with the paths to the main.py file on each instance
instance1_path = '/path/to/instance1/main.py'
instance2_path = '/path/to/instance2/main.py'

# Replace with the name of your key pair file (without .pem extension)
key_pair_name = '/path/to/key/pair'

# Replace with the IDs of your instances
instance_ids = ['instance-id-1', 'instance-id-2']

# Create an instance of the EC2Runner class
runner = EC2Runner(aws_access_key_id, aws_secret_access_key, region, key_pair_name)

# Start instance 1 and run main.py
instance1_id = instance_ids[0]
success, instance_id = runner.start_instance(instance1_id, instance1_path)
if success:
    print(f'Successfully started instance {instance_id} and ran main.py')
else:
    print(f'Failed to start instance {instance_id} and run main.py')

# Stop instance 1
success, instance_id = runner.stop_instance(instance1_id)
if success:
    print(f'Successfully stopped instance {instance_id}')
else:
    print(f'Failed to stop instance {instance_id}')

# Start instance 2 and run main.py
instance2_id = instance_ids[1]
success, instance_id = runner.start_instance(instance2_id, instance2_path)
if success:
    print(f'Successfully started instance {instance_id} and ran main.py')
else:
    print(f'Failed to start instance {instance_id} and run main.py')

# Stop instance 2
success, instance_id = runner.stop_instance(instance2_id)
if success:
    print(f'Successfully stopped instance {instance_id}')
else:
    print(f'Failed to stop instance {instance_id}')


# Note that you'll need to replace the values for aws_access_key_id, aws_secret_access_key, region, instance1_path, instance2_path, key_pair_name, and instance_ids with your own values.