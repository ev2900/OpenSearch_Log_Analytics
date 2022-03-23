---
title: "4. Visualize and Analyze"
chapter: false
disableToc: false
menuTitle: "Visualize and Analyze"
weight: 10
---

OpenSearch provides us the ability to analyze out logs. Let's begin by navigating to the OpenSearch Dashboard

### Open the OpenSearch Dashboard

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on the **workshop-domain** OpenSearch domain you created earlier

![select_domain](/images/open-search-log-analytics/IAM_1.PNG)

3. Click on the OpenSearch Dashboard URL. This should open the URL in a web browser window

![open_search_dashboard](/images/open-search-log-analytics/IAM_4.PNG)

4. You will be prompted to log in. For the user name enter ```OSMasterUser``` for the password enter ```AwS#OpenSearch1``` 
5. If an additional popup window is present after login asking about data upload click on **Explore on my own**
6. If an additional popup windows is present asking you to select your tenant select **Global** and click on **Confirm**

You should now see a window that looks like this

![select_domain](/images/open-search-log-analytics/os_1.PNG)

### Create an Index Pattern

When we deployed Kinesis Data Firehose we configured it to create a new index in OpenSearch every 1 hr. We also configured it to name each index starting with *workshop-log* 

This means that open search will have 1 index for each hour it is sent logs, and that these indices' names will start with *workshop-log*

In order to work with all of the logs (ie. multiple hours) we will create an index pattern in OpenSearch. The index pattern will be a representation of all of the *workshop-log* indexes for all of the hours

1. In the OpenSearch Dashboard, expand the side menu and click on **Stack Management** under management section

![stack_management](/images/open-search-log-analytics/va_1.PNG)

2. On the stack management page click on **Index Patterns** on the left hand menu

![index_pattern](/images/open-search-log-analytics/va_2.PNG)

3. On the index patterns page click on **Create index pattern**

![create_index_pattern_1](/images/open-search-log-analytics/va_3.PNG)

4. Enter ```workshop-*``` under the index pattern name section
5. Click on **Next step**

![create_index_pattern_2](/images/open-search-log-analytics/va_4.PNG)

6. Select **date** as the time field
7. Click on **Create index pattern**

![create_index_pattern_3](/images/open-search-log-analytics/va_5.PNG)

We have now created an index pattern! We can use the index pattern to analyze our logs

### Search the Logs

OpenSearch provides the ability to easily search log data. Let's run a few simple searches on our logs

1. In the OpenSearch Dashboard expand the side menu and click on **Discover** under the OpenSearch Dashboards section

![search_1](/images/open-search-log-analytics/search_1.PNG)

This will bring you to the discovery page. By default this view of the log data views the last 15 minutes. Let's adjust it to display the last two years of data.

2. Click on date/time filter next to the search bar
3. Configure the relative date range for 2 years
4. Click on the **Update** 

![search_4](/images/open-search-log-analytics/search_4.PNG)

We can now see the log data we sent via. the Cloud9 Python application

![search_2](/images/open-search-log-analytics/search_2.PNG)

We can now run a few different searched against our index pattern. To get started lets look for any log messages that related to spark broadcast operations.

5. Run the search ```"spark" AND "broadcast"```

![search_3](/images/open-search-log-analytics/search_3.PNG)

OpenSearch displays the 74 logs of the total 2000 logs. Now that you have run a search. Try running at least 3 other searches. A few search suggestions are below. However feel free to come up with you own

Suggested searches 

1. ```date:2021-01-01```
2. ```date:2021-01-01 AND message:Memory```
3. ```date<2021-01-01```

After you have run a few searches. We can look at creating a visualization and dashboard

### Create a Visualization

1. In the OpenSearch Dashboard expand the side menu and click on **Visualize** under the OpenSearch Dashboards section

![visualize_1](/images/open-search-log-analytics/visualize_1.PNG)

2. Click on **Create new visualization**

![visualize_3](/images/open-search-log-analytics/visualize_3.PNG)

3. Click on **Gauge** from the list of visualizations
4. Click **workshop-** from the list of index patterns
5. Click on date/time filter next to the search bar
6. Configure the relative date range for 2 years
7. Click on the Update

![visualize_5](/images/open-search-log-analytics/visualize_5.png)

8. On the create page enter ```"spark" AND "broadcast"``` in the search bar

![visualize_4](/images/open-search-log-analytics/visualize_4.PNG)

This will produce a gauge chart visual.

6. Click on the **Save** button. Name the visual anything you would like

### Create a Dashboard

Dashboards allow you to combine multiple visualizations in a single place. Let's build a simple dashboard

1. In the OpenSearch Dashboard expand the side menu and click on **Dashboards** under the OpenSearch Dashboards section

![visualize_1](/images/open-search-log-analytics/dashboard_1.PNG)

2. On the dashboard page click on **Create new dashboard**

![visualize_4](/images/open-search-log-analytics/dashboard_4.PNG)

3. On the dashboard page click on **Add an existing** 

![visualize_1](/images/open-search-log-analytics/dashboard_2.PNG)

4. Select the visualization you just created. 

![visualize_1](/images/open-search-log-analytics/dashboard_3.PNG)

Use the create new button or repeat the earlier process to create at least 2 additional visuals. Try to create visuals that can show

1. Horizontal bar chart showing how many logs we received per day
2. Bar chart showing the number of logs level (ie. ERROR, WARNING, INFO)

When you are ready proceed to the next step [Clean Up]({{<relref "../5_Clean_Up/">}}) if you want to delete the resources we used for this workshop