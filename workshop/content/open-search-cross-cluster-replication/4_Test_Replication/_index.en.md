---
title: "4. Test Replication"
chapter: false
disableToc: false
menuTitle: "Test Replication"
weight: 10
---

You will now create an index and replication rule that will copy data from the leader to the follower domain. 

#### Environment Info ####
1. Goto the OpenSearch service page and note the Domain endpoints for both leader and follower domain.
![cloud9_1](/images/open-search-cross-cluster-replication/cloud9_1.png)

{{% notice info %}}
Be sure that the URL does not contain a following forward slash.
{{% /notice %}}



#### Step 1 - Run a Python Application from Cloud9

1. Navigate to the [Cloud9 Console](https://console.aws.amazon.com/cloud9/home) 
2. Click on **Open IDE** under the already created workshop-cloud9 environment. 

![cloud9_2](/images/open-search-cross-cluster-replication/cloud9_2.png)

The [OpenSearch_API_Examples](https://github.com/ev2900/OpenSearch_API_Examples) repository will be automatically pulled down to your environment. Do the following within the Cloud9 console.


3. Open the file **OpenSearch_API_Examples/Cross_Cluster_Replication/cross_cluster_replication.py**
4. Update the **leader_os_url** and **follower_os_url** variables to your OpenSearch domains.
5. Goto **File** -> **Save** to save the changes to cross_cluster_replication.py

![cloud9_3](/images/open-search-cross-cluster-replication/cloud9_3.png)


In the terminal window, run the following commands:

6. ```pip install requests```
7. ```python OpenSearch_API_Examples/Cross_Cluster_Replication/cross_cluster_replication.py```

The image below highlights the commands. 

![cloud9_4](/images/open-search-cross-cluster-replication/cloud9_4.png)

The script creates and index called **log-data-1**, inserts a sample document, and creates a replication rule for all indexes that start with 'log'.

### Step 2 - Verify Replication

1. Goto the OpenSearch service page and note the Domain endpoints for both leader and follower domain. 

![cloud9_5](/images/open-search-cross-cluster-replication/cloud9_5.png)
 
2. Open the **Leader** OpenSearch Dashboard. Once you open the dashboard URL you will be prompted to login.

3. Enter ```OSMasterUser``` as the username
4. Enter ```AwS#OpenSearch1``` as the password
5. Click on **Log In**
6. If an additional pop up window is present after login asking about data upload click on **Explore on my own**
7. If an additional pop up windows is present asking you to select your tenant select **Global** and click on **Confirm**

Once you have logged in to the OpenSearch dashboard

7. Click on the top left hand menu on the OpenSearch dashboard
8. Click on **Query Workbench** under the OpenSearch Plugins section

![cloud9_6](/images/open-search-cross-cluster-replication/cloud9_6.png)

9. Select the data from log-data-1 using this simple query:
```SELECT * FROM log-data-1```

![cloud9_7](/images/open-search-cross-cluster-replication/cloud9_7.png)


10. Follow the same procedure for the **Follower** domain.

Observe that the result sets match between Leader and Follower.

11. Send more data by re-running the Python script and observe the result sets.
```python OpenSearch_API_Examples/Cross_Cluster_Replication/cross_cluster_replication.py```

![cloud9_8](/images/open-search-cross-cluster-replication/cloud9_8.png)


When you are ready, proceed to the next step [Clean Up]({{<relref "../5_Clean_Up/">}}) if you want to delete the resources you used for this workshop.
