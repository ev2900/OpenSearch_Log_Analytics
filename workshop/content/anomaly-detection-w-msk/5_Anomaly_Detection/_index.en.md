---
title: "5. Anomaly Detection"
chapter: false
disableToc: false
menuTitle: "Anomaly Detection"
weight: 10
---

Now that you have sent data to MSK via. the two python scripts in Cloud9. Lets first validate that we can see the log data in OpenSearch. Then second, lets create our anomaly detector. 

### Step 1 - Create Index Pattern

1. Navigate to the [OpenSearch page in the AWS console](https://us-east-1.console.aws.amazon.com/esv3/home)
2. Click on **workshop-domain**

![anomoly_1](/images/anomaly-detection-w-msk/anomoly_1.png)

3. Click on the **OpenSearch Dashboards URL**

![anomoly_2](/images/anomaly-detection-w-msk/anomoly_2.png)

4. You will be prompted to log in. For the user name enter ```OSMasterUser``` for the password enter ```AwS#OpenSearch1``` 
5. If an additional popup window is present after login asking about data upload click on **Explore on my own**
6. If an additional popup window is present asking you to select your tenant select **Global** and click on **Confirm**
7. In the OpenSearch Dashboard, expand the side menu and click on Stack Management under management section

![stack_management](/images/open-search-log-analytics/va_1.PNG)

8. On the stack management page click on **Index Patterns** on the left hand menu

![index_pattern](/images/open-search-log-analytics/va_2.PNG)

9. On the index patterns page click on **Create index pattern**

![create_index_pattern_1](/images/open-search-log-analytics/va_3.PNG)

10. Enter ```infa-logs-*``` under the index pattern name section

![anomoly_3](/images/anomaly-detection-w-msk/anomoly_3.png)

11. Click on **Next step**
12. Click on the time field drop down and select **eventtime**

![anomoly_4](/images/anomaly-detection-w-msk/anomoly_4.png)

13. Click on **Create index pattern**

You have now created an index pattern! You can use the index pattern to search our log and validate that the logs have been send from MSK to OpenSearch

### Step 2 - Search Logs

1. In the OpenSearch Dashboard expand the side menu and click on **Discover** under the OpenSearch Dashboards section

![search_1](/images/open-search-log-analytics/search_1.PNG)

2. Expand the time range that OpenSearch will view to the **Last 3 year**

![anomoly_5](/images/anomaly-detection-w-msk/anomoly_5.png)

You will now be able to see logs from the past 3 yrs

![anomoly_6](/images/anomaly-detection-w-msk/anomoly_6.png)

### Step 3 - Create Anomoly Detector

1. In the OpenSearch Dashboard expand the side menu and click on Anomaly detection under the OpenSearch Plugins section

![anomoly_7](/images/anomaly-detection-w-msk/anomoly_7.png)

2. Click on **Create detector**

![anomoly_8](/images/anomaly-detection-w-msk/anomoly_8.png)

3. Enter ```cpu_detector``` for the name of the detector
4. Pick ```infa-logs-1``` for the data source of the detector

![anomoly_9](/images/anomaly-detection-w-msk/anomoly_9.png)

5. Pick ```eventtime``` for the timestamp of the detector
6. Change the detector interval to ```1440```
7. Click on **Next**

![anomoly_10](/images/anomaly-detection-w-msk/anomoly_10.png)

8. Enter ``CPU-Utilization`` for the feature name
9. Select ```average()``` for the aggregation method
10. Select ```cpu_util``` for the field

![anomoly_11](/images/anomaly-detection-w-msk/anomoly_11.png)

11. Click the check box to enable categorical fields
12. Select ```application_id``` for the categorical field
13. Click on **Next**

![anomoly_12](/images/anomaly-detection-w-msk/anomoly_12.png)

14. Click to uncheck the box to start real-time detector automatically
15. Click the check box to run historical analysis detection
16. Adjust the historical analysis date range to the last 3 yrs 
17. Click on **Apply**
18. Click on **Next**

![anomoly_13](/images/anomaly-detection-w-msk/anomoly_13.png)

19. Click on **Create detector**

### Step 4 - View Anomaly Detector Results

1. Click on the **Historical analysis** tab

![anomoly_14](/images/anomaly-detection-w-msk/anomoly_14.png)

You will now be able to see a heat map of the anomaly's detected by application. Click on an of the rectangles in the heat map to see a more detailed view of the anomaly

![anomoly_15](/images/anomaly-detection-w-msk/anomoly_15.png)

When you are ready proceed to the next step [Clean Up]({{<relref "../6_Clean_Up/">}}) if you want to delete the resources we used for this workshop