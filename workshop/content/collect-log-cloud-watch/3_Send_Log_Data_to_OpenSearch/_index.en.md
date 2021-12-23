---
title: "3. Send Log Data to OpenSearch"
chapter: false
disableToc: false
menuTitle: "Send Log Data to OpenSearch"
weight: 10
---

We have now create an OpenSearch domain, configured the required IAM and OpenSearch premissions and we created two Glue jobs that we can run. One Glue job that completes sucssfully and another which creates an error. 

All of the log information for the Glue jobs is collected in CloudWatch. Lets send the data - in realtime - from CloudWatch to OpenSearch

We can complete this in the following steps

1. Set up CloudWatch to OpenSearch Lambda Function(s)
2. Re-run the Glue Jobs to Create additonal CloudWatch Logs

#### Set up CloudWatch to OpenSearch Lambda Function(s)

1. Navigate to the [CloudWatch Console](https://console.aws.amazon.com/cloudwatch/)
2. On the left hand menu click on **Log groups**

![GLUE_1](/images/collect-log-cloud-watch/CW_1.PNG)

On the log groups page of CloudWatch you should see a few log groups which begin with /aws-glue/

![CW_1](/images/collect-log-cloud-watch/CW_2.PNG)

3. Click on the log group **aws-glue/jobs/error**
4. Click on the **Subscription filters** tab
5. Click on the **Create** drop down
6. Click on the **Create Amazon OpenSearch Service subscription filter**

![CW_3](/images/collect-log-cloud-watch/CW_3.PNG)

7. On the Create Amazon OpenSearch Service subscription filter page, under the choose destination click on **This account**
8. From the drop down select the **workshop-domain**

![CW_4](/images/collect-log-cloud-watch/CW_4.PNG)

9. Under the Lambda Function section select the IAM role ```workshop-role``` that we created earlier

![CW_5](/images/collect-log-cloud-watch/CW_5.PNG)

10. Under the configure log format and filters select **JSON**
11. For the subscription filter pattern enter ```" "```
12. For the subscription filter name ```all log```

![CW_6](/images/collect-log-cloud-watch/CW_6.PNG)

13. Click on Start streaming

![CW_7](/images/collect-log-cloud-watch/CW_7.PNG)

The steps you just completed created a lambda function that will send CloudWatch logs to OpenSearch in realtime. 

Now that we have compelted this process for the ```	/aws-glue/jobs/error``` log group Navigate back to the [CloudWatch Console](https://console.aws.amazon.com/cloudwatch/) and repeat steps 1 - 13 for log groups ```	/aws-glue/jobs/logs-v2``` and ```/aws-glue/jobs/output```

#### Re-run the Glue Jobs to Create additonal CloudWatch Logs

1. Go to the [Glue Console](https://console.aws.amazon.com/glue/home)
2. On the left hand menu click on **Jobs**

![GLUE_1](/images/collect-log-cloud-watch/GLUE_1.PNG)

3. Click on the check box next to the ```glue_job_success``` job
4. Click on the **Action** drop down
5. Click on the **Run job** button

![GLUE_8](/images/collect-log-cloud-watch/GLUE_8.PNG)

Repeat step 3 - 4 for of the jobs you created earlier ie. ```glue_job_success``` and ```glue_job_error```. Run each job a few times. The goal is to generate some CloudWatch logs that will be sent to OpenSearch.

You can view the job run history for a job by click on the check box next to job name and viewing the history tab

![GLUE_9](/images/collect-log-cloud-watch/GLUE_9.PNG)

Ensure that you have at least 3 runs completed for each job. The job status for the ```glue_job_success``` should be Succeeded and the job status for the ```glue_job_error``` should be Failed

When you have at least 3 completed job runs for each job begin the next step [Search Logs]({{<relref "../4_Search_Logs/">}})