---
title: "1. OpenSearch Log Analytics"
menuTitle: "OpenSearch Log Analytics"
chapter: true
weight: 10
url: "/open-search-log-analytics/"
---

# OpenSearch Log Analytics Workshop

This workshop is an introduction to log analytics with Amazon OpenSearch Service. OpenSearch allows for full text search on logs indexed by the service. In this workshop we use sample Spark logs to learn about log analytics with Amazon OpenSearch Service.

In this workshop we will implement the following architecture

![cloud_shell_button](/images/open-search-log-analytics/architecture.png)

The architecture uses a Python application run from a Cloud9 development environment to simulate a log producer. The application will send 2,000 logs that we will later analyze. The Python application will send the logs to Kinesis Data Firehose. Kinesis Data Firehose will ingest the log into OpenSearch. Once the logs are ingested we will use OpenSearch Dashboard to analyze our logs

When you are ready to being the lab navigate to [Getting started]({{<relref "./1_Getting_Started/">}})