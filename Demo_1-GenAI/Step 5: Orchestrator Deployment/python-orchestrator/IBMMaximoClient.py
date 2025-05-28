import requests
import json

# URL of the server endpoint
IBM_MAXIMO_URL = "https://masdev.manage.masinst.apps.ocimas.demo.com/maximo/api/os/plusamxevent?lean=1"
IBM_MAXIMO_API_KEY = "ddcq6kk0m65lkp63qlsdlg67m5vfmo44v0grf6m3"

# Optional headers, especially if authentication or content-type is required
headers = {
    "Content-Type": "application/json",
    "apikey" : IBM_MAXIMO_API_KEY
}

class IBMMaximoClient:
    def send_message(self, json_payload):
        try:
            # Make the POST request
            response = requests.post(IBM_MAXIMO_URL, headers=headers, json=json_payload, verify=False)
            # Handle response
            if response.status_code in [200, 201]:
                print("Ticket created successfully. Status code: " + str(response.status_code))
            else:
                print(f"Failed to create ticket: {response.status_code}")
        
        except Exception as e:
            print(f"An error occurred: {e}")
