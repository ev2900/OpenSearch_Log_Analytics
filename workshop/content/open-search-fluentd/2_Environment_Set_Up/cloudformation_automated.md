---
title: "CloudFormation (Automated)"
weight: 10
---

#### Step 1 - Deploy CloudFormation Template

1. Right click the **Launch CloudFormation Stack** button below and open the link in a new tab. 

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=fluentd-demo-opensearch&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/fluentd_cloud9_opensearch.yml)

2. Navigate to the new tab you just opened. You should see a screen similar to the one below

![enviorment_set_up_cloudformation_automation_1](/images/open-search-fluentd/enviorment_set_up_cloudformation_automation_1.png)

3. Click on the **Next** button
4. Continue to click on the **Next** buttons until you arrive at the final review screen. Scroll to the bottom of this page
5. At the bottom of the page click on **I acknowledge that AWS CloudFormation might create IAM resources with custom names**
6. Click on **Create stack**

![enviorment_set_up_cloudformation_automation_2](/images/open-search-fluentd/enviorment_set_up_cloudformation_automation_2.png)

This will begin the process of deploy an Amazon OpenSearch service, Kinesis Data Firehose and Cloud9 environment. You will automatically be redirected to the following screen

![enviorment_set_up_cloudformation_automation_3](/images/open-search-fluentd/enviorment_set_up_cloudformation_automation_3.png)

The deployment will take 5 - 10 minutes to complete. You can click on the refresh button and view the status of the deployment. The initial status will be ```CREATE_IN_PROGRESS``` when the status is ```CREATE_COMPLETE```. Click on the **Outputs** section of the CloudFormation stack and copy the values of the output. The output values will be used in subsequent parts of this workshop.

![enviorment_set_up_cloudformation_automation_4](/images/open-search-fluentd/enviorment_set_up_cloudformation_automation_4.png)


#### Step 2 - Map IAM Role with OpenSeach Role

You now have an OpenSearch domain and Cloud9 environment created. In order to send logs to OpenSearch via Fluentd you need to grant the IAM role that Fluentd will use permissions in OpenSearch.

The CloudFormation stack already created an IAM role for us. you need to map the IAM role to an OpenSearch role. To map the role you can run a python script in Cloud9 that will use the OpenSearch APIs to map the IAM role the all_access role in OpenSearch.

{{% notice warning %}}
For the purposes of this lab you are mapping our IAM role to the all_access role in OpenSearch. In a production environment more limited permissions should be granted to the IAM role Fluentd will use 
{{% /notice %}}


To map the IAM role to the OpenSearch role follow the steps below

1. Go to the [Cloud9 Console](https://us-east-1.console.aws.amazon.com/cloud9/home?region=us-east-1)
2. Click on **Open IDE**


![enviorment_set_up_cloudformation_automation_5](/images/open-search-fluentd/enviorment_set_up_cloudformation_automation_5.png)


Once you have opened the Cloud9 IDE navigate the folder structure on the left hand menu to and open the Flentd_Examples folder. Then the Cloud9_Apache_Logs_OpenSearch sub-folder. In this folder open the map_IAM_user.py file.

In the map_IAM_user.py file

3. Replace the value of the os_url variable with the value of the OSDomainURL key from the CloudFormation stack outputs
4. Replace the value of the iam_arn variable with the value of the IAMUserARN key from the CloudFormation stack outputs
5. Save the python file

![enviorment_set_up_cloudformation_automation_6](/images/open-search-fluentd/enviorment_set_up_cloudformation_automation_6.png)

You can now run the map_IAM_user.py script by executing the following commands in the Cloud9 terminal

5. ```pip install requests```
6. ```python Fluentd_Examples/Cloud9_Apache_Logs_OpenSearch/map_IAM_user.py```

![enviorment_set_up_cloudformation_automation_7](/images/open-search-fluentd/enviorment_set_up_cloudformation_automation_7.png)

Our AWS environment set up. When you are ready begin the next step [Configure Fluentd]({{<relref "../3_Configure_Fluentd/">}})