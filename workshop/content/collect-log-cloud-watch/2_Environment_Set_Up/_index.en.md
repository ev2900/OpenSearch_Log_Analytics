---
title: "2. Environment Set Up"
chapter: false
disableToc: false
menuTitle: "Environment Set Up"
weight: 10
---

We need to deploy a few services and configure our AWS environment before we can get started.

We will need to complete the following set up steps

1. Create an OpenSearch Domain
2. Create an IAM Role
3. Map IAM Role to OpenSearch Role
4. Deploy Glue Jobs to Generate CloudWatch Logs

Follow the instructions below for each step

#### Create an OpenSearch Domain

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on **Create domain** 

![cloud_shell_button](/images/open-search-log-analytics/set_up_1.PNG)

3. Enter the name ```workshop-domain``` for the OpenSearch Domain
4. Under the deployment type section, select ```Development and testing```
5. Under the network section, select ```Public access```
6. Under the fine-grained access control section select ```Create master user```
7. Enter and username and password. Copy down the user name and password. We will need these later in the workshop
8. Leave all other settings at the default selections
9. Click on **Create**

It will take approximately 5 - 10 minutes for your OpenSearch domain to be created. Upon successful creation you will see your OpenSearch domain status is active

![cloud_shell_button](/images/open-search-log-analytics/set_up_2.PNG)

Do not proceed to the next step until you confirm that your domain status is active

#### Create an IAM Role

1. Go to the [IAM Console](https://console.aws.amazon.com/iamv2/home)
2. Click on **Roles** 

![ONFIG_IAM_1](/images/collect-log-cloud-watch/CONFIG_IAM_1.PNG)

3. Click on **Create role**

![CONFIG_IAM_2](/images/collect-log-cloud-watch/CONFIG_IAM_2.PNG)

4. Under the choose a use case click on **Lambda** and then click on **Next:Permissions**

![CONFIG_IAM_3](/images/collect-log-cloud-watch/CONFIG_IAM_3.PNG)

5. Search for ```AdministratorAccess``` and click on the box next to the AdministratorAccess policies 

**Note** for the purposes of this workshop we will give the IAM role AdministratorAccess. In a production environment you should scope down the permissions given to the IAM role

![CONFIG_IAM_4](/images/collect-log-cloud-watch/CONFIG_IAM_4.PNG)

6. Click on **Next: Tags**
7. Click on **Next: Review** . There is no need to change anything on the Add tags page
8. Name the role ```workshop-role```
9. Click on **Create role**

![CONFIG_IAM_5](/images/collect-log-cloud-watch/CONFIG_IAM_5.PNG)

10. Back on the [IAM Roles page](https://console.aws.amazon.com/iamv2/home#/roles) search for and select the ```workshop-role``` you just created 

![CONFIG_IAM_6](/images/collect-log-cloud-watch/CONFIG_IAM_6.PNG)

11. On the summary page copy down the Role ARN. We will need this later in the workshop

![CONFIG_IAM_7](/images/collect-log-cloud-watch/CONFIG_IAM_7.PNG)

12. Click on the **Trust relationships** tab
13. Click on the **Edit trust relationship**

![CONFIG_IAM_9](/images/collect-log-cloud-watch/CONFIG_IAM_9.PNG)

14. Replace the service section of the JSON with the following

```
"Service": [
	"lambda.amazonaws.com",
	"glue.amazonaws.com"
]
```

Your trust relationship policy document should look like the following

![CONFIG_IAM_10](/images/collect-log-cloud-watch/CONFIG_IAM_10.PNG)

15. Click on **Update Trust Policy**

#### Map IAM Role to OpenSearch Role

1. Go to the [OpenSearch Console](https://console.aws.amazon.com/esv3/home)
2. Click on the **workshop-domain** OpenSearch domain you created earlier
3. Click on the OpenSearch Dashboard URL. This should open the URL in a web browser window

![open_search_dashboard](/images/open-search-log-analytics/IAM_4.PNG)

4. You will be prompted to log in. Using the user name and password you created during the OpenSearch deployment, log in 
5. If an additional pop up window is present after login asking about data upload click on **Explore on my own**
6. If an additional pop up windows is present asking you to select your tenant select **Global** and click on **Confirm**

You should now see a window that looks like this

![select_domain](/images/open-search-log-analytics/os_1.PNG)

7. Click on and expand the hamburger menu on the side bar of the OpenSearch home page
8. Under the OpenSearch Plugins section click on **Security**

![select_security](/images/open-search-log-analytics/os_2.PNG)

9. On the security page click on **Roles** from the left hand menu

![select_roles](/images/open-search-log-analytics/os_3.PNG)

10. On the roles page search for and click on ```all_access``` 

![search_all_access](/images/open-search-log-analytics/os_4.PNG)

11. On the all_access role page click on **Mapped users**
12. Under the mapped users page click on **Manage mapping**

![mapped_users](/images/open-search-log-analytics/os_5.PNG)

13. Under the backend roles section enter the ARN that you copied down earlier for the IAM workshop-role that you created
14. Click on **Map** 

![CONFIG_IAM_8](/images/collect-log-cloud-watch/CONFIG_IAM_8.PNG)

#### Deploy Glue Jobs to Generate CloudWatch Logs

CloudWatch provides log collection for AWS services. In order to generate logs that we can use in this workshop we will create two simple AWS Glue Jobs. We can run these jobs to produce logs. Subsequently we can analyze these logs in OpenSearch

1. Go to the [Glue Console](https://console.aws.amazon.com/glue/home)
2. On the left hand menu click on **Jobs**

![GLUE_1](/images/collect-log-cloud-watch/GLUE_1.PNG)

3. On the jobs page click on **Add job**

![GLUE_2](/images/collect-log-cloud-watch/GLUE_2.PNG)

4. Enter ```glue_job_success``` for the name of the job
5. For the IAM tole select **workshop-role**
6. Under the this job run section select **A new script to be authored by you**

![GLUE_3](/images/collect-log-cloud-watch/GLUE_3.PNG)

7. Under the monitoring options click on **Job metrics** and **Continuous logging**

![GLUE_4](/images/collect-log-cloud-watch/GLUE_4.PNG)

8. Under the security configuration, script libraries, and job parameters (optional) set the max concurrency to ```10```

![GLUE_7](/images/collect-log-cloud-watch/GLUE_7.PNG)

9. Leave all other settings at the default selections and click on **Next** at the bottom of the page

10. On the connections page leave all of the setting at the defaults and click on **Save job and edit script**

![GLUE_4](/images/collect-log-cloud-watch/GLUE_5.PNG)

11. In the edit job window copy and paste the following code into the editing window

```
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

logger = glueContext.get_logger()

logger.error("Success!!")
```
![GLUE_4](/images/collect-log-cloud-watch/GLUE_6.PNG)

12. Click on **Save**
13. Click on **Run**
14. Repeat steps 1 - 13 again. However this time name the Glue job ```glue_job_error``` and use the following code in the job 

```
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)

logger = glueContext.get_logger()

logger.error("Error!!")
```

The jobs will use the logger in AWS Glue to produce custom error log message *Success!!* and *Error!!*. Later in this workshop we will search for the log message in OpenSearch.

You have completed the set up for your AWS environment! When you are ready lets begin the next step [Send Log Data to OpenSearch]({{<relref "../3_Send_Log_Data_to_OpenSearch/">}})
