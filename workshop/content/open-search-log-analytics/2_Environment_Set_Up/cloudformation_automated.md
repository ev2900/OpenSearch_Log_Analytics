---
title: "CloudFormation (Automated)"
weight: 10
---

#### Step 1 - Deploy CloudFormation Template

1. Right click the **Launch CloudFormation Stack** button below and open the link in a new tab. 

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=open-search-deployment&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_demo.yaml)

2. Navigate to the new tab you just opened. You should see a screen similar to the one below

![cf_1](/images/open-search-log-analytics/cf_1.PNG)

3. Click on the **Next** button
4. Continue to click on the **Next** buttons until you arrive at the final review screen. Scroll to the bottom of this page
5. At the bottom of the page click on **I acknowledge that AWS CloudFormation might create IAM resources with custom names**
6. Click on **Create stack**

![cf_2](/images/open-search-log-analytics/cf_2.PNG)

This will begin the process of deploy an Amazon OpenSearch service, Kinesis Data Firehose and Cloud9 environment. You will automatically be redirected to the following screen

![cf_3](/images/open-search-log-analytics/cf_3.PNG)

The deployment will take 5 - 10 minutes to complete. You can click on the refresh button and view the status of the deployment. The initial status will be ```CREATE_IN_PROGRESS``` when the status is ```CREATE_COMPLETE``` proceed to step 2 below.

#### Step 2 - Configure Identity Access Management (IAM) Permissions

We now have an OpenSearch domain and Kinesis Firehose created. In order to send logs to OpenSearch via Kinesis Data Firehose we need to grant the IAM role that firehose uses permissions in OpenSearch.

##### Map IAM Role with OpenSeach Role

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on the **workshop-domain** OpenSearch domain you created earlier
3. Click on the OpenSearch Dashboard URL. This should open the URL in a web browser window

![open_search_dashboard](/images/open-search-log-analytics/IAM_4.PNG)

4. You will be prompted to log in. Using the user name ```OSMasterUser``` and password ```AwS#OpenSearch1```  log in 
5. If an additional pop up window is present after login asking about data upload click on **Explore on my own**
6. If an additional pop up windows is present asking you to select your tenant select **Global** and click on **Confirm**

You should now see a window that looks like this

![select_domain](/images/open-search-log-analytics/os_1.PNG)

7. Click on and expand the hamburger menu on the side bar of the OpenSearch home page
8. Under the OpenSearch Plugins section click on **Security**

![select_security](/images/open-search-log-analytics/os_2.PNG)

9. On the security page click on **Roles** from the left hand menu

![select_roles](/images/open-search-log-analytics/os_3.PNG)

10. On the roles page search for and click on ```all_access``` 

![search_all_access](/images/open-search-log-analytics/os_4.PNG)

11. On the all_access role page click on **Mapped users**
12. Under the mapped users page click on **Manage mapping**

![mapped_users](/images/open-search-log-analytics/os_5.PNG)

On the manage mapping page we need to map the IAM role the is used by Kinesis Data Firehose to the all_access OpenSearch role. This will give Kinesis Firehose the permissions it need to create, update indexes and write data. 

For the purposes of this lab we will give Kinesis Firehose all_access in OpenSearch. 

We need to find the ARN of the IAM role Kinesis Firehose is using. Keeping the **Manage mapping page open in your browser**, navigate to a new tab and 

13. Go to the [Kinesis Firehose Console](https://console.aws.amazon.com/firehose/home)
14. Click on the **workshop-firehose** listed. This is the Kinesis Data Fire hose we created earlier
15. Click on the **Configuration** section

![IAM_role](/images/open-search-log-analytics/os_6.PNG)

16. On the configuration page scroll down to the permissions section
17. Click on the IAM role

![IAM_role](/images/open-search-log-analytics/os_7.PNG)

18. This will open a new window in your web browser. Copy down the ARN of the IAM role

![IAM_role](/images/open-search-log-analytics/os_8.PNG)

19. Navigate back to the OpenSearch map user tab
20. Enter the ARN we copied in step 18 and paste it in the backend roles section of OpenSearch console page
21. Click on **Map**

![IAM_role](/images/open-search-log-analytics/os_9.PNG)

Our AWS environment set up. When you are ready begin the next step [Send Log Data to Kinesis Fire Hose]({{<relref "../3_Send_Log_Data_to_Kinesis_Fire_Hose/">}})