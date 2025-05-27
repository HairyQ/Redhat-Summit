# AI-Powered Intelligent Maintenance Solution on OCI 
## (2025 Red Hat Summit)
### Demo Overview
This demo showcases an end-to-end AI-enhanced incident and anomaly management workflow integrating Oracle Cloud Infrastructure (OCI), IBM Maximo, and open-source technologies. These core components are deployed on RedHat OpenShift in OCI, taking advantage of the flexible and scalable OpenShift technology from the public cloud to edge computing.

  - In the first phase, human-entered incident reports are ingested into OCI Object Storage, where OCI Functions and Llama3 generate concise summaries for maintenance teams. These are then mapped and pushed into IBM Maximo’s Events Management via REST API.

  - In the second phase, real-time aircraft telemetry data is streamed through ThingsBoard and analyzed using OCI’s MSET2 for anomaly detection. Identified anomalies are auto-logged into Maximo Incidents and correlated with human-entered Events Management from above.

  - Lastly, an integrated Oracle Analytics Cloud dashboard provides unified visualization of both user-reported events and telemetry-triggered incidents, alongside financial and operational impact analyses

<p align="center">
  <img src="Demo-Content/Images/Demo_Architecture_Overview.png" alt="Architecture Diagram" width="900"/>
</p>

This repository consists of material for 2 separate demos, each focsuing on **AI-Powered Intelligent Maintenance**.
## Demo # 1 (Agentic Incident Report) Abstract
This workflow streamlines operations by transforming unstructured event reports into concise, actionable summaries using AI, enabling faster incident analysis and response. It reduces manual effort and ensures consistent, enterprise-wide asset management through automated data processing and system integration

This demo ingests unstructured, text-based event reports using Object Storage and triggers OCI Events to initiate processing. OCI Functions handle data cleansing and formatting, then invoke a Generative AI model (LLM) to summarize key incident details for easier analysis. The structured summaries are published via OCI Streaming and consumed by an orchestrator, which ensures reliable delivery to the enterprise asset management system. This automated pipeline reduces manual effort, accelerates response times, and standardizes incident reporting across the organization.

![Demo #1 Architecture Diagram](Demo-Content/Images/Demo%#1%Architecture%Overview.png)

## Demo #2 (Agentic Anomaly Detection) Abstract
This workflow enables early detection of equipment anomalies through automated analysis of real-time telemetry data, reducing unplanned downtime and improving asset reliability. Detected issues are automatically logged as incidents, streamlining operational response and minimizing manual intervention. Integrated reporting combines system-generated alerts with user-submitted data to provide actionable insights for maintenance and engineering teams.

This demo illustrates how automated signal anomaly detection improves operational efficiency by proactively identifying equipment issues using OCI’s MSET2 engine and streaming IoT telemetry. By seamlessly integrating anomaly alerts into IBM Maximo through OCI services, the workflow eliminates manual data entry, accelerates incident response, and reduces downtime. The added analytics layer in Oracle Analytics Cloud enables real-time insights and strategic decision-making across engineering and maintenance teams.

![Demo #2 Architecture Diagram](Demo-Content/Images/Demo%#2%Architecture%Overview.png)
