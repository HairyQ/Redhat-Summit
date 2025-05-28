from base64 import b64encode
import oci
import uuid
import json
from oci.auth import signers
import logging

OCI_STREAMING_ENDPOINT = "default-endpoint"

class OCIStreamingClient:
    def __init__(self, stream_endpoint=OCI_STREAMING_ENDPOINT):
        signer_a = signers.get_resource_principals_signer()
        self.streaming_client = oci.streaming.StreamClient(config={}, signer=signer_a, service_endpoint=stream_endpoint)

    def send_message(self, text_message, stream_ocid):
        unique_id = str(uuid.uuid4())
        encoded_key = b64encode(unique_id.encode()).decode()
        encoded_value = b64encode(json.dumps(text_message).encode()).decode()
        message = oci.streaming.models.PutMessagesDetailsEntry(key=encoded_key, value=encoded_value)
        messages = oci.streaming.models.PutMessagesDetails(messages=[message])
        response =  self.streaming_client.put_messages(stream_ocid, messages)
        print("Written to stream : "+ unique_id)

        return response