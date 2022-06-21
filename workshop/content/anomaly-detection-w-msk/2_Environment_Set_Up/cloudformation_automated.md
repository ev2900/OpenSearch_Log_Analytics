---
title: "CloudFormation (Automated)"
weight: 10
---

#### Step 1 - Deploy CloudFormation Template

1. Right click the **Launch CloudFormation Stack** button below and open the link in a new tab. 

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=msk-lambda-opensearch&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/msk_lambda_opensearch.yaml)

2. Navigate to the new tab you just opened. You should see a screen similar to the one below

![enviorment_set_up_cloudformation_automation_1](/images/anomaly-detection-w-msk/enviorment_set_up_cloudformation_automation_1.png)

3. Click on the **Next** button
4. Continue to click on the **Next** buttons until you arrive at the final review screen. Scroll to the bottom of this page
5. At the bottom of the page click on **I acknowledge that AWS CloudFormation might create IAM resources with custom names**
6. Click on **Create stack**

![enviorment_set_up_cloudformation_automation_2](/images/open-search-fluentd/enviorment_set_up_cloudformation_automation_2.png)

This will begin the process of deploying the required resources. You will automatically be redirected to the following screen

![enviorment_set_up_cloudformation_automation_3](/images/anomaly-detection-w-msk/enviorment_set_up_cloudformation_automation_2.png)

The deployment will take 5 - 10 minutes to complete. You can click on the refresh button and view the status of the deployment. The initial status will be ```CREATE_IN_PROGRESS``` when the status is ```CREATE_COMPLETE```. Click on the **Outputs** section of the CloudFormation stack and copy the values of the output. The output values will be used in subsequent parts of this workshop.

![enviorment_set_up_cloudformation_automation_4](/images/anomaly-detection-w-msk/enviorment_set_up_cloudformation_automation_4.png)

#### Step 2 - Update MSK Network Security Group

Cloud9 and MSK from a network point of view, must be able to communicate with each other. To achieve this you must update the network security group for MSK to accept incoming traffic from the Cloud9 security group.

1. Navigate to the [Security Group page in the AWS console](https://us-east-1.console.aws.amazon.com/vpc/home?region=us-east-1#securityGroups:)
2. Select the security group with the name **msk security group**
3. Click on the **Inbound rules** tab
4. Click on **Edit inbound rules**

![enviorment_set_up_nsg_1](/images/anomaly-detection-w-msk/enviorment_set_up_nsg_1.png)

You will be redirected to the edit inbound rules page

5. Click on **Add rule**
6. Select **All traffic** from the type drop down
7. Select the security group that starts with **aws-cloud9-msk-works** as the source
8. Click on **Save rules**

![enviorment_set_up_nsg_1](/images/anomaly-detection-w-msk/enviorment_set_up_nsg_2.png)

The msk security group will now accept inbound network traffic originating from the cloud-9 security group

#### Step 3 - Create Kafka Topic

We need to create a topic in Kafka that we can later send log data to.

1. Navigate to the [MSK page in the AWS console](https://us-east-1.console.aws.amazon.com/msk/home)
2. Select the **msk-workshop-cluster**

![enviorment_set_up_msk_1](/images/anomaly-detection-w-msk/enviorment_set_up_msk_1.png)

3. Click on **View client information**

![enviorment_set_up_msk_2](/images/anomaly-detection-w-msk/enviorment_set_up_msk_2.png)

4. Copy the plaintext Apache ZooKeeper connection information

![enviorment_set_up_msk_3](/images/anomaly-detection-w-msk/enviorment_set_up_msk_3.png)

5. Navigate to the [Cloud9 console](https://us-east-1.console.aws.amazon.com/cloud9/home)
6. Click on **Open IDE**

![enviorment_set_up_msk_4](/images/anomaly-detection-w-msk/enviorment_set_up_msk_4.png)

7. In the Cloud9 environment navigate and open ```Kafka_OpenSearch_Anomaly_Detection/Kafka/1_create_topic.py``` 

![enviorment_set_up_msk_5](/images/anomaly-detection-w-msk/enviorment_set_up_msk_5.png)

8. Run ```yes | sudo yum install java-1.8.0``` in the Cloud9 terminal
9. Run ```wget https://archive.apache.org/dist/kafka/2.6.2/kafka_2.12-2.6.2.tgz```
10. Run ```tar -xzf kafka_2.12-2.6.2.tgz```
11. Run ```cd kafka_2.12-2.6.2```

![enviorment_set_up_msk_6](/images/anomaly-detection-w-msk/enviorment_set_up_msk_6.png)

12. Update the ```bin/kafka-topics.sh --create --zookeeper <ZookeeperConnectString> --replication-factor 1 --partitions 1 --topic ApplicationMetricTopic``` replace the ```<ZookeeperConnectString>``` with the plaintext Apache ZooKeeper connection information you copied down on Step 4

Run the updated command on the AWS console

![enviorment_set_up_msk_7](/images/anomaly-detection-w-msk/enviorment_set_up_msk_7.png)

The command will return a result *Created topic ApplicationMetricTopic*

#### Step 4 - Create OpenSearch Index

Before we can send data to OpenSearch we need to create an index. You will run a python script from Cloud9 that will create an index in the OpenSearch domain.

If you are not already in the Cloud9 console 

1. Navigate to the [Cloud9 in the AWS console](https://us-east-1.console.aws.amazon.com/cloud9/home)
2. Under the *msk-workshop-cloud9* environment click on **Open IDE**

If you are already in the Cloud9 console 

3. In the Cloud9 environment navigate and open ```Kafka_OpenSearch_Anomaly_Detection/OpenSearch/1_create_index.py``` 
4. Replace the ```<opensearch_domain_endpoint_url>``` with the value of the **OSDomainURL** key from the CloudFormation stack output
6. Run the following command on the Cloud9 terminal ```cd ~```
7. Run the following command on the Cloud9 terminal ```pip install requests```
8. Run the python script by issuing the following command in the Cloud9 terminal ```python environment/Kafka_OpenSearch_Anomaly_Detection/OpenSearch/1_create_index.py``` 

![enviorment_set_up_create_os_index_1](/images/anomaly-detection-w-msk/enviorment_set_up_create_os_index.png)

#### Step 5 - Map IAM Role to OpenSearch Role

Later in the lab when we upload data to OpenSearch the IAM role we will use needs access in OpenSearch. We can run a python script in Cloud9 map the IAM role to the OpenSearch role

If you are not already in the Cloud9 console 

1. Navigate to the [Cloud9 in the AWS console](https://us-east-1.console.aws.amazon.com/cloud9/home)
2. Under the *msk-workshop-cloud9* environment click on **Open IDE**

If you are already in the Cloud9 console 

3. In the Cloud9 environment navigate and open ```Kafka_OpenSearch_Anomaly_Detection/OpenSearch/2_map_IAM_user.py```
4. Replace the ```<os_domain_url>``` with the value of the **OSDomainURL** key from the CloudFormation stack output
5. Replace the ```<IAM_user/role_arn>``` with the value of the **IAMUserARN** key from the CloudFormation stack output
6. Run the python script by issuing the following command in the Cloud9 terminal ```python environment/Kafka_OpenSearch_Anomaly_Detection/OpenSearch/2_map_IAM_user.py```

![enviorment_set_up_map_iam_os_1](/images/anomaly-detection-w-msk/enviorment_set_up_map_iam_os_1.png)

Our AWS environment set up. When you are ready begin the next step [Configure Lambda]({{<relref "../3_Configure_Lambda/">}})