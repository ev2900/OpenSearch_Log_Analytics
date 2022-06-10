---
title: "4. Trigger Alert"
chapter: false
disableToc: false
menuTitle: "Trigger Alert"
weight: 10
---

You will now simulate an alert condition and verify that our alert triggers and you receive an email 

#### Step 1 - Run a Python Application from Cloud9

1. Navigate to the [Cloud9 Console](https://console.aws.amazon.com/cloud9/home) 
2. Click on **Open IDE** under the already created workshop-cloud9 environment. 

![cloud9_2](/images/open-search-alerting/cloud9_2.png)

The [OpenSearch_API_Examples](https://github.com/ev2900/OpenSearch_API_Examples) repository will be automatically pulled down to your environment. Do the following within the Cloud9 console.

1. Open the file **OpenSearch_API_Examples/Alerting/2_trigger_alert.py**
2. Update the **os_url** variable to your OpenSearch instance. This is the value of the **OSDomainURL** key from the CloudFormation stack output.
3. Goto **File** -> **Save** to save the changes to 2_trigger_alert.py

In the terminal window, run the following commands:

4. ```python OpenSearch_API_Examples/Alerting/2_trigger_alert.py```

The image below highlights the commands. 

![cloud9_trigger](/images/open-search-alerting/cloud9_trigger_1.png)

The script will to send high CPU values to OpenSearch until you stop the script. You can stop it with **Ctrl-C** in the terminal window.


### Step 2 - Verify Alerting

1. Emails should have been received in the specified email address.

![cloud9_email](/images/open-search-alerting/os_email_1.png)

2. Click on the top left hand menu on the OpenSearch dashboard
3. Click on **Alerting** under the OpenSearch Plugins section

![os_alert_1](/images/open-search-alerting/os_alert_1.png)

4. Click on **Monitors**
5. Click on the **High CPU Alert**

![os_alert_4](/images/open-search-alerting/os_alert_4.png)

Observe the **History** section. You should see the *Triggered* status occurring.

![cloud9_email_2](/images/open-search-alerting/os_email_2.png)

6. Under the **Alerts** section, click on the alert and acknowledge the alert to stop receiving email.

When you are ready proceed to the next step [Clean Up]({{<relref "../5_Clean_Up/">}}) if you want to delete the resources you used for this workshop