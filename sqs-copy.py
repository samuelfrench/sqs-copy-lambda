import json
import boto3

def lambda_handler(event, context):
    sqs = boto3.resource('sqs');
    queue = sqs.get_queue_by_name(QueueName='fifo_queue_poc.fifo')
    response = queue.send_message(
        MessageBody=json.dumps(event),
        DelaySeconds=0,
        MessageAttributes={},
        MessageGroupId='test'
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

