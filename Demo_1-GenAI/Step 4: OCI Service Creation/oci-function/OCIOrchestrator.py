from base64 import b64encode
import datetime
import OCIAIClient
import OCIStreamingClient
import oci
import json
import uuid
import csv
import json
import io
from oci.auth import signers

BUCKET_NAME = "maximo-data"

COMPARTMENT_ID="ocid1.compartment.oc1..aaaaaaaa5noas7excyco6l5cw4dosgyestcfe5xnzugktvwb6kn4ntlprg7q"
OCI_STREAMING_ENDPOINT = "https://cell-1.streaming.us-ashburn-1.oci.oraclecloud.com"
OCI_STREAM_OCID="ocid1.stream.oc1.iad.amaaaaaahtyn6pya75xlrsgjmygj743gysvwraxa6g7kw2xv7aaobngojbbq"
field_to_read_then_remove = "Narrative"

# Field mapping from CSV headers to JSON keys
field_mapping = {
    "Time_Date Time": "reportdate",
    "Aircraft 1_Make Model Name": "plusapart",
    "Component_Aircraft Component": "plusacomponent",
    #"Function": "owner",
    "Place_State Reference": "plusalocation",
    "Aircraft 1_Flight Phase": "plusaopregime",
    "Assessments_Primary Problem": "plusaeventtype",
    "Events_Anomaly": "plusarootcause",
    "Events_Result": "plusaeffectcode",
    "Failure Code_Failure Code": "failurecode",
    "Aircraft 1_MSN ID": "serialnum",
    #"historyflag": False,
    #"plusacategory": "plusacategory",
    #"status": "status",
    #"reported by": "reported by",
    "ACN" : "plusadelaytime",
    "Report 1_Narrative" : "Narrative"
}

class OCIOrchestrator:

    def __init__(self, bucket_name, logger):        
        self.bucket_name = bucket_name

        signer = oci.auth.signers.get_resource_principals_signer()
        self.client = oci.object_storage.ObjectStorageClient({}, signer=signer)
        self.namespace = self.client.get_namespace().data
        self.streaming_client = OCIStreamingClient.OCIStreamingClient(OCI_STREAMING_ENDPOINT)
        self.aiclient = OCIAIClient.OCIAIClient()
        self.logger = logger

    def read_csv(self, csv_file_name):
        # Read and decode the stream into a string
        obj = self.client.get_object(self.namespace, self.bucket_name, csv_file_name)
        content = obj.data.content.decode('utf-8')  
        csv_reader = csv.DictReader(io.StringIO(content))
        return csv_reader     

    def list_json_objects(self):
        """Lists all JSON objects in the specified bucket."""
        response = self.client.list_objects(self.namespace, self.bucket_name)
        return [obj.name for obj in response.data.objects if obj.name.endswith('.json')]
    
    def read_json_file(self, object_name):
        obj = self.client.get_object(self.namespace, self.bucket_name, object_name)
        content = obj.data.content.decode('utf-8')
        data = json.loads(content)
        return data.get("textcontent")        
   
    def send_text_to_stream(self, summary):
        return self.streaming_client.send_message(summary, OCI_STREAM_OCID)
    
    def process_csv_file(self, object_name):
        try:
            # Read json file from object storage
            print("Processing file from object storage : " + object_name)
            reader = self.read_csv(object_name)
            for row in reader:
                    json_row = {}
                    json_row["owner"] = "CAPTAIN"
                    json_row["reported by"] = "MAXADMIN"
                    json_row["status"] = "NEW"
                    json_row["historyflag"] = False
                    json_row["plusacategory"] = "BASIC"

                    json_row["assetsiteid"] = "AVIATION" #
                    json_row["assetorgid"] = "EAGLE"     #

                    for old_key, new_key in field_mapping.items():
                        value = row.get(old_key, "")
                        if new_key == field_to_read_then_remove:
                            self.process_each_record(json_row, row)

                        elif new_key == "plusaeventtype":
                            json_row[new_key] = value.upper()
                        elif new_key == "serialnum":
                            json_row["assetnum"] = value
                        elif new_key == "failurecode":
                            json_row["failurecode"] = value #
                        else:
                            json_row[new_key] = value
                    #break
        except Exception as e:
            print(f"\nError reading {object_name}: {str(e)}")

    def get_combined_string(self, row):
        combined_text=""
        for field in ["Report 1_Narrative", "Report 1_Callback", "Report 2_Narrative", "Report 2_Callback"]:
            value = row.get(field, "").strip()
            if value:
                combined_text += value     
        return combined_text   

    def process_each_record(self, json_row, row):
         
         # Summarize the text
         #narrative_text = self.get_combined_string(row)
         narrative = row.get("Report 1_Narrative", "").strip()
         summary = self.aiclient.get_summary(narrative)
         json_row["description_longdescription"] = summary
         json_row["description"] = self.aiclient.get_title(narrative)

         #print("\n Created json doc : " + json.dumps(json_row, indent=2))
         print("AI Generated summary: " + summary)

         # Put summary to OCI Streaming
         self.send_text_to_stream(json_row)
         self.logger.info("Json written to stream")


if __name__ == "__main__":
    print("Processing start")