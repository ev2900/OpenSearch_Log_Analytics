import os
import re
import boto3

print("---------------------------------")
print("Starting - hugo build -----------")
print("---------------------------------")

os.system('hugo')

print("---------------------------------")
print("Finished - hugo build -----------")
print("---------------------------------")

print("")

print("---------------------------------")
print("Starting - html clean up --------")
print("---------------------------------")

l1 = [
	'./public/index.html'
]

l2 = [
	'./public/open-search-log-analytics/index.html',
	'./public/open-search-log-analytics/1_getting_started.html',
	'./public/open-search-log-analytics/2_environment_set_up.html',
	'./public/open-search-log-analytics/3_send_log_data_to_kinesis_fire_hose.html',
	'./public/open-search-log-analytics/4_visualize_analyze.html',
	'./public/open-search-log-analytics/5_clean_up.html',
	'./public/collect-log-cloud-watch/index.html',
	'./public/collect-log-cloud-watch/1_getting_started.html',
	'./public/collect-log-cloud-watch/2_environment_set_up.html',
	'./public/collect-log-cloud-watch/3_send_log_data_to_opensearch.html',
	'./public/collect-log-cloud-watch/4_search_logs.html',
	'./public/collect-log-cloud-watch/5_clean_up.html',
	'./public/open-search-fluentd/index.html',
	'./public/open-search-fluentd/1_getting_started.html',
	'./public/open-search-fluentd/2_environment_set_up.html',
	'./public/open-search-fluentd/3_configure_fluentd.html',
	'./public/open-search-fluentd/4_search_logs.html',
	'./public/open-search-fluentd/5_clean_up.html',
	'./public/anomaly-detection-w-msk/index.html',
	'./public/anomaly-detection-w-msk/1_getting_started.html',
	'./public/anomaly-detection-w-msk/2_environment_set_up.html',
	'./public/anomaly-detection-w-msk/3_configure_lambda.html',
	'./public/anomaly-detection-w-msk/4_send_logs.html',
	'./public/anomaly-detection-w-msk/5_anomaly_detection.html',
	'./public/anomaly-detection-w-msk/6_clean_up.html'
]

l3 = [
	'./public/open-search-log-analytics/1_getting_started/aws_event.html',
	'./public/open-search-log-analytics/1_getting_started/self_paced.html',
	'./public/open-search-log-analytics/2_environment_set_up/cloudformation_automated.html',
	'./public/open-search-log-analytics/2_environment_set_up/console_manual.html',
	'./public/collect-log-cloud-watch/1_getting_started/aws_event.html',
	'./public/collect-log-cloud-watch/1_getting_started/self_paced.html',
	'./public/open-search-fluentd/1_getting_started/aws_event.html',
	'./public/open-search-fluentd/1_getting_started/self_paced.html',
	'./public/open-search-fluentd/2_environment_set_up/cloudformation_automated.html',
	'./public/anomaly-detection-w-msk/1_getting_started/aws_event.html',
	'./public/anomaly-detection-w-msk/1_getting_started/self_paced.html',
	'./public/anomaly-detection-w-msk/2_environment_set_up/cloudformation_automated.html'
]

for html_file in l1:

	with open(html_file, "r+") as html_object:

		html = html_object.read()
		html_object.seek(0)
		
		c1 = re.sub(r'<a href="./open-search-log-analytics/">', '<a href="./open-search-log-analytics/index.html">', html)
		c2 = re.sub(r'<a href="./collect-log-cloud-watch/"', '<a href="./collect-log-cloud-watch/index.html"', c1)
		c3 = re.sub(r'<a href="./open-search-fluentd/"', '<a href="./open-search-fluentd/index.html"', c2)
		c4 = re.sub(r'<a href="./anomaly-detection-w-msk/"', '<a href="./anomaly-detection-w-msk/index.html"', c3)
		
		c5 = re.sub(r'<a class="nav nav-next" href="./open-search-log-analytics/"', '<a class="nav nav-next" href="./open-search-log-analytics/index.html"', c4)
		
		html_object.write(c5)
		html_object.truncate()

		print("Finished file " + html_file)

for html_file in l2:

	with open(html_file, "r+") as html_object:

		html = html_object.read()
		html_object.seek(0)
		
		html_object_1 = re.sub(r'<a href="*..*/open-search-log-analytics/">', '<a href="../open-search-log-analytics/index.html">', html)
		html_object_2 = re.sub(r'<a href="*..*/collect-log-cloud-watch/">', '<a href="../collect-log-cloud-watch/index.html">', html_object_1)
		html_object_3 = re.sub(r'<a href="*..*/open-search-fluentd/">', '<a href="../open-search-fluentd/index.html">', html_object_2)
		html_object_4 = re.sub(r'<a href="*..*/anomaly-detection-w-msk/">', '<a href="../anomaly-detection-w-msk/index.html">', html_object_3)
		
		html_object_5 = re.sub(r'<a href=\'..\/\'>OpenSearch Log Analytics Workshop</a> > 2. CloudWatch Log Collection', '<a href=\'../index.html\'>OpenSearch Log Analytics Workshop</a> > CloudWatch Log Collection', html_object_4)
		html_object_6 = re.sub(r'<a href=\'..\/\'>OpenSearch Log Analytics Workshop</a> > 1. OpenSearch Log Analytics', '<a href=\'../index.html\'>OpenSearch Log Analytics Workshop</a> > OpenSearch Log Analytics', html_object_5)

		html_object_7 = re.sub(r'<a href=\'..\/\'>OpenSearch Log Analytics Workshop</a> > <a href=\'../open-search-log-analytics/\'>1. OpenSearch Log Analytics</a> > 1. Getting started', '<a href=\'../index.html\'>OpenSearch Log Analytics Workshop</a> > <a href=\'../open-search-log-analytics/index.html\'>OpenSearch Log Analytics</a> > 1. Getting started', html_object_6)
		html_object_8 = re.sub(r'<a href=\'..\/\'>OpenSearch Log Analytics Workshop</a> > <a href=\'../collect-log-cloud-watch/\'>2. CloudWatch Log Collection</a> > 1. Getting started', '<a href=\'../index.html\'>OpenSearch Log Analytics Workshop</a> > <a href=\'../collect-log-cloud-watch/index.html\'>CloudWatch Log Collection</a> > 1. Getting started', html_object_7)

		html_object_9 = re.sub(r'> 1. Getting started', '> Getting started', html_object_8)

		html_object_10 = re.sub(r'> <a href=\'../open-search-log-analytics/\'>1. OpenSearch Log Analytics</a>', '> <a href=\'../open-search-log-analytics/index.html\'>OpenSearch Log Analytics</a>', html_object_9)
		html_object_11 = re.sub(r'> 2. Environment Set Up', '> Environment Set Up', html_object_10)

		html_object_12 = re.sub(r'> 3. Send Log Data to Kinesis Fire Hose', '> Send Log Data to Kinesis Fire Hose', html_object_11)
		html_object_13 = re.sub(r'Analytics</a> > 5. Clean Up', 'Analytics</a> > Clean Up', html_object_12)

		html_object_14 = re.sub(r'Analytics</a> > 5. Clean Up', 'Analytics</a> > Clean Up', html_object_13)

		html_object_15 = re.sub(r'> <a href=\'../open-search-log-analytics/\'>1. OpenSearch Log Analytics</a>', '> <a href=\'../open-search-log-analytics/index.html\'>OpenSearch Log Analytics</a>', html_object_14)
		html_object_16 = re.sub(r'> 4. Visualize and Analyze', '> Visualize and Analyze', html_object_15)

		html_object_17 = re.sub(r'> <a href=\'../collect-log-cloud-watch/\'>2. CloudWatch Log Collection</a>', '> <a href=\'../collect-log-cloud-watch/index.html\'>CloudWatch Log Collection</a>', html_object_16)

		html_object_18 = re.sub(r'> 3. Send Log Data to OpenSearch', '> Send Log Data to OpenSearch', html_object_17)
		html_object_19 = re.sub(r'> 4. Search Logs', '> Search Logs', html_object_18)

		html_object_20 = re.sub(r'> 5. Clean Up', '> Clean Up', html_object_19)		

		html_object.write(html_object_20)
		html_object.truncate()

		print("Finished file " + html_file)

for html_file in l3:
		
		with open(html_file, "r+") as html_object:

			html = html_object.read()
			html_object.seek(0)
			
			html_object_1 = re.sub(r'<a href="*..*/open-search-log-analytics/">', '<a href="../../open-search-log-analytics/index.html">', html)
			html_object_2 = re.sub(r'<a href="*..*/collect-log-cloud-watch/">', '<a href="../../collect-log-cloud-watch/index.html">', html_object_1)
			html_object_3 = re.sub(r'<a href="*..*/open-search-fluentd/">', '<a href="../../open-search-fluentd/index.html">', html_object_2)
			html_object_4 = re.sub(r'<a href="*..*/anomaly-detection-w-msk/">', '<a href="../../anomaly-detection-w-msk/index.html">', html_object_3)

			html_object_5 = re.sub(r'> <a href=\'../../open-search-log-analytics/\'>1. OpenSearch Log Analytics</a>', '> <a href=\'../../open-search-log-analytics/index.html\'>OpenSearch Log Analytics</a>', html_object_4)
			html_object_6 = re.sub(r'<a href=\'../../\'>OpenSearch Log Analytics Workshop</a> >', '<a href=\'../../index.html\'>OpenSearch Log Analytics Workshop</a> >', html_object_5)
			html_object_7 = re.sub(r'<a href=\'../../open-search-log-analytics/1_getting_started.html\'>1. Getting started</a> >', '<a href=\'../../open-search-log-analytics/1_getting_started.html\'>Getting started</a> >', html_object_6)

			html_object_8 = re.sub(r'> <a href=\'../../collect-log-cloud-watch/\'>2. CloudWatch Log Collection</a>', '> <a href=\'../../collect-log-cloud-watch/index.html\'>CloudWatch Log Collection</a>', html_object_7)
			html_object_9 = re.sub(r'> <a href=\'../../collect-log-cloud-watch/1_getting_started.html\'>1. Getting started</a>', '> <a href=\'../../collect-log-cloud-watch/1_getting_started.html\'> Getting started</a>', html_object_8)

			html_object.write(html_object_9)
			html_object.truncate()

			print("Finished file " + html_file)	 

print("---------------------------------")
print("Finished - html clean Up --------")
print("---------------------------------")