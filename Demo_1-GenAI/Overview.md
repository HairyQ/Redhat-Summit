# Demo # 1 (Agentic Incident Report) Abstract
This workflow streamlines operations by transforming unstructured event reports into concise, actionable summaries using AI, enabling faster incident analysis and response. It reduces manual effort and ensures consistent, enterprise-wide asset management through automated data processing and system integration

This demo ingests unstructured, text-based event reports using Object Storage and triggers OCI Events to initiate processing. OCI Functions handle data cleansing and formatting, then invoke a Generative AI model (LLM) to summarize key incident details for easier analysis. The structured summaries are published via OCI Streaming and consumed by an orchestrator, which ensures reliable delivery to the enterprise asset management system. This automated pipeline reduces manual effort, accelerates response times, and standardizes incident reporting across the organization.

<p align="center">
  <img src="../Demo-Content/Images/Demo1_Architecture_Overview.png" alt="Demo 1 - Architecture Diagram" width="700"/>
</p>

# Demo Components
## 1. Demo Data Collection
### 1a. Download New Data
1. Navigate to NASA ASRS Database to download data.
  - LINK: https://akama.arc.nasa.gov/ASRSDBOnline/QueryWizard_Filter.aspx
2. Select appropriate filters 
  - Date Range: Jan 2014 - Dec 2024
  - Make/Model: All Airbus models
  - Mission: Passenger
3. Click Run Search > Export Excel File
### 1b. Transform and Supplement Data
1. Transform date variable to desired format
2. Consolidate Parent and Child Headers into single row
3. Remove empty rows (particularly Row 3)
4. Add 'MSNID' Variable
  - This will act as a dummy unique identifier (Manufacturer Serial Number) for the aircraft associated with each event. Ensure that each MSNID is only associated with a single 'Make Model Name' for consistency purposes.
### ALTERNATIVE: Access Existing Data Files
1. Navigate to [Demo_1-GenAI/Demo_Data](https://github.com/HairyQ/Redhat-Summit/tree/main/Demo_1-GenAI/Demo_Data) to access existing data downloads
   - Subset of dataset to be uploaded for live demo (4 records)
     https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Demo_Data/ASRS_New_Data.csv
   - Sample CSV output of subset
     https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Demo_Data/ASRS_New_Data_Sample-Output.csv
   - Sample of Doc version of subset
     https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Demo_Data/ASRS_Document_Example.docx
   - Additional data for training or exploratory purposes
     https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Demo_Data/ASRS_Additional_Data.xlsx


## 2. OpenShift Deployment


## 3. NVIDIA NIM Deployment (Llama Model)


## 4. OCI Event + Function + Stream Creation


## 5. Orchestrator Deployment


## 6. IBM Maximo Data Configuration


# Demo Steps
