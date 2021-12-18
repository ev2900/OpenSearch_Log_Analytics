import json
import csv
import boto3

client = boto3.client('firehose')

response = client.put_record(
    DeliveryStreamName='workshop-firehose',
    Record={
        'Data': b'{"Name":"Chris"}'
    }
)

print("Sent!")