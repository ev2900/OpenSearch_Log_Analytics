---
title: "3. Send Log Data to Kinesis Fire Hose"
chapter: false
disableToc: false
menuTitle: "Send Log Data to Kinesis Fire Hose"
weight: 10
---

We need to send sample log data to Kinesis Data Firehose which in turn will send the data to OpenSearch. 

We will run a python application that will send a few different types of log data to OpenSearch. We will run the sample Python application in a Cloud9 

**Create a Cloud9 Enviorment**
1. Go to the [Cloud9 Console](https://console.aws.amazon.com/cloud9/home)
2. Click on **Create enviorment**

![cloud9_create](/images/open-search-log-analytics/cloud9_1.PNG)

3. Under the name enviorment section enter ```log_producer``` for the name
4. Click on **Next step**
5. Leave all of the settings at the default selections
6. Click on **Next step**
7. Click on **Create enviorment**

After the Cloud9 envriorment is created your broswer will automaticlly be redirected to the Cloud9 console

![cloud9_create](/images/open-search-log-analytics/cloud9_2.PNG)

**Run a Python Application from Cloud9**

With in the Cloud9 console running the following commands in the console section of the Cloud9 enviorment

1. ```wget https://sharkech-public.s3.amazonaws.com/opensearch-log-analytics/data-producer/Log_Producer_Desktop.py```

The image below highlights were to run the commands. Run all of the commands in order

![cloud9_create](/images/open-search-log-analytics/cloud9_4.PNG)

2. ```mkdir sample_logs```
3. ```cd sample_logs```
4. ```wget https://sharkech-public.s3.amazonaws.com/opensearch-log-analytics/data-producer/sample_logs/hadoop.txt```
5. ```wget https://sharkech-public.s3.amazonaws.com/opensearch-log-analytics/data-producer/sample_logs/hdfs.txt```
6. ```wget https://sharkech-public.s3.amazonaws.com/opensearch-log-analytics/data-producer/sample_logs/spark.txt```
7. ```wget https://sharkech-public.s3.amazonaws.com/opensearch-log-analytics/data-producer/sample_logs/zoo_keeper.txt```
8. ```cd ..```
9. ```pip install boto3```
10. ```python Log_Producer_Desktop.py```

These commands download the sample log data. They also download and configure the python script that will send the sample log data to Kinesis Data Firehose. 

Upon running the last command you should be messages appearing in the Cloud9 console indicating the logs are being sent.

![cloud9_create](/images/open-search-log-analytics/cloud9_3.PNG)

Leave this broswer window open. This way the python application continues to run and send data.

When you are ready move on to the next step [Send Log Data to Kinesis Fire Hose]({{<relref "../4_Visualize_Analyze_in_Kibana/">}})