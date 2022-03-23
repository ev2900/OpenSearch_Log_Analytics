---
title: "3. Send Log Data to Kinesis Firehose"
chapter: false
disableToc: false
menuTitle: "Send Log Data to Kinesis Firehose"
weight: 10
---

We need to send sample log data to Kinesis Data Firehose which in turn will send the data to OpenSearch. 

We will run a python application that will send sample Spark log data to OpenSearch. We will run the sample Python application in a Cloud9 environment.

{{% notice warning %}}
If in the previous section [Environment Set Up]({{<relref "../2_Environment_Set_Up/">}}) you chose the [CloudFormation (Automated)]({{<relref "../2_Environment_Set_Up/cloudformation_automated">}}) deployment option your Cloud9 environment is already created. Navigate to the [Cloud9 Console](https://console.aws.amazon.com/cloud9/home) and click on **Open IDE** under the already created ```workshop-cloud9``` environment. Then skip the *Create a Cloud9 environment* section below and start at the *Run a Python Application from Cloud* section. **If you did not use the CloudFormation template** in the [Environment Set Up]({{<relref "../2_Environment_Set_Up/">}}) and instead used the [Console Deploy (Manual)]({{<relref "../2_Environment_Set_Up/console_manual">}}) complete the *Create a Cloud9 environment* section below before starting on the *Run a Python Application from Cloud* section.
{{% /notice %}}

#### Create a Cloud9 environment
1. Go to the [Cloud9 Console](https://console.aws.amazon.com/cloud9/home)
2. Click on **Create environment**

![cloud9_create](/images/open-search-log-analytics/cloud9_1.PNG)

3. Under the name environment section enter ```workshop-cloud9``` for the name
4. Click on **Next step**
5. Leave all of the settings at the default selections
6. Click on **Next step**
7. Click on **Create environment**

After the Cloud9 environment is created your browser will automatically be redirected to the Cloud9 console

![cloud9_create](/images/open-search-log-analytics/cloud9_2.PNG)

#### Run a Python Application from Cloud9

Within the Cloud9 console running the following commands in the console section of the Cloud9 environment

1. ```wget https://sharkech-public.s3.amazonaws.com/opensearch-log-analytics/data-producer/Log_Producer_Desktop.py```

The image below highlights were to run the commands. Run all of the commands in order

![cloud9_create](/images/open-search-log-analytics/cloud9_4.PNG)

2. ```wget https://sharkech-public.s3.amazonaws.com/opensearch-log-analytics/data-producer/sample_logs/spark.txt```
3. ```pip install boto3```
4. ```python Log_Producer_Desktop.py```

These commands download the sample log data. They also download and configure the python script that will send the sample log data to Kinesis Data Firehose. 

Upon running the last command you should be messages appearing in the Cloud9 console indicating the logs are being sent.

![cloud9_create](/images/open-search-log-analytics/cloud9_3.PNG)

Leave this browser window open. This way the python application continues to run and send data.

When you are ready move on to the next step [Visualize and Analyze]({{<relref "../4_Visualize_Analyze/">}})