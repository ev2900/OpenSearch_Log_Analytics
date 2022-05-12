---
title: "4. Search Logs"
chapter: false
disableToc: false
menuTitle: "Search Logs"
weight: 10
---

OpenSearch provides us the ability to analyze out logs. Let's begin by navigating to the OpenSearch Dashboard

### Step 1 - Open the OpenSearch Dashboard

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on the **fluentd-domain** OpenSearch domain you created earlier

![search_logs_1](/images/open-search-fluentd/search_logs_1.png)

3. Click on the OpenSearch Dashboard URL. This should open the URL in a web browser window

![search_logs_2](/images/open-search-fluentd/search_logs_2.png)

4. You will be prompted to log in. For the user name enter ```OSMasterUser``` for the password enter ```AwS#OpenSearch1``` 
5. If an additional popup window is present after login asking about data upload click on **Explore on my own**
6. If an additional popup window is present asking you to select your tenant select **Global** and click on **Confirm**

You should now see a window that looks like this

![search_logs_3](/images/open-search-fluentd/search_logs_3.png)

### Step 2 - Create an Index Pattern

In order to search our logs via. the OpenSearch dashboard you need to create an index pattern. Follow the steps below to create an index pattern for the Fluentd logs

1. In the OpenSearch Dashboard, expand the side menu and click on **Stack Management** under management section

![stack_management](/images/open-search-log-analytics/va_1.PNG)

2. On the stack management page click on **Index Patterns** on the left hand menu

![index_pattern](/images/open-search-log-analytics/va_2.PNG)

3. On the index patterns page click on **Create index pattern**

![create_index_pattern_1](/images/open-search-log-analytics/va_3.PNG)

4. Enter ```fluentd*``` under the index pattern name section
5. Click on **Next step**

![search_logs_7.png](/images/open-search-fluentd/search_logs_7.png)

6. Click on **Create index pattern**

You have now created an index pattern! You can use the index pattern to analyze our logs

### Step 3 - Search the Logs

OpenSearch provides the ability to easily search log data. Let's view and search our logs sent by Fluentd

1. In the OpenSearch Dashboard expand the side menu and click on **Discover** under the OpenSearch Dashboards section

![search_1](/images/open-search-log-analytics/search_1.PNG)

This will bring you to the discovery page. You can now see the sample logs Fluentd sent to OpenSearch

![search_logs_9.png](/images/open-search-fluentd/search_logs_9.png)

You can expand any of the logs to view all of the available fields

![search_logs_10](/images/open-search-fluentd/search_logs_10.png)

You can also search logs using the search bar at the top of the page

![search_logs_10](/images/open-search-fluentd/search_logs_11.png)

When you are ready proceed to the next step [Clean Up]({{<relref "../5_Clean_Up/">}}) if you want to delete the resources you used for this workshop