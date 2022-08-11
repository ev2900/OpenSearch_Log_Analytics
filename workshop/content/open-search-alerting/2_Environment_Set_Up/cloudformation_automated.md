---
title: "CloudFormation"
weight: 10
---

#### Step 1 - Deploy CloudFormation Template

1. Right click the **Launch Stack** button below and open the link in a new tab. 

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=os-alerting&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_demo_alerting.yaml)

2. Navigate to the new tab you just opened. You should see a screen similar to the one below
![cf_1](/images/open-search-alerting/cf_1.png)

3. Click on the **Next** button
4. Populate EmailParameter with a valid email address to send alerts.
![cf_2](/images/open-search-alerting/cf_2.png)

5. Continue to click on the **Next** buttons until you arrive at the final review screen. Scroll to the bottom of this page
6. At the bottom of the page click on **I acknowledge that AWS CloudFormation might create IAM resources with custom names**
7. Click on **Create stack**

![cf_3](/images/open-search-alerting/cf_3.png)

This will begin the process of deploy an Amazon OpenSearch service, SNS topic, and Cloud9 environment. You will automatically be redirected to the following screen

![cf_4](/images/open-search-alerting/cf_4.png)

The deployment will take 5 - 10 minutes to complete. You can click on the refresh button and view the status of the deployment. The initial status will be ```CREATE_IN_PROGRESS``` when the status is ```CREATE_COMPLETE``` proceed to step 2 below.

Be sure to check the Outputs tab of the os-alerting stack for environment info.
![cf_5](/images/open-search-alerting/cf_5.png)

#### Step 2 - Confirm SNS Subscription

You will receive an email confirming a subscription to your SNS topic. Click Confirm subscription.
![cf_6](/images/open-search-alerting/cf_6.png)

Proceed to [Create OpenSearch Index]({{<relref "./create_index/">}})