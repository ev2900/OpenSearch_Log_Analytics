---
title: "Create OpenSearch Index"
weight: 10
---

You will need to create a sample index in OpenSearch so you can store and query data for an alert. To do this, you will run a Python application in our Cloud9 environment to create the index.

#### Step 1 - Create Index

1. Navigate to the [Cloud9 Console](https://console.aws.amazon.com/cloud9/home) 
2. Click on **Open IDE** under the already created workshop-cloud9 environment. 

![cloud9_2](/images/open-search-alerting/cloud9_2.png)

The [OpenSearch_API_Examples](https://github.com/ev2900/OpenSearch_API_Examples) repository will be automatically pulled down to your environment. Do the following within the Cloud9 console.

1. Open the file **OpenSearch_API_Examples/Alerting/1_create_index.py**
2. Update the **os_url** variable to your OpenSearch instance. This is the value of the **OSDomainURL** key from the CloudFormation stack output.
3. Go to **File** -> **Save** to save the changes to 1_create_index.py

In the terminal window, run the following commands:

4. ```pip install requests```
5. ```python OpenSearch_API_Examples/Alerting/1_create_index.py```

#### Step 2 - Check that the Index was Created via. OpenSearch Dashboard
The image below highlights the commands. 

![cloud9_create](/images/open-search-alerting/cloud9_1.png)

This command creates and index for use in this workshop

1. Open the OpenSearch Dashboard using the URL provided in the value for the key DashboardURL in the CloudFormation outputs

![cloud9_3](/images/open-search-alerting/cloud9_3.png)

Once you open the dashboard URL you will be prompted to login 

2. Enter ```OSMasterUser``` as the username
3. Enter ```AwS#OpenSearch1``` as the password
4. Click on **Log In**
5. If an additional pop up window is present after login asking about data upload click on **Explore on my own**
6. If an additional pop up windows is present asking you to select your tenant select **Global** and click on **Confirm**

Once you have logged in to the OpenSearch dashboard

7. Click on the top left hand menu on the OpenSearch dashboard
8. Click on **Index Management** under the OpenSearch Plugins section

![cloud9_4](/images/open-search-alerting/cloud9_4.png)

9. Click on **Indices**

You should be able to see an index alert-1 is present

![os_2](/images/open-search-alerting/os_2.png)

When you are ready move on to the next step [Create Alert]({{<relref "../3_Create_Alert/">}})
