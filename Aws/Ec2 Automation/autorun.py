import boto3
import paramiko
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class EC2Runner:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region, key_name):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region = region
        self.key_name = key_name
        self.ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region)

    def start_instance(self, instance_id, instance_path):
        try:
            # Start the instance
            self.ec2.start_instances(InstanceIds=[instance_id])
            print(f'Started instance: {instance_id}')

            time.sleep(60)
            # Wait for the instance to start running
            waiter = self.ec2.get_waiter('instance_running')
            waiter.wait(InstanceIds=[instance_id])
            print(f'Instance {instance_id} is now running')

            # Get the public IP address of the instance
            response = self.ec2.describe_instances(InstanceIds=[instance_id])
            instance = response['Reservations'][0]['Instances'][0]
            instance_ip = instance['PublicIpAddress']

            # Connect to the instance and run main.py in a tmux session
            print(f'Connecting to instance {instance_id} ({instance_ip})')
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh_client.connect(instance_ip, username='ubuntu', key_filename=f'{self.key_name}.pem')
            print(f'Connected to instance {instance_id} ({instance_ip})')

            # Create a tmux session and run main.py inside it
            session_name = 'new_session'
            command = f'cd /home/ubuntu/Paritosh-Scrapers && tmux new-session -d -s {session_name}; tmux send-keys "python3 {instance_path}" C-m'
            stdin, stdout, stderr = ssh_client.exec_command(command)
            print(f'Results from instance {instance_id}:')
            print(stdout.read().decode('utf-8'))

            ssh_client.close()
            print(f'Finished running main.py on instance {instance_id}')

            return True, instance_id

        except Exception as e:
            print(f'Error while starting instance {instance_id}: {e}')
            return False, instance_id

    def stop_instance(self, instance_id):
        try:
            # Stop the instance
            self.ec2.stop_instances(InstanceIds=[instance_id])
            print(f'Stopped instance: {instance_id}')

            # Wait for the instance to stop running
            waiter = self.ec2.get_waiter('instance_stopped')
            waiter.wait(InstanceIds=[instance_id])
            print(f'Instance {instance_id} has stopped')

            return True, instance_id

        except Exception as e:
            print(f'Error while stopping instance {instance_id}: {e}')
            return False, instance_id
