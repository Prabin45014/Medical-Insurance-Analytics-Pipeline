import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Load data
df = pd.read_csv("medical_insurance.csv")
df.columns = df.columns.str.lower().str.strip()

# BigQuery identifiers
PROJECT_ID = "medical-insurance-project"
DATASET_ID = "medical_insurance"
TABLE_ID = "medical_insurance_raw"

table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

# Explicit credentials (SAFE)
KEY_PATH = r"E:\Project\keys\bq_service_account.json"

credentials = service_account.Credentials.from_service_account_file(
    KEY_PATH
)

client = bigquery.Client(
    project=PROJECT_ID,
    credentials=credentials
)

job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE",
    autodetect=True
)

job = client.load_table_from_dataframe(
    df,
    table_ref,
    job_config=job_config
)

job.result()

print("✅ Data successfully loaded to BigQuery")
