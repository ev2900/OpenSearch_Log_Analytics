---
title: "Cross Cluster Replication"
menuTitle: "Cross Cluster Replication"
chapter: true
weight: 10
url: "/open-search-cross-cluster-replication/"
---

# Cross Cluster Replication Workshop

This workshop demonstrates how to replicate indexes, mapping, and metadata from one OpenSearch Service domain to another. This follows an active-passive replication model where a following index pulls data from a leader index to keep the indexes in sync.

In this workshop you will implement the following architecture:

![cloud_shell_button](/images/open-search-cross-cluster-replication/OpenSearch_cross_cluster_replication_demo_yaml.png)

The architecture uses Python applications run from a Cloud9 development environment to create a sample index and to send sample data to OpenSearch. You will set up replication between the leader and follower domains and observe how the index data replicates.

When you are ready to being the lab navigate to [Getting started]({{<relref "./1_Getting_Started/">}})
