
CREATE OR REPLACE PROCEDURE call_maximo_api_procedure(p_data_source_id NUMBER) AS
  l_msn_id     VARCHAR2(100);
  l_report_date VARCHAR2(100);
  json_payload CLOB;
  req          UTL_HTTP.req;
  resp         UTL_HTTP.resp;
BEGIN
  SELECT msn_id
  INTO l_msn_id
  FROM msn_data
  WHERE data_source_id = p_data_source_id;
  
  l_report_date := TO_CHAR(SYSTIMESTAMP AT TIME ZONE 'UTC', 'YYYY-MM-DD"T"HH24:MI:SS') || '+00:00';

  json_payload := '{
    "assetnum": "' || l_msn_id || '",
    "description": "Signal Anomaly - Turbine Engine",
    "failurecode": "ANOM-ENG",
    "reportdate": "' || l_report_date || '",
    "reportedby": "SAM-AGENT",
    "status": "QUEUED",
    "siteid": "AVIATION",
    "historyflag": false,
    "assetorgid": "EAGLE",
    "assetsiteid": "AVIATION"
  }';

  req := UTL_HTTP.begin_request('https://nginx.nginx-rhdemo.online', 'POST', 'HTTP/1.1');
  UTL_HTTP.set_header(req, 'Content-Type', 'application/json');
  UTL_HTTP.set_header(req, 'Content-Length', LENGTH(json_payload));
  UTL_HTTP.set_header(req, 'apikey', 'ddcq6kk0m65lkp63qlsdlg67m5vfmo44v0grf6m3');
  UTL_HTTP.write_text(req, json_payload);
  resp := UTL_HTTP.get_response(req);
  UTL_HTTP.end_response(resp);

 EXCEPTION
 WHEN OTHERS THEN
      NULL; -- Suppress all errors for demo (optional: add logging)
END;
/

CREATE OR REPLACE TRIGGER MAX_API_TRIGGER
AFTER UPDATE OF job_status ON anomaly_detection_jobs 
FOR EACH ROW 
WHEN (
    NEW.job_status = 'COMPLETED'
    AND NEW.anomalous_columns != '[]'
)
BEGIN
 BEGIN
    call_maximo_api_procedure(:NEW.data_source_id);  -- Pass value directly
 EXCEPTION
 WHEN OTHERS THEN
  NULL; -- or log
 END;
END;
/
