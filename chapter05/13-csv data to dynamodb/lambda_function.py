import json
import boto3
import csv
from io import StringIO

print('Loading function')
# 初始化 AWS 服务
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('替换为要导入数据的dynamodb表名称')

def lambda_handler(event, context):
    # 从事件中获取对象并显示其内容类型
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read().decode('utf-8')
    # 解析CSV数据
    csv_data = csv.reader(StringIO(data))
    for row in csv_data:
        if len(row) == 3:  # 检查每行是否有三列数据
            try:
                # 将数据写入DynamoDB
                table.put_item(
                    Item={
                        'id': row[0],
                        'name': row[1],
                        'age': row[2]
                    }
                )
            except Exception as e:
                print('Error:', str(e))  # 打印错误信息
        else:
            print('Invalid data row:', row)  # 打印无效数据行