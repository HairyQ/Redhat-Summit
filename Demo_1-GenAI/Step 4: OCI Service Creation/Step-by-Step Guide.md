# Step 4: OCI Service Creation (Events, Functions, Streaming, etc.)
This step will deploy OCI Services needed to complete the data flow from our raw data, calling Llama APIs, and pushing to OCI Streaming.

## OCI Object Storage Deployment
This Object Storage bucket will be used to host our demo data. 

1. Create a new bucket named 'maximo-data'. 
2. Go to Object Storage -> Bucket Details -> Bucket Information and enable 'Emit Object Events:'. This is required for the function to get invoked when a new object is uploaded to bucket.

## OCI Streaming Deployment
This OCI Stream will push the JSON payloads to be consumed by our Orchestrator node and posted to IBM Maximo via REST API.

1. Create a new stream. OCI Console -> Streaming -> Create Stream (name: flight-messages)
2. Go to Stream Information and note down 'Messages Endpoint' and 'OCID'

## OCI Functions Deployment
This OCI Function, called by our Event, will use Python to curate the data, create our JSON payload, and call the Llama API to run a prompt to summarize our data narratives. Lastly, it will push the JSON payload to OCI Streaming.

Follow the OCI tutorial to create OCI application (flight-app) and functions (task-orchestrator).
https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartcloudshell.htm

Replace all files with files in the oci-function directory. Following are the configurations in the functions.

1. Edit func.py to update bucket name and filename prefix.
- BUCKET_NAME: Bucket to monitor for incoming files
- CSV_FILE_NAME_PREFIX: This is the file name prefix for monitoring files. Files will be processed only 

2. Edit OCIAIClient.py to update LLM endpoint.
- LLM_ENDPOINT: LLM endpoint for generating summary and title.

3. Edit OCIOrchestrator.py to update below parameters.
- COMPARTMENT_ID: Compartment where all OCI resources are hosted.
- OCI_STREAMING_ENDPOINT: OCI streaming messages endpoint.
- OCI_STREAM_OCID: OCI Streaming OCID.

## OCI Events Deployment
This OCI Event will be used to monitor new uploads to our Object Storage bucket and call an OCI Function.

1. Go to Observability & Management, Event Service, Rules
2. Click Create Rule 
3. Select Condition as EventType, Service Name as Object Storage and Event Type as Object - Create
4. Click Another Condition
5. Select Condition as Attribute, Attribute Name as bucketName and Attribute Values as maximo-data
6. On Actions, Select Action Type as Functions
7. Select function compartment
8. Select Function Applicaiton (flightapp) and function (task-orchestrator)
9. Click Create Rule