# Auto Start AWS EC2 Instances
### This is a Python script to automate the starting and running of AWS EC2 instances. It uses the boto3 library to interact with the AWS API, and the paramiko library to remotely connect to the EC2 instances.

## Getting Started
- Prerequisites
- Python 3.x
- boto3 library (pip install boto3)
- paramiko library (pip install paramiko)
- AWS access key ID and secret access key with appropriate permissions
- .pem key pair file for connecting to EC2 instances

## Installation
### Clone this repository:

```
git clone https://github.com/paritoshtripathi935/paritoshLibraries
cd Aws

```
### Install the required libraries:

```
pip install -r requirements.txt
```
### Set the necessary environment variables in a .env file in the root directory of the project:

```
AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
REGION=<your_aws_region>
INSTANCE_IDS=<comma_separated_list_of_instance_ids>
INSTANCE_1_PATH=<path_to_main_py_file_on_instance_1>
INSTANCE_2_PATH=<path_to_main_py_file_on_instance_2>
```
### Run the script:

```
python ec2_runner.py
```

## Usage
### The EC2Runner class provides two methods: start_instance and stop_instance. To start an EC2 instance and run a Python script on it, call the start_instance method with the instance ID and the path to the Python script as arguments:

```
runner = EC2Runner(aws_access_key_id, aws_secret_access_key, region, key_pair_name)

instance_id = 'i-0123456789abcdef0'
instance_path = '/path/to/main.py'

runner.start_instance(instance_id, instance_path)
```
### To stop an EC2 instance, call the stop_instance method with the instance ID as an argument:

```
runner = EC2Runner(aws_access_key_id, aws_secret_access_key, region, key_pair_name)

instance_id = 'i-0123456789abcdef0'

runner.stop_instance(instance_id)
```
## The script provided in ec2_runner.py starts two instances with the specified instance IDs and Python script paths, waits for the first instance to shut down, and then starts the second instance. You can modify this script to fit your use case.





