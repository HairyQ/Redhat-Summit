# Step 5: Orchestrator Deployment
This step will describe how to deploy the Python-based Orchestrator node in a standalone OCI Compute VM. This orchestrator will consume the streams from OCI streaming and post the JSON payloads to IBM Maximo via REST API.

1. Copy the all files from python-orchestrator to a folder on compute VM.
2. Open IBMMaximoClient.py and edit following parameters.
- IBM_MAXIMO_URL: URL of IBM Maximo.
- IBM_MAXIMO_API_KEY: IBM Maximo API key.
3. Open OCIStreamingClient.py and edit following parameters.
- OCI_STREAMING_ENDPOINT: OCI Message endpoint.
- OCI_STREAM_OCID: OCI Streaming OCID.
4. Start stream consumer. 
- ./start-consumer.sh


