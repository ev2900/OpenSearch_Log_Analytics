---
title: "4. Search Logs"
chapter: false
disableToc: false
menuTitle: "Search Logs"
weight: 10
---

Now that we are sending logs from CloudWatch to OpenSearch lets create and index patterns and run a simple search to validate that our logs are actually being sent to OpenSearch. 

OpenSearch is capable of more then search it can also build visualizations and more. In this section we will perform a simple search to ensure that our logs are actually being delivered. 

Check out the Visualize and Analyze section of the OpenSearch Log Analytics workshop for a more thorough lab on searching and visualizing logs.

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

The Lambda functions the send the messages from CloudWatch to OpenSearch will create a new OpenSearch index each day. Each index name will start with **cwl** and will be followed by the date. 

To search all of the CloudWatch logs (ie. multiple days) we will create an index pattern in OpenSearch. The index pattern will be a representation of all of the **cwl** log indexes for all of the days.

1. In the OpenSeach Dashboard, expand the side menu and click on **Stack Management** under managment section

![stack_managment](/images/open-search-log-analytics/va_1.PNG)

2. On the stack managment page click on **Index Patterns** on the left hand menu

![index_pattern](/images/open-search-log-analytics/va_2.PNG)

3. On the index patterns page click on **Create index pattern**

![create_index_pattern_1](/images/open-search-log-analytics/va_3.PNG)

4. Enter ```cwl-*``` under the index pattern name section
5. Click on **Next step**

![create_index_pattern_2](/images/collect-log-cloud-watch/OS_1.PNG)

6. Select ```@timestamp``` as the primary time feild
7. Click on **Create index pattern**

![create_index_pattern_2](/images/collect-log-cloud-watch/OS_2.PNG)

We have now created an index pattern! We can use the index pattern to analyze our logs

### Search the Logs

OpenSearch provides the ability to easily search log data. Lets run a simple searche on our logs to validate that they have been sucssfully sent from CloudWatch to OpenSearch.

The Glue Jobs that you ran earlier logged custom message of *Sucess!!* and *Error!!*

We can search for the *Sucess!!* logs 

1. In the OpenSearch Dashboard expand the side menu and click on **Discover** under the OpenSearch Dashboards section

![search_1](/images/open-search-log-analytics/search_1.PNG)

This will bring you to the discovery page. On this page we can see the log data sent from CloudWatch

2. Ensure that you adjust the time range in the top right hand corner to include a large enough range that all of the logs we collected are included. Click **Update** or **Refresh** once you update the time range

![create_index_pattern_2](/images/collect-log-cloud-watch/OS_3.PNG)

3. We can now search our CloudWatch logs. Try searching for ```Success!!``` you will see the log message that the Glue job created during its execution 

![create_index_pattern_2](/images/collect-log-cloud-watch/OS_4.PNG)

You will see a few logs that contain the customer log message from the Glub Job. Feel free to spend a few minutes trying other OpenSearch searches. See if you can search for the other *Error!!* logs

When you are ready proceed to the next step [Clean Up]({{<relref "../5_Clean_Up/">}}) if you want to delete the resources we used for this workshop
