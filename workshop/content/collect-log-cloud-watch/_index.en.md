---
title: "2. CloudWatch Log Collection"
menuTitle: "CloudWatch Log Collection"
chapter: true
weight: 10
url: "/collect-log-cloud-watch/"
---

# Collect AWS CloudWarch Logs for OpenSearch

This workshop covers how to send logs from CloudWatch to OpenSearch. CloudWatch can be a rich source of log for various AWS services. Intergrating logs from CloudWatch into OpenSearch can imporove you ability to use OpenSearch for various log analytics use cases.

In this workshop we will implement the following architecture

![create_index_pattern_2](/images/collect-log-cloud-watch/architecture.PNG)

The architecture uses two Glue Jobs to generate CloudWatch logs. Lamdba functions send the data from CloudWatch to OpenSearch in realtime. Once in OpenSearch we are able to search for the custom logging messages that the Glue Jobs create.

When you are ready to being the lab navigate to [Getting started]({{<relref "./1_Getting_Started/">}})