import io
import json
import logging
import csv
import oci  # Make sure your function has the OCI SDK available
import OCIOrchestrator

BUCKET_NAME = "maximo-data"
CSV_FILE_NAME_PREFIX = "ASRS_"

def handler(ctx, data: io.BytesIO = None):
    logger = logging.getLogger()
    logger.info(f"Function invoked")
    try:
        payload = data.read()
        payload_str = payload.decode('utf-8')
        event_data = json.loads(payload_str)

        if isinstance(event_data, dict):
            event_data = [event_data]

        for event in event_data:
            object_name = event['data']['resourceName']
            bucket_name = event['data']['additionalDetails']['bucketName']
            namespace = event['data']['additionalDetails']['namespace']

            logger.info(f"New object created: {object_name}")
            logger.info(f"Bucket: {bucket_name}, Namespace: {namespace}")

            if object_name.startswith(CSV_FILE_NAME_PREFIX) and object_name.endswith(".csv"):
                logger.info("CSV matched filter. Reading...")
                read_csv(namespace, bucket_name, object_name, logger)

        return {"status": "success"}

    except Exception as e:
        logger.error(f"Exception: {e}")
        return {"status": "error", "message": str(e)}


def read_csv(namespace, bucket_name, object_name, logger):
    try:
        logger = logging.getLogger()        
        logger.info("Calling task orchestrator")
        reader = OCIOrchestrator.OCIOrchestrator(bucket_name, logger)
        reader.process_csv_file(object_name)            

    except Exception as e:
        logger.error(f"Failed to read CSV: {e}")

