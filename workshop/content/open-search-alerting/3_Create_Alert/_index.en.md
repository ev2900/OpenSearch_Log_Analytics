---
title: "3. Create Alert"
chapter: false
disableToc: false
menuTitle: "Create Alert"
weight: 10
---

Now we will configure an OpenSearch Alert using the index we created in the last step.

#### Create a Destination

In this section, we will configure the SNS Topic created from the CloudFormation script as an OpenSearch Alert Destination.

1. Open the OpenSearch Dashboard using the URL and credentials provided in the CloudFormation outputs: **DashboardURL, UserName, Password**
2. Click on the menu icon and go to **OpenSearch Plugins->Alerting**
![os_alert_1](/images/open-search-alerting/os_alert_1.png)
3. Click on the Destinations tab and push **Add destination**
![os_alert_2](/images/open-search-alerting/os_alert_2.png)
4. Add destination details and click **Create**
| Field         | Value                            |
| ------------- | -------------------------------- |
| Name          | ```SNS Destination```            |
| Type          | ```Amazon SNS```                 |
| SNS topic ARN | *TopicARN from CloudFormation*   |
| IAM role ARN  | *IAMRoleARN from CloudFormation* |

![os_alert_3](/images/open-search-alerting/os_alert_3.png)

#### Set up a Monitor

Next, we will configure a monitor that will trigger an alert if *cpu_util* exceeds 50.

1. Click on the **Monitors** tab and push **Create monitor**
![os_monitor_1](/images/open-search-alerting/os_monitor_1.png)
2. Fill in the **Monitor details** and **Data source** sections with the following values:
| Field                   | Value                            |
| ----------------------- | -------------------------------- |
| Monitor name            | ```High CPU Alert```             |
| Monitor type            | Per query monitor                |
| Monitor defining method | Visual editor                    |
| Frequency               | By interval                      |
| Run every               | 1 Minutes                        |
| Index                   | **alert-1**                      |
| Time field              | **eventtime**                    |

![os_monitor_2](/images/open-search-alerting/os_monitor_2.png)

3. Under Query, click **+ Add metric**
![os_monitor_3](/images/open-search-alerting/os_monitor_3.png)
4. Specify MAX OF cpu_util by setting Aggregation to **max()** and Field to **cpu_util**. Click **Save**.
![os_monitor_4](/images/open-search-alerting/os_monitor_4.png)
5. Under Triggers, click **Add trigger**. Create a trigger with the following:
| Field                   | Value                            |
| ----------------------- | -------------------------------- |
| Trigger name            | ```CPU over 50```                |
| Severity level          | 1 (Highest)                      |
| Trigger condition       | IS ABOVE 50                      |

![os_monitor_5](/images/open-search-alerting/os_monitor_5.png)

6. For that trigger, configure an **Action** to send an email to our SNS Topic.
| Field                   | Value                            |
| ----------------------- | -------------------------------- |
| Action name             | ```Email Alert```                |
| Destination             | SNS Destination (Amazon SNS)     |
| Message subject         | ```High CPU!```                  |
| Message                 | *Leave default message*          |

![os_monitor_6](/images/open-search-alerting/os_monitor_6.png)

After the Monitor saves, your new High CPU Alert monitor dashboard will be available.
![os_monitor_7](/images/open-search-alerting/os_monitor_7.png)

When you are ready move on, go to the next step [Trigger Alert]({{<relref "../4_Trigger_Alert/">}})
