---
title: "2. Environment Set Up"
chapter: false
disableToc: false
menuTitle: "Environment Set Up"
weight: 10
---

We will need to deploy a few services and configure our AWS environment before we can get started.

We will need to complete the following set up steps

1. Create an OpenSearch Domain
2. Create a Kinesis Firehose
3. Configure Identity Access Management Permissions

In order to completed Step 1 (create an OpenSearch domain) and Step 2 (create a Kinesis Firehose). You can either follow the steps below to deploy the resources manually via. the AWS console. 

Or you can click the button below to execute a CloudFormation template that will complete the deployment of the OpenSearch domain and Kinesis Firehose. 

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=open-search-deployment&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_demo.yaml)

If you use the CloudFormation deployment method wait for the CloudFormation stack to finish deploying (5 - 10 minutes) and then move on the Step 3 (configure identity access management). The instructions for step 3 are towards the bottom of this web page.

If you do not use the CloudFormation deployment method and want to complete the deployment of your OpenSearch domain and Kinesis Firehose manually via. the AWS console. Follow the instructions below.

#### Step 1 - Create an OpenSearch Domain

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on **Create domain** 

![cloud_shell_button](/images/open-search-log-analytics/set_up_1.PNG)

3. Enter the name ```workshop-domain``` for the OpenSearch Domain
4. Under the deployment type section, select ```Development and testing```
5. Under the network section, select ```Public access```
6. Under the fine-grained access control section select ```Create master user```
7. For the username enter ```OSMasterUser```
8. For the password enter  ```AwS#OpenSearch1```
9. Under the access policy section, select ```Only use fine-grain access control``` 
10. Leave all other settings at the default selections
11. Click on **Create**

It will take approximately 5 - 10 minutes for your OpenSearch domain to be created. Upon successful creation you will see your OpenSearch domain status is active

![cloud_shell_button](/images/open-search-log-analytics/set_up_2.PNG)
Do not proceed to the next step until you confirm that your domain status is active

#### Step 2 - Create a Kinesis Firehose

1. Go to the [Kinesis Firehose Console](https://console.aws.amazon.com/firehose/home)
2. Click on **Create delivery stream**

![create_delivery_stream](/images/open-search-log-analytics/kfh_1.PNG)

3. Under the choose source and destination section for the source, select ```Direct PUT``` for the destination select ```Amazon OpenSearch Service```
4. Under the delivery stream name section name the stream ```workshop-firehose```

![select_source_destination](/images/open-search-log-analytics/kfh_2.PNG)

5. Under the destination settings for the OpenSearch service domain, click on **Browse** and select the OpenSearch domain **workshop-domain** this is the OpenSearch domain we created in the previous step
6. Name the index ```workshop-log```
7. Select  ```Every hour``` for the Index rotation. This will produce a next index every hour

![index_rotation](/images/open-search-log-analytics/kfh_3.PNG)

8. Expand the **Buffer hints** section
9. Adjust the buffer interval to ``60`` seconds. This will write data from Kinesis Firehose to OpenSearch every 60 seconds

![buffer_hints](/images/open-search-log-analytics/kfh_4.PNG)
 
10. Under the backup settings under the S3 backup bucket click on **Create**. This will (in a new browser window) open the create S3 bucket web page

![back_up_create_s3](/images/open-search-log-analytics/kfh_5.PNG)

11. On the create bucket page provide a bucket name. You may name the bucket any valid name
12. Click on **Create bucket** at the bottom of the page. Leaving all of the S3 settings the the default selections
13. Return the browser window that we were using to configure our Kinesis Firehose and under the backup setting section for the S3 backup bucket, click on **Browse**
14. Select the bucket you just created. If you do not see the bucket listed click on the small refresh button in the top right corner of the window that pops us when you click on the browse button

![back_up_select_s3](/images/open-search-log-analytics/kfh_6.PNG)

15. At the bottom of the page click on **Create delivery stream** leave all other settings at the default selections

#### Step 3 - Configure Identity Access Management (IAM) Permissions

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