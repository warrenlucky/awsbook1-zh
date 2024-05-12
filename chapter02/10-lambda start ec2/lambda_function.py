import boto3

def lambda_handler(event, context):
    # 定义 EC2 实例的参数
    instance_params = {
        'ImageId': ' ami-0f4dfdbd0b33c2e4c',  # AMI ID
        'InstanceType': 't3.micro',  # 实例类型
        'KeyName': 'your-key-pair',  # 替换为您的密钥对名称
        'MinCount': 1,  # 最小实例数
        'MaxCount': 1,  # 最大实例数
    }

    # 创建 EC2 实例
    ec2_client = boto3.client('ec2', region_name='your-region')  # 替换 AWS 区域
    response = ec2_client.run_instances(**instance_params)
    # 提取新创建的实例 ID
    instance_id = response['Instances'][0]['InstanceId']

    return {
        'statusCode': 200,
        'body': f'EC2 instance {instance_id} has been successfully launched.'
    }