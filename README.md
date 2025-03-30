# Log Analytics via Amazon OpenSearch Service

<img width="85" alt="map-user" src="https://img.shields.io/badge/views-1095-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-301-green">

Live at https://sharkech-public.s3.amazonaws.com/opensearch-log-analytics/workshop/index.html

In the workshop OpenSearch Log Analytics you will learn how to perform log analytics via AWS OpenSearch. You will explore the basics of ingesting, analyzing and visualizing data in OpenSearch.

## Rendering the Workshop Locally

1. [Install Hugo](https://gohugo.io/getting-started/installing/)
2. Download this repository
3. In a terminal navigate to the workshop directory ```cd OpenSearch_Log_Analytics/workshop```
4. Via the same terminal window run ```hugo serve```

## Automated Deployment

The main branch of the repo will auto deploy to the **development** site https://sharkech-public-dev.s3.amazonaws.com/dev-opensearch-log-analytics/index.html

Pull requests merged to the prod branch will auto deploy to the **production** site at https://sharkech-public.s3.amazonaws.com/opensearch-log-analytics/workshop/index.html

## You can help

Want to contribute to this workshop? Do you see a mistake? Fork this repo and submit a pull request with edits, updates, fixes

## Future Improvements Planned for this Repository

* Cross Cluster Replication
* Index managment including: roll ups, ultrawarm
