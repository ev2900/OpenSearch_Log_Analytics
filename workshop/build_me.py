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

l1 = ['./public/index.html']
l2 = ['./public/open-search-log-analytics/index.html', './public/open-search-log-analytics/1_getting_started.html', './public/open-search-log-analytics/2_enviorment_set_up.html', './public/open-search-log-analytics/3_send_log_data_to_kinesis_fire_hose.html', './public/open-search-log-analytics/4_visualize_analyze_in_kibana.html', './public/open-search-log-analytics/5_clean_up.html']
l3 = ['./public/open-search-log-analytics/1_getting_started/aws_event.html', './public/open-search-log-analytics/1_getting_started/self_paced.html']

for html_file in l1:

	with open(html_file, "r+") as html_object:

		html = html_object.read()
		html_object.seek(0)
		
		c1 = re.sub(r'<a href="./open-search-log-analytics/">', '<a href="./open-search-log-analytics/index.html">', html)
		c2 = re.sub(r'<a class="nav nav-next" href="./open-search-log-analytics/"', '<a class="nav nav-next" href="./open-search-log-analytics/index.html"', c1)

		html_object.write(c2)
		html_object.truncate()

		print("Finished file " + html_file)

for html_file in l2:

	with open(html_file, "r+") as html_object:

		html = html_object.read()
		html_object.seek(0)
		html_object.write(re.sub(r'<a href="*..*/open-search-log-analytics/">', '<a href="../open-search-log-analytics/index.html">', html))
		html_object.truncate()

		print("Finished file " + html_file)

for html_file in l3:
		
		with open(html_file, "r+") as html_object:

			html = html_object.read()
			html_object.seek(0)
			html_object.write(re.sub(r'<a href="*..*/open-search-log-analytics/">', '<a href="../../open-search-log-analytics/index.html">', html))
			html_object.truncate()

			print("Finished file " + html_file)	 

print("---------------------------------")
print("Finished - html clean up --------")
print("---------------------------------")

print ("")

print("---------------------------------")
print("S3 Upload - start ---------------")
print("---------------------------------")

os.system('aws s3 cp ./public/ s3://sharkech-public-dev/dev-opensearch-log-analytics/ --profile ev2900 --recursive')

print("---------------------------------")
print("S3 Upload - finished ------------")
print("---------------------------------")

print ("")

print("---------------------------------")
print("S3 Set public ACL - start -------")
print("---------------------------------")

print("")

print("GO TO THE AWS CONSOLE AND SET THE ACLs to PUBLIC")