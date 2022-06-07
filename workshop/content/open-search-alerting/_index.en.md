---
title: "OpenSearch Alerting"
menuTitle: "OpenSearch Alerting"
chapter: true
weight: 10
url: "/open-search-alerting/"
---

# OpenSearch Alerting Workshop

This workshop demonstrates how alerts work with OpenSearch. When data from your OpenSearch indices match certain conditions, an alert can notify destinations such as SNS or Slack. For example, you may want an alert if your application reports connection timeouts to dependent server.

In this workshop we will implement the following architecture:

![cloud_shell_button](/images/open-search-alerting/OpenSearch_demo_alerting_yaml.png)

The architecture uses Python applications run from a Cloud9 development environment to create a sample index and to send sample data to OpenSearch. We will set up an alert in OpenSearch and send notifications using Amazon Simple Notification Service (SNS) to an email address.

When you are ready to being the lab navigate to [Getting started]({{<relref "./1_Getting_Started/">}})
