---
title: "2. Environment Set Up"
chapter: false
disableToc: false
menuTitle: "Environment Set Up"
weight: 10
---

We will need to deploy a few services and configure our AWS environment before we can get started with log analytics.

We will need to compelete the following set up steps

1. Create an OpenSearch Domain
2. Create a Kinesis Firehose
3. Configure Identity Access Management Premisions

Follow the instructions below for each step

#### Create an OpenSearch Domain

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on **Create domain** 

![cloud_shell_button](/images/open-search-log-analytics/set_up_1.PNG)

3. Enter the name ```workshop-domain``` for the OpenSearch Domain
4. Under the deployment type section, select ```Development and testing```
5. Under the network section, select ```Public access```
6. Under the fine-grained access control section select ```Create master user```
7. Enter and username and password. Copy down the user name and password. We will need these later in the workshop
8. Leave all other settings at the default selections
9. Click on **Create**

It will take approximately 5 - 10 minutes for your OpenSearch domain to be created. Upon sucssful creation you will see your OpenSearch domain status is active

![cloud_shell_button](/images/open-search-log-analytics/set_up_2.PNG)

#### Create a Kinesis Firehose

1. Go to the [Kinesis Firehose Console](https://console.aws.amazon.com/firehose/home)
2. Click on **Create delivery stream**

![create_delivery_stream](/images/open-search-log-analytics/kfh_1.PNG)

3. Under the choose source and destination section for the source, select ```Direct PUT``` for the desintation select ```Amazon OpenSearch Service```
4. Under the delivery stream name section name the stream ```
workshop-firehose```

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

#### Configure Identity Access Management (IAM) Premisions

In the first step we created an OpenSearch domain. We can send logs to the OpenSearch domin via. the Kinesis Data Firehose we just created

However before we can start to send sample log data to OpenSearch (via Kinesis Data Firehose) we need to configure premissions in IAM and in OpenSearch

##### Adjust OpenSearch Access Policy

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on the **workshop-domain** OpenSearch domain you created earlier

![select_domain](/images/open-search-log-analytics/IAM_1.PNG)

3. Click on **Security configuration**
4. Under the security configuration window click on **Edit**

![security_configuration](/images/open-search-log-analytics/IAM_2.PNG)

5. Naviage to the access policy section of the edit security configuration window
6. Adjust the JSON access policy switch the deny to an ```Allow```

![access_policy](/images/open-search-log-analytics/IAM_3.PNG)

7. Click on **Save changes** at the bottom of the page

#### Map IAM Role with OpenSeach Role

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on the **workshop-domain** OpenSearch domain you created earlier
3. Click on the OpenSearch Dashboard URL. This should open the URL in a web browser window

![open_search_dashboard](/images/open-search-log-analytics/IAM_4.PNG)

4. You will be prompted to log in. Using the user name and password you created during the OpenSearch deployment, log in 
5. If an additonal pop up window is present after login asking about data upload click on **Explore on my own**
6. If an additonal pop up windows is present asking you to select your tenant select **Global** and click on **Confirm**

You should now see a window that looks like this

![select_domain](/images/open-search-log-analytics/os_1.PNG)

7. 