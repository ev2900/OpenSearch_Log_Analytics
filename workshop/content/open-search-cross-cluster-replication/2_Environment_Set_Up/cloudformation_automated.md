---
title: "CloudFormation"
weight: 10
---

#### Step 1 - Deploy CloudFormation Template

1. Right click the **Launch Stack** button below and open the link in a new tab. 

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=os-cross-cluster-replication&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/OpenSearch_cross_cluster_replication_demo.yaml)

2. Navigate to the new tab you just opened. You should see a screen similar to the one below
![cf_1](/images/open-search-cross-cluster-replication/cf_1.png)

3. Continue to click on the **Next** buttons until you arrive at the final review screen. Scroll to the bottom of this page
4. Click on **Create stack**

![cf_2](/images/open-search-cross-cluster-replication/cf_2.png)

This will begin the process of deploy multiple domains for Amazon OpenSearch service and a Cloud9 environment. You will automatically be redirected to the following screen

![cf_3](/images/open-search-cross-cluster-replication/cf_3.png)

The deployment will take 5 - 10 minutes to complete. You can click on the refresh button and view the status of the deployment. The initial status will be ```CREATE_IN_PROGRESS``` when the status is ```CREATE_COMPLETE``` proceed to step 2 below.

Be sure to check the Outputs tab of the os-cross-cluster-replication stack for environment info.
![cf_4](/images/open-search-cross-cluster-replication/cf_4.png)

Proceed to [Setup a Cross-Cluster Connection]({{<relref "../3_Setup_Connection/">}})
