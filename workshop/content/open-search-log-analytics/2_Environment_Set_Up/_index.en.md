---
title: "2. Environment Set Up"
chapter: false
disableToc: false
menuTitle: "Environment Set Up"
weight: 10
---

We will need to deploy a few services and configure our AWS environment before we can get started.

We will need to complete the following set up steps

1. Create an OpenSearch Domain
2. Create a Kinesis Firehose
3. Configure Identity Access Management Permissions

Two options to complete these steps are available. Option 1 uses a CloudFormation template to automate steps 1 + 2. Option 2 provides instructions to complete steps 1 + 2 manually via. the AWS console. 

To complete the environment step up via. a CloudFormation template follow the steps in the [CloudFormation (Automated)]({{<relref "../2_Environment_Set_Up/cloudformation_automated">}})

Of if you would prefer to set up your AWS environment manually via. the AWS console follow the steps in the [Console Deploy (Manual)]({{<relref "../2_Environment_Set_Up/console_manual">}})