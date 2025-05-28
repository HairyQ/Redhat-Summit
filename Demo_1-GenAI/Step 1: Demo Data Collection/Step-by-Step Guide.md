### 1a. Download New Data
1. Navigate to NASA ASRS Database to download data.
    - LINK: https://akama.arc.nasa.gov/ASRSDBOnline/QueryWizard_Filter.aspx
2. Select appropriate filters 
    - Date Range: Jan 2014 - Dec 2024
    - Make/Model: All Airbus models
    - Mission: Passenger
3. Click Run Search > Export Excel File
### 1b. Transform and Supplement Data
1. Transform date variable to desired format
2. Consolidate Parent and Child Headers into single row
3. Remove empty rows (particularly Row 3)
4. Add 'MSNID' Variable
      - This will act as a dummy unique identifier (Manufacturer Serial Number) for the aircraft associated with each event.
      - Ensure that each MSNID is only associated with a single 'Make Model Name' for consistency purposes.
### ALTERNATIVE: Access Existing Data Files
Navigate to [Demo_1-GenAI/Demo_Data](https://github.com/HairyQ/Redhat-Summit/tree/main/Demo_1-GenAI/Demo_Data) to access existing data downloads
   - Subset of dataset to be uploaded for live demo (4 records)
       - https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Demo_Data/ASRS_New_Data.csv
   - Sample CSV output of subset
       - https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Demo_Data/ASRS_New_Data_Sample-Output.csv
   - Sample of Doc version of subset
       - https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Demo_Data/ASRS_Document_Example.docx
   - Additional data for training or exploratory purposes (4,000+ records)
       - https://github.com/HairyQ/Redhat-Summit/blob/main/Demo_1-GenAI/Demo_Data/ASRS_Additional_Data.xlsx

