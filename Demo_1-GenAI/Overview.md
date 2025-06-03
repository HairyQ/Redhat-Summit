# Demo # 1 (Agentic Incident Report) Abstract
This workflow streamlines operations by transforming unstructured event reports into concise, actionable summaries using AI, enabling faster incident analysis and response. It reduces manual effort and ensures consistent, enterprise-wide asset management through automated data processing and system integration

This demo ingests unstructured, text-based event reports using Object Storage and triggers OCI Events to initiate processing. OCI Functions handle data cleansing and formatting, then invoke a Generative AI model (LLM) to summarize key incident details for easier analysis. The structured summaries are published via OCI Streaming and consumed by an orchestrator, which ensures reliable delivery to the enterprise asset management system. This automated pipeline reduces manual effort, accelerates response times, and standardizes incident reporting across the organization.

<p align="center">
  <img src="../Demo-Content/Images/Demo1_Architecture_Overview.png" alt="Demo 1 - Architecture Diagram" width="700"/>
</p>

# Demo Components
## 1. Demo Data Collection
Step-by-Step Guide
    - https://github.com/HairyQ/Redhat-Summit/blob/0010aa2ea1e573e2c43d2607b728018f274009f2/Demo_1-GenAI/Step%201%3A%20Demo%20Data%20Collection/Step-by-Step%20Guide.md

Downloadable Content
    - https://github.com/HairyQ/Redhat-Summit/tree/8b812a542a54e7e4275b3834515aadda5bd76f77/Demo_1-GenAI/Demo_Data
## 2. OpenShift Deployment
Step-by-Step Guide   - https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Step%202%3A%20OpenShift%20Configuration/Step-by-Step%20Guide.md
## 3. NVIDIA NIM Deployment (Llama Model)
Step-by-Step Guide  - https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Step%203%3A%20NVIDA%20NIM%20Deployment/Step-by-Step%20Guide.md
## 4. OCI Event + Function + Stream Creation
Step-by-Step Guide  - https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Step%204%3A%20OCI%20Service%20Creation/Step-by-Step%20Guide.md
## 5. Orchestrator Deployment
Step-by-Step Guide  - https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Step%205%3A%20Orchestrator%20Deployment/Step-by-Step%20Guide.md
## 6. IBM Maximo Data Configuration
Step-by-Step Guide  - https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Step%206%3A%20IBM%20Maximo%20Data%20Configuration/Step-by-Step%20Guide.md


# Demo Steps
## Pre-Requisites
Follow the above Step-by-Step Guides to complete all the pre-requisites:

1. Download demo data
2. Create an OpenShift Cluster with GPUs
3. Deploy an NVIDIA NIM with Llama3 in a GPU node within that OpenShift cluster
4. Provision and configure Object Storage buckets, OCI Event, Function and Streaming services and edit relevant Python code
5. Configure Orchestrator node and edit relevant Python code
6. Enter dynamic values into IBM Maximo to ensure REST APIs will work

Once all of the components are appropriately configured, you can use the below steps to run through the demo process flow.

## Demo Steps
1. SSH into Orhcestrator node and start stream-consumer
2. Load data into Object Storage bucket
3. Navigate to OCI Functions and/or OCI Streaming to see Function status
4. Monitor Orchestrator command line 
