---
title: "4. Send Logs"
chapter: false
disableToc: false
menuTitle: "Send Logs"
weight: 10
---

You need to send log data to MSK so it can subsequently be sent to OpenSearch (in real time) by the Lambda function we deployed. 

You will send the log data to Kafka via. a Python Script run from Cloud9

1. Navigate to the [MSK page in the AWS console](https://us-east-1.console.aws.amazon.com/msk/home)
2. Select the **msk-workshop-cluster**

![enviorment_set_up_msk_1](/images/anomaly-detection-w-msk/enviorment_set_up_msk_1.png)

3. Click on **View client information**

![enviorment_set_up_msk_2](/images/anomaly-detection-w-msk/enviorment_set_up_msk_2.png)

4. Copy the bootstrap servers connection information
5. Navigate to the [Cloud9 console](https://us-east-1.console.aws.amazon.com/cloud9/home)
6. Click on **Open IDE**

![enviorment_set_up_msk_4](/images/anomaly-detection-w-msk/enviorment_set_up_msk_4.png) 

7. In the Cloud9 environment navigate and open ```Kafka_OpenSearch_Anomaly_Detection/Kafka/2_base_data.py``` 
8. Update the **<plain_text_bootstrap_server>** with the bootstrap servers connection information you copied down
9. Run ```pip install pykafka``` 
10. Run ```cd ~``` in the Cloud9 terminal
11. Run ```python environment/Kafka_OpenSearch_Anomaly_Detection/Kafka/2_base_data.py```

![send_log_data_1](/images/anomaly-detection-w-msk/send_log_data_1.png)

Allow the python script to run until the terminal looks similar to the image below

![send_log_data_2](/images/anomaly-detection-w-msk/send_log_data_2.png)

12. open ```Kafka_OpenSearch_Anomaly_Detection/Kafka/3_anomoly_data.py```
13. Update the **<plain_text_bootstrap_server>** with the bootstrap servers connection information you copied down
14. Run ```python environment/Kafka_OpenSearch_Anomaly_Detection/Kafka/3_anomoly_data.py```

![send_log_data_3](/images/anomaly-detection-w-msk/send_log_data_3.png)

Allow this python script to run until completion. This may take several minutes. If you leave the Cloud9 environment open in your web browser as a separate tab you can move on to the next steps

When the script is complete the Cloud9 terminal will look similar to the image below 

![send_log_data_4](/images/anomaly-detection-w-msk/send_log_data_4.png)

We have completed the process of sending data to MSK. When you are ready begin the next step [Anomaly Detection]({{<relref "../5_Anomaly_Detection/">}})