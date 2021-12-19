import json
import boto3
import time

client = boto3.client('firehose')

log_types = ['hadoop', 'hdfs', 'spark', 'zoo_keeper']

for log_type in log_types:

	counter = 0

	with open('./sample_logs/' + log_type + '.txt', encoding='utf-8') as log_file:
    
		for row in log_file:
		
			data = '{"log_message":"' + row.strip() + '"}'

			response = client.put_record(
    			DeliveryStreamName='workshop-firehose',
    			Record={
        			'Data': data
    			}
			)

			# time.sleep(1)

			print(log_type + " log # " + str(counter) + " / " + '2000' + " sent")

			counter = counter + 1