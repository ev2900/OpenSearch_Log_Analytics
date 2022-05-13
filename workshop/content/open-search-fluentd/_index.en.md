---
title: "3. Fluntd Log Ingestion"
menuTitle: "Fluentd Log Ingestion"
chapter: true
weight: 10
url: "/open-search-fluentd/"
---

# Fluentd Log Ingestion

This workshop is an introduction to ingesting logs with [Fluentd](https://www.fluentd.org/). Fluentd is an open source data collector. Fluentd supports log parsing and ingestion directly to Amazon OpenSearch service.  

In this workshop you will implement the following architecture

![fluentd_architecture](/images/open-search-fluentd/fluentd_cloud9_opensearch_yml.png)



To implement this architecture you install Fluentd in an Ubuntu Cloud9 environments. Once installed you configure Fluentd to parse and send apache2 access logs to an OpenSearch domain.  

When you are ready to begin the lab navigate to [Getting started]({{<relref "./1_Getting_Started/">}})