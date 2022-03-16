---
title: "5. Clean Up"
menuTitle: "Clean Up"
chapter: false
weight: 10
---

### Delete Cloud 9

If you used CloudFormation to deploy your resources you can navigate to the [CloudFormation console](https://us-east-1.console.aws.amazon.com/cloudformation/home?) select the stack named open-search-deployment and select delete. 

If you did not use the CloudFormation to deploy your resources follow the steps below to manually delete each resource.

![delete_1](/images/open-search-log-analytics/cf_delete.png)

If you did not use CloudFormation to deploy your resources you can manually delete the resources following the steps below

1. Go to the [Cloud9 Console](https://console.aws.amazon.com/cloud9/home)

![delete_1](/images/open-search-log-analytics/delete_1.PNG)

2. Select your Cloud9 environment
3. Click on **Delete**
4. Follow the instructions in the prompt to complete the delete

### Delete Kinesis Data Firehose

1. Go to the [Kinesis Firehose Console](https://console.aws.amazon.com/firehose/home)
2. Click on the selector next to the Kinesis Data Firehose we created earlier

![delete_1](/images/open-search-log-analytics/delete_2.PNG)

3. Click on **Delete**
4. Follow the instructions in the prompt to complete the delete

### Delete OpenSearch

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on the **workshop-domain** OpenSearch domain you created earlier

![select_domain](/images/open-search-log-analytics/IAM_1.PNG)

3. Click on **Delete**

![select_domain](/images/open-search-log-analytics/delete_3.PNG)

4. Follow the instructions in the prompt to complete the delete

You have completed deleting the resources used in this workshop