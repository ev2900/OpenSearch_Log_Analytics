---
title: "4. Trigger Alert"
chapter: false
disableToc: false
menuTitle: "Trigger Alert"
weight: 10
---

In this exercise, we will simulate an alert condition and verify our email alert is working properly.        

#### Run a Python Application from Cloud9

Navigate to the [Cloud9 Console](https://console.aws.amazon.com/cloud9/home) and click on **Open IDE** under the already created ```workshop-cloud9``` environment. The [OpenSearch_API_Examples](https://github.com/ev2900/OpenSearch_API_Examples) repository will be automatically pulled down to your environment. Do the following within the Cloud9 console.

1. Open the file **OpenSearch_API_Examples/Alerting/2_trigger_alert.py**

2. Update the **os_url** variable to your OpenSearch instance. This is the **OSDomainURL** Output from the CloudFormation stack.

3. Go to File->Save to save the changes to **2_trigger_alert.py**

In the terminal window, run the following commands:

4. ```python OpenSearch_API_Examples/Alerting/2_trigger_alert.py```

The image below highlights the commands. 

![cloud9_trigger](/images/open-search-alerting/cloud9_trigger_1.png)

The script will to send high CPU values to OpenSearch until you stop the script. You can stop it with **Ctrl-C** in the terminal window.


### Verify Alerting

1. Emails should have been received in the specified email address.

![cloud9_email](/images/open-search-alerting/os_email_1.png)

2. In the OpenSearch Dashboard, click the menu icon and go to **OpenSearch Plugins->Alerting**. 

3. Click on the **Monitors** tab and open the **High CPU Alert** monitor we created earlier.

Observe the **History** section. You should see the *Triggered* status occurring.

![cloud9_email_2](/images/open-search-alerting/os_email_2.png)

Under the **Alerts** section, this will show active and historical alerts triggered by this monitor.

In order to stop receiving emails, we need to acknowledge the alert.

4. Select the alert caused by running the script. Click **Acknowledge**

When you are ready proceed to the next step [Clean Up]({{<relref "../5_Clean_Up/">}}) if you want to delete the resources we used for this workshop
