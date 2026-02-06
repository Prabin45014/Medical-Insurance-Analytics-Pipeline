### **Medical Insurance Analytics Engineering Pipeline**



###### **📌 Project Overview**



This project showcases an end-to-end analytics engineering pipeline using **BigQuery, dbt**, **and Looker Studio**, with data sourced from **Kaggle**.



Medical insurance data is extracted from Kaggle using the **Kaggle API and Python**, explored and validated with **Pandas**, and then uploaded to **BigQuery** as raw data. Using **dbt**, the raw data is transformed into clean, analytics-ready tables. Finally, the data is visualized through interactive dashboards in **Looker Studio**.



###### **Project Architecture \& Workflow** 

**Architecture**

**┌─────────────┐       ┌───────────────┐       ┌──────────────┐**

**│  Data Source│──────▶│ Data Extraction│──────▶│ Local Storage│**

**│  (Kaggle)   │       │  (Python)     │       │  CSV/Files   │**

**└─────────────┘       └───────────────┘       └──────────────┘**

                                                            **│**

                                                            **▼**

                                                  **┌──────────────────┐**

                                                  **│ BigQuery (Raw DB)│**

                                                  **└──────────────────┘**

                                                            **│**

                                                            **▼**

                                                  **┌──────────────────┐**

                                                  **│ dbt Transformations│**

                                                  **│ (Staging \& Marts) │**

                                                  **└──────────────────┘**

                                                            **│**

                                                            **▼**

                                                  **┌──────────────────┐**

                                                  **│ Looker Studio     │**

                                                  **│ Interactive Dash │**

                                                  **└──────────────────┘**



**Workflow Diagram**



**Kaggle Dataset**

      **↓** (Kaggle API)

**Python**

      **↓**

**Pandas** (EDA \& validation)

      **↓**

**Local CSV File**

      **↓** (Manual Upload)

**BigQuery** (RAW)

      **↓**

**dbt** (Staging \& Marts)

      **↓**

**BigQuery** (Analytics)

      **↓**

**Looker Studio** (Dashboards)


**⚡ Tech Stack**
---

* **Kaggle API** - Programmatic dataset extraction
* **Python** – Orchestrating data extraction and preprocessing
* **Pandas** – Data exploration, validation, and preprocessing
* **Google BigQuery** – Cloud-based data warehouse for raw and analytics-ready datasets
* **dbt (Data Build Tool)** – SQL-based transformations, staging \& mart modeling, data quality tests, and documentation
* **Looker Studio** – Interactive dashboards built directly on BigQuery analytics tables
* **SQL** – Data transformation, aggregation, and analytics logic
* **Git \& GitHub** – Source control and project documentation
* 

**✅ Key Features**
---

* Programmatic data extraction from Kaggle using Python API
* Data exploration and validation using Pandas
* Raw data storage in BigQuery following warehouse best practices
* Analytics engineering using dbt (staging \& mart layers)
* Modular and reusable SQL-based transformations
* Built-in data quality tests with dbt
* Clear separation of RAW, STAGING, and MART layers
* Interactive Looker Studio dashboards with live BigQuery connection
* Scalable and production-style analytics architecture



###### **📂 Repository Structure**



**insurance\_analytics/**

**│**

**├── models/**

**│   ├── sources.yml**                 

**│   │**

**│   ├── staging/**

**│   │   └── stg\_medical\_insurance.sql**   

**│   │**

**│   ├── marts/**

**│   │   ├── insurance\_metrics.sql**      

**│   │   ├── risk\_metrics.sql**           

**│   │   └── age\_metrics.sql**           

**│   │**

**│   └── schema.yml**                  

**│**

**├── dbt\_project.yml**                 

**├── profiles.yml**                   

**├── README.md**   

**|\_\_\_ .gitignore**

**|\_\_\_ import pandas as pd.py**

**|\_\_\_ medical insurance.ipynb**

**|\_\_\_ medical\_insurance.csv**

**|\_\_\_ pandas\_to\_bigquery.py
|**



###### **⚙️ Step-by-Step Implementation**

**1. Kaggle Dataset Access**

* Used Kaggle API to programmatically download the medical insurance dataset.
* Kaggle acts as the external data source for the project.



**2. Data Analysis with Pandas**

* Loaded Kaggle dataset into Pandas DataFrames.
* Performed basic data exploration, validation, and sanity checks.
* Identified relevant columns for analytics and reporting.
* Saved the processed dataset to the local file system.



**3. BigQuery Raw Data Setup**

* Created project, dataset and tables in Google BigQuery.
* Manually uploaded the local CSV file into BigQuery.
* BigQuery acts as the central data warehouse (RAW layer).



**4. dbt Project Setup**

* Initialized a dbt project connected to BigQuery.
* Configured profiles and service account authentication.
* Defined BigQuery raw tables as dbt sources.



**5. dbt Transformations**

* Built staging models to clean and standardize raw data.
* Created analytics mart models aligned with dashboard requirements.
* Implemented dbt tests to ensure data quality and consistency.
* Generated dbt documentation for model lineage and metadata.



**6. Looker Studio Dashboards**

* Connected Looker Studio directly to BigQuery analytics tables.
* Built interactive dashboards for:
* Regional cost analysis
* Risk segmentation
* Age group insights



**📊 Final Deliverables**

* End-to-end medical insurance analytics pipeline
* Kaggle dataset → external data source
* BigQuery raw tables → centralized data warehouse
* dbt staging \& mart models → clean and aggregated analytics data
* Interactive dashboards → Looker Studio





