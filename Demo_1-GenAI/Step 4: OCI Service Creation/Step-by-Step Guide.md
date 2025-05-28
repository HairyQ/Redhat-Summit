# Step 4: OCI Service Creation (Events, Functions, Streaming, etc.)
This step will deploy OCI Services needed to complete the data flow from our raw data, calling Llama APIs, and pushing to OCI Streaming.
## OCI Object Storage Deployment
This Object Storage bucket will be used to host our demo data.
## OCI Events Deployment
This OCI Event will be used to monitor new uploads to our Object Storage bucket and call an OCI Function.
## OCI Functions Deployment
This OCI Function, called by our Event, will use Python to curate the data, create our JSON payload, and call the Llama API to run a prompt to summarize our data narratives. Lastly, it will push the JSON payload to OCI Streaming. 
## OCI Streaming Deployment
This OCI Stream will push the JSON payloads to be consumed by our Orchestrator node and posted to IBM Maximo via REST API.
