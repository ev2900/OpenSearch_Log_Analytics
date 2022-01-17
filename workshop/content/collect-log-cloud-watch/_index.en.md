---
title: "2. CloudWatch Log Collection"
menuTitle: "CloudWatch Log Collection"
chapter: true
weight: 10
url: "/collect-log-cloud-watch/"
---

# Collect AWS CloudWatch Logs for OpenSearch

This workshop covers how to send logs from CloudWatch to OpenSearch. CloudWatch can be a rich source of log for various AWS services. Integrating logs from CloudWatch into OpenSearch can improves your ability to use OpenSearch for various log analytics use cases.

In this workshop we will implement the following architecture:

![create_index_pattern_2](/images/collect-log-cloud-watch/architecture.PNG)

The architecture uses: two Glue Jobs to generate CloudWatch logs, Lambda functions to send log data from CloudWatch to OpenSearch. Once the CloudWatch log data is in OpenSearch we will search for log messages produced by the Glue Jobs.

When you are ready to being the lab navigate to [Getting started]({{<relref "./1_Getting_Started/">}})