---
title: "3. Setup Cross-Cluster Connection"
chapter: false
disableToc: false
menuTitle: "Setup Cross-Cluster Connection"
weight: 10
---

Now you will create a cross-cluster connection between our two OpenSearch domains. This will permit indexes to replicate between them.

#### Step 1 - Request Outbound Connection 

1. Open the AWS Console and navigate to the **Domains** section of OpenSearch 

![os_connect_1](/images/open-search-cross-cluster-replication/os_connect_1.png)


2. Select the 'workshop-domain-follower' domain and open the **Connections** tab. Click **Request** under the Outbound connection section.

![os_connect_2](/images/open-search-cross-cluster-replication/os_connect_2.png)

3. Here we will request a connection with the 'workshop-domain-leader' domain. Fill out the Connection alias, connect to a cluster in this AWS account, and select the 'workshop-domain-leader' domain in the dropdown. Click **Request**.

![os_connect_3](/images/open-search-cross-cluster-replication/os_connect_3.png)


#### Step 2 - Approve Connection

Now that you requested a connecton from the follower domain to the leader domain, the leader domain must approve the connection.

1. Under the **Domains** section of OpenSearch, open the 'workshop-domain-leader' domain and open the **Connections** tab. 

2. In the Inbound connections section, select the request from 'workshop-domain-follower' and click **Approve**. A popup will ask for your confirmation.

![os_connect_4](/images/open-search-cross-cluster-replication/os_connect_4.png)

Now the domains are ready for replication. 

When you are ready move on, go to the next step [Test Replication]({{<relref "../4_Test_Replication/">}})
