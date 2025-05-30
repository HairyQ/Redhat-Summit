# Step 6: IBM Maximo Data Configuration
IBM Maximo is an enterprise asset management platform that helps organizations track, manage, and maintain physical assets across their lifecycle.

In this demo, Maximo Events Management module serves as the endpoint where anomalous occurrences are automatically logged as structured records (via DB Trigger in the SAM Databsae), enabling streamlined maintenance workflows and faster response to operational issues. 


IBM Maximo log in information will be provided by the IBM team when a demo instance is launched. Note, it is likely that the domains are not publicly registered, so you will need to add the IP/Domains to your local hosts file in order to access the UI. These details will be provided by the IBM team.

For this demo, we will be mapping a simple JSON Payload to IBM Maximo Incidents module. Due to limitations in the data, this payload will be almost exclusively static data, except for a field mapping to the MSN IDs we inputted into Maximo in the previous demo. These MSN IDs will be pulled from a table mapped to the Data Source ID that SAM generated when data was streamed in.

Certain data elements in Maximo are reference data fields or controlled values, and must be pre-inputted into Maximo. This section will demonstrate how to do that.

## Failure Codes
This will describe how to create new Failure Codes in IBM Maximo in order to create a new Incident when SAM detects an anomaly.

Step-by-Step Walkthrough:
1. Log into IBM Maximo and find the Search tab in the top left 
2. Search for 'Failure Codes' and click on 'Failure Codes'
3. Click 'New Failure Code' on the left menu labeled 'Common Actions'
4. In the 'Failure Class' field, enter 'ANOM-ENG'
5. In the description field to the right of that, enter 'Signal Anomaly - Turbine Engine'
6. Click the Save button in the top right
7. Repeat the process for the following Failure Codes

   - 'ANOM-NAV' / 'Signal Anomaly - Navigation'
   - 'ANOM-FUE' / 'Signal Anomaly - Fuel'
   - 'ANOM-AUT' / 'Signal Anomaly - Autoflight System'
  

