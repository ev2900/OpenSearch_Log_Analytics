---
title: "3. Create Alert"
chapter: false
disableToc: false
menuTitle: "Create Alert"
weight: 10
---

Now you will configure an OpenSearch Alert using the index you created in the last step. First you need to configure the SNS Topic created from the CloudFormation script as an OpenSearch Alert Destination. This will allow OpenSearch to use the SNS destination to send alerts.

#### Step 1 - Create a Destination

1. Click on the top left hand menu on the OpenSearch dashboard
2. Click on **Alerting** under the OpenSearch Plugins section

![os_alert_1](/images/open-search-alerting/os_alert_1.png)

3. On the alerting page click on the **Destinations**
4. Click on **Add destination**

![os_alert_2](/images/open-search-alerting/os_alert_2.png)

On the add destination page configure the destination entering the values for each field in the table below

| Field         | Value                            				|
| ------------- | -------------------------------- 				|
| Name          | ```SNS Destination```                         |
| Type          | ```Amazon SNS```                 				|
| SNS topic ARN | *TopicARN value from CloudFormation output*   |
| IAM role ARN  | *IAMRoleARN value from CloudFormation output* |

An example destination may look like 

![os_alert_3](/images/open-search-alerting/os_alert_3.png)

5. Once you finish configuring the destination click on **Create**

#### Step 2 - Set up a Monitor

Using the destination you configured, you will configure a monitor that will trigger an alert if *cpu_util* exceeds 50.

1. On the OpenSearch alerting page, click on the **Monitors** tab 
2. Click on **Create monitor**

![os_monitor_1](/images/open-search-alerting/os_monitor_1.png)

2. Fill in the **Monitor details** and **Data source** sections with the following values 

| Field                   | Value                            |
| ----------------------- | -------------------------------- |
| Monitor name            | ```High CPU Alert```             |
| Monitor type            | Per query monitor                |
| Monitor defining method | Visual editor                    |
| Frequency               | By interval                      |
| Run every               | 1 Minutes                        |
| Index                   | **alert-1**                      |
| Time field              | **eventtime**                    |


An example monitor details and data source may look like 

![os_monitor_2](/images/open-search-alerting/os_monitor_2.png)

3. Under the query section, click **+ Add metric**

![os_monitor_3](/images/open-search-alerting/os_monitor_3.png)

4. Select **max()** as the aggregation function
5. Select **cpu_util** as the field
6. Click on **Save**

![os_monitor_4](/images/open-search-alerting/os_monitor_4.png)

5. Under the triggers section, click **Add trigger**
6. Fill in the trigger sections with the following values

| Field                   | Value                            |
| ----------------------- | -------------------------------- |
| Trigger name            | ```CPU over 50```                |
| Severity level          | 1 (Highest)                      |
| Trigger condition       | IS ABOVE 50                      |

An example trigger configuration may look like

![os_monitor_5](/images/open-search-alerting/os_monitor_5.png)

7. For the trigger, configure an **Action** to send an email to our SNS Topic, fill in the action sections with the following values

| Field                   | Value                            |
| ----------------------- | -------------------------------- |
| Action name             | ```Email Alert```                |
| Destination             | SNS Destination (Amazon SNS)     |
| Message subject         | ```High CPU!```                  |
| Message                 | *Leave default message*          |

An example action may look like

![os_monitor_6](/images/open-search-alerting/os_monitor_6.png)

8. Click on **Create**

After the Monitor saves, your new High CPU Alert monitor dashboard will be available

![os_monitor_7](/images/open-search-alerting/os_monitor_7.png)

When you are ready move on, go to the next step [Trigger Alert]({{<relref "../4_Trigger_Alert/">}})
