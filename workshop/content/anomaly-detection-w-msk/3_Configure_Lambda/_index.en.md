---
title: "3. Configure Lambda"
chapter: false
disableToc: false
menuTitle: "Configure Lambda"
weight: 10
---

You need to configure a Lambda function to read data from MSK and write it to OpenSearch. To configure the Lambda function

1. Navigate to the [Lambda console](https://us-east-1.console.aws.amazon.com/lambda/home)
2. Click on **msk-os-lambda**

![lambda_1](/images/anomaly-detection-w-msk/lambda_1.png)

3. Click on **Add trigger**

![lambda_2](/images/anomaly-detection-w-msk/lambda_2.png)

4. Select **MSK** from the trigger drop down
5. Select **msk-workshop-cluster** from the MSK cluster drop down
6. Enter ```500``` for the batch size
7. Enter ```30``` for the batch window
8. Enter ```ApplicationMetricTopic``` for the topic name
9. Select **Latest** from the starting position drop down
10. Click on **Add**

![lambda_3](/images/anomaly-detection-w-msk/lambda_3.png)

You will automatically be redirected to a page that looks like the one below. Take note of the status of trigger. Remain on this page refreshing as necessary until the trigger status is **Enabled**

![lambda_4](/images/anomaly-detection-w-msk/lambda_4.png)

11. Click on the **Code** tab
12. Update the **os_url** variable with the value of the **OSDomainURL** key from the CloudFormation stack output

![lambda_5](/images/anomaly-detection-w-msk/lambda_5.png)

13. Click on the **Deploy** button

![lambda_6](/images/anomaly-detection-w-msk/lambda_6.png)

Our Lambda function is now set up. When you are ready begin the next step [Send Logs]({{<relref "../4_Send_Logs/">}})