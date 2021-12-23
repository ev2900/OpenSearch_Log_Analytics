---
title: "5. Clean Up"
menuTitle: "Clean Up"
chapter: false
weight: 10
---

### Delete OpenSearch

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on the **workshop-domain** OpenSearch domain you created earlier

![select_domain](/images/open-search-log-analytics/IAM_1.PNG)

3. Click on **Delete**

![select_domain](/images/open-search-log-analytics/delete_3.PNG)

4. Follow the instructions in the prompt to complete the delete

### Delete Glue Jobs

1. Go to the [Glue Console](https://console.aws.amazon.com/glue/home)
2. On the left hand menu click on **Jobs**

![GLUE_1](/images/collect-log-cloud-watch/GLUE_1.PNG)

3. Click on the box next to a Glue Job
4. Click on the **Actions** drop down
5. From the drop down click on **Delete**

![CLEAN_1](/images/collect-log-cloud-watch/CLEAN_1.PNG)

6. In the pop up window click on the **Delete** button
7. Repeat this process until you have deleted both of the Glue Jobs (```glue_job_success``` and ```glue_job_error```) the we created earlier

### Delete Cloud Watch Log Groups

1. Navigate to the [CloudWatch Console](https://console.aws.amazon.com/cloudwatch/)
2. On the left hand menu click on **Log groups**

![GLUE_1](/images/collect-log-cloud-watch/CW_1.PNG)

3. On the log groups page click on the **check box to select all of the log groups**
4. Click on the **Actions**drop down
5. Click on **Delete log group(s)**

### Delete Lambda Functions

1. Navigate to the [Lambda Function Console](https://console.aws.amazon.com/lambda/home?region=us-east-1#/discover)
2. Click on **Functions** on the left hand menu

![CLEAN_2](/images/collect-log-cloud-watch/CLEAN_2.PNG)

3. Click on the **check box next to the function**
4. Click on the **actions drop down**
5. Select **delete**

![CLEAN_3](/images/collect-log-cloud-watch/CLEAN_3.PNG)

6. Click on the **delete** button in the pop up window
7. Repeat the process until you have deleted the Lambda Functions that you want to delete

You have completed deleting the resources used in this workshop