---
title: "4. Visualize and Analyze in Kibana"
chapter: false
disableToc: false
menuTitle: "Visualize and Analyze in Kibana"
weight: 10
---

OpenSearch provides us the ability to analyze out logs. Lets begin by naviaging to the OpenSearch Dashboard  

### Open the OpenSearch Dashboard

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on the **workshop-domain** OpenSearch domain you created earlier

![select_domain](/images/open-search-log-analytics/IAM_1.PNG)

3. Click on the OpenSearch Dashboard URL. This should open the URL in a web browser window

![open_search_dashboard](/images/open-search-log-analytics/IAM_4.PNG)

4. You will be prompted to log in. Using the user name and password you created during the OpenSearch deployment, log in 
5. If an additonal pop up window is present after login asking about data upload click on **Explore on my own**
6. If an additonal pop up windows is present asking you to select your tenant select **Global** and click on **Confirm**

You should now see a window that looks like this

![select_domain](/images/open-search-log-analytics/os_1.PNG)

### Create an Index Pattern

When we deployed Kinesis Data Firehose we configured it to create a new index in OpenSearch every 1 hr. We also configured it to name each index starting with *workshop-log* 

This means that open search will have 1 index for each hour it is sent logs and that these indexies's name will start with *workshop-log*

In order to work with all of the logs (ie. multiple hours) we will create an index pattern in OpenSearch. The index pattern will be a representation of all of the *workshop-log* indexes for all of the hours

1. In the OpenSeach Dashboard, expand the side menu and click on **Stack Management** under managment section

![stack_managment](/images/open-search-log-analytics/va_1.PNG)

2. On the stack managment page click on **Index Patterns** on the left hand menu

![index_pattern](/images/open-search-log-analytics/va_2.PNG)

3. On the index patterns page click on **Create index pattern**

![create_index_pattern_1](/images/open-search-log-analytics/va_3.PNG)

4. Enter ```workshop-log-*``` under the index pattern name section
5. Click on **Next step**

![create_index_pattern_2](/images/open-search-log-analytics/va_4.PNG)

6. Click on **Create index pattern**

![create_index_pattern_3](/images/open-search-log-analytics/va_5.PNG)

We have not created an index pattern! We can use the index pattern to analyze our logs

### Search the Logs

OpenSearch provides the ability to easily search log data. Lets run a few simple searches on our logs

1. In the OpenSearch Dashboard expand the side menu and click on **Discover** under the OpenSearch Dashboards section

![search_1](/images/open-search-log-analytics/search_1.PNG)

This will bring you to the discovery page. On this page we can see the log data we sent via. the Cloud9 Python application

![search_2](/images/open-search-log-analytics/search_2.PNG)

We can now run a few different searched against our index pattern. To get started lets look for any log messages that are Hadoop Error. Remeber that we have 4 types of logs in our index Hadoop, Spark, HDFS, ZooKeeper

2. Run the search ```"Hadoop" AND "Error"```

![search_3](/images/open-search-log-analytics/search_3.PNG)

OpenSearch displays the 156 Hadoop error logs of the total 8000 logs. Now that you have run a search. Try running at least 3 other searchs. A few search suggestions are below. However feel free to come up with you own

Suggested searches 

1. ```"spark" AND "broadcast"```
2. ```"hdfs"```
3. ```"zoo_keeper" AND "WARN" AND "waiting for message"```

After you have run a few searches. We can look at creating a visualization and dashboard

### Create a Visualization

1. In the OpenSearch Dashboard expand the side menu and click on **Visualize** under the OpenSearch Dashboards section

![visualize_1](/images/open-search-log-analytics/visualize_1.PNG)

2. Click on **Create new visualization**

![visualize_3](/images/open-search-log-analytics/visualize_3.PNG)

3. Click on **Gauge** from the list of visualizations
4. Click **workshop-log-** from the list of index patterns
5. On the create page enter ```"Hadoop" AND "ERROR"``` in the search bar

![visualize_3](/images/open-search-log-analytics/visualize_4.PNG)

This will produce a gauge chart visualizing the number of hadoop error logs.

6. Click on the **Save** button. Name the visual anything you would like

### Create a Dashboard

Dashboards allow you to combine multiple visualizations in a single place. Lets build a simple dashboard

1. In the OpenSearch Dashboard expand the side menu and click on **Visualize** under the OpenSearch Dashboards section

![visualize_1](/images/open-search-log-analytics/dashboard_1.PNG)

2. On the dashboard page click on **Add an existing** 

![visualize_1](/images/open-search-log-analytics/dashboard_2.PNG)

3. Select the visualization you just created. 

![visualize_1](/images/open-search-log-analytics/dashboard_3.PNG)

Use the create new button or repeat the earlier process to create a second visual and add it to your dashboard. Have at least 2 visuals on your dashboard. 

Also take note of the ability to save and share this dashboard with other. These options are listed on the top bar

When you are ready proceed to the next step [Clean Up]({{<relref "../5_Clean_Up/">}}) if you want to delete the resources we used for this workshop
