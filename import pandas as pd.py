import pandas as pd
from google.cloud import bigquery

# Load data (already cleaned in Pandas step)
df = pd.read_csv("medical_insurance.csv")

# Standardize columns (safety)
df.columns = df.columns.str.lower().str.strip()

# BigQuery details
PROJECT_ID = "medical-insurance-project"
DATASET_ID = "medical-insurance-project.medical_insurance"
TABLE_ID = "medical-insurance-project.medical_insurance.medical_insurance_raw"

table_ref = f"{medical-insurance-project}.{medical-insurance-project.medical_insurance}.{medical-insurance-project.medical_insurance.medical_insurance_raw}"

# BigQuery client
client = bigquery.Client(project=medical-insurance-project)

# Load job configuration
job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE",  # overwrite for now
    autodetect=True
)

# Load dataframe to BigQuery
job = client.load_table_from_dataframe(
    df,
    table_ref,
    job_config=job_config
)

job.result()  # Wait for job to complete

print("✅ Data successfully loaded to BigQuery")
