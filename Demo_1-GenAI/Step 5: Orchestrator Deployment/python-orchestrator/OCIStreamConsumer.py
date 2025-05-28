import json
import IBMMaximoClient
import oci
import os
import time
from base64 import b64decode
import re

PROCESSED_KEYS_FILE = 'processed_keys.txt'
OCI_STREAMING_ENDPOINT = "https://cell-1.streaming.us-ashburn-1.oci.oraclecloud.com"
OCI_STREAM_OCID="ocid1.stream.oc1.iad.amaaaaaahtyn6pya75xlrsgjmygj743gysvwraxa6g7kw2xv7aaobngojbbq"

maximo_client = IBMMaximoClient.IBMMaximoClient()

# Load processed keys
if os.path.exists(PROCESSED_KEYS_FILE):
    with open(PROCESSED_KEYS_FILE, 'r') as f:
        processed_keys = set(line.strip() for line in f if line.strip())
else:
    processed_keys = set()

def save_processed_key(key):
    with open(PROCESSED_KEYS_FILE, 'a') as f:
        f.write(f"{key}\n")
    processed_keys.add(key)

# Function to consume messages from the stream (wait mode)
def consume_message_wait(client, stream_id, cursor):

    try:
        while True:
            get_response = client.get_messages(stream_id, cursor, limit=1)

            for message in get_response.data:
                raw_key = b64decode(message.key).decode() if message.key else None
                raw_value = b64decode(message.value).decode()

                if raw_key in processed_keys:
                    print(f"Skipping already processed key: {raw_key}")
                else:
                    print(f"\nConsumed: {raw_key}")
                    #print("Doc : " + json.dumps(raw_value, indent=2))

                    # Call API and pass the payload
                    call_maximo_api(raw_value)

                    # Do not process the same key again
                    save_processed_key(raw_key)

            cursor = get_response.headers.get("opc-next-cursor")
            time.sleep(.1)
    except KeyboardInterrupt:
        print("\nStopped watching stream.")

def call_maximo_api(payload):
    try:
        json_object = json.loads(payload)
        print("Parsed JSON:", json.dumps(json_object, indent=2))
        maximo_client.send_message(json_object)        
    except json.JSONDecodeError as e:
        print(f"\n\n ->>>Error: {e}")
        print("Raw JSON string:")
        print(payload)


# Set up the Streaming Client
config = oci.config.from_file()
client = oci.streaming.StreamClient(config, service_endpoint=OCI_STREAMING_ENDPOINT)

# Create a cursor (start from beginning or use LATEST if preferred)
cursor_details = oci.streaming.models.CreateCursorDetails(
    partition="0",
    type=oci.streaming.models.CreateCursorDetails.TYPE_TRIM_HORIZON  # or TYPE_LATEST
)
cursor_response = client.create_cursor(OCI_STREAM_OCID, cursor_details)
cursor = cursor_response.data.value

# Start consuming
print(f"Starting to consume messages from stream")
consume_message_wait(client, OCI_STREAM_OCID, cursor)