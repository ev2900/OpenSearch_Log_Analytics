---
title: "Create OpenSearch Index"
weight: 10
---

We will need to create a sample index in OpenSearch so we can store and query data for an alert. To do this, we will run a Python application in our Cloud9 environment to create the index.

#### Run a Python Application from Cloud9

Navigate to the [Cloud9 Console](https://console.aws.amazon.com/cloud9/home) and click on **Open IDE** under the already created ```workshop-cloud9``` environment. The [OpenSearch_API_Examples](https://github.com/ev2900/OpenSearch_API_Examples) repository will be automatically pulled down to your environment. Do the following within the Cloud9 console.

1. Open the file **OpenSearch_API_Examples/Alerting/1_create_index.py**
2. Update the **os_url** variable to your OpenSearch instance. This is the **OSDomainURL** Output from the CloudFormation stack.
3. Goto File->Save to save the changes to **1_create_index.py**

In the terminal window, run the following commands:

4. ```pip install requests```
5. ```python OpenSearch_API_Examples/Alerting/1_create_index.py```

The image below highlights the commands. 

![cloud9_create](/images/open-search-alerting/cloud9_1.png)

This command creates and index for use in this workshop. If you would like to verify it was created, you can browse to your OpenSearch dashboard.

1. Open the OpenSearch Dashboard using the URL and credentials provided in the CloudFormation outputs: **DashboardURL, UserName, Password**
2. Click on the menu icon and goto **OpenSearch Plugins->Index Management**
![os_1](/images/open-search-alerting/os_1.png)
3. Open **Indicies->Indicies** and verify **alert-1** index exists. You will find the health in yellow status, but this is expected.
![os_2](/images/open-search-alerting/os_2.png)

When you are ready move on to the next step [Create Alert]({{<relref "../3_Create_Alert/">}})
