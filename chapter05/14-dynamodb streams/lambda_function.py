from __future__ import print_function

def lambda_handler(event, context):
    # 遍历处理事件中的每一条记录
    for record in event['Records']:
        # 打印事件的唯一标识符
        print(record['eventID'])
        # 打印事件的类型（例如，INSERT、MODIFY 或 REMOVE）
        print(record['eventName'])
    # 打印处理的记录总数
    print('Successfully processed %s records.' % str(len(event['Records'])))