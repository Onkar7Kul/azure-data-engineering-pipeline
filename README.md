Azure Data Engineering Pipeline (ADF + Databricks + PySpark + Delta Lake)
📌 Overview

This project demonstrates an end-to-end Azure Data Engineering pipeline built using Azure Data Factory, Azure Databricks, PySpark, Delta Lake, and Azure Data Lake Storage (ADLS).
It follows the Medallion Architecture (Bronze → Silver → Gold) and includes incremental data ingestion (CDC), metadata-driven pipelines, table optimization, and CI/CD deployment.

The goal is to showcase a production-grade Azure Lakehouse pipeline using real engineering patterns.

🏗 Architecture
Components Used

Azure Data Factory (ADF) – Orchestration, pipeline scheduling

Azure Databricks – Data processing, PySpark transformations

Delta Lake – Storage layer with ACID transactions

ADLS Gen2 – Raw/clean/curated data zones

Azure DevOps – CI/CD, version control

Azure Monitor + Log Analytics – Monitoring and logging

Architecture Diagram (High Level)
Source Systems (REST API / SQL DB / CSV)
              ↓
   Azure Data Factory (Orchestration)
              ↓
           ADLS Bronze
              ↓
   Azure Databricks (PySpark - Cleansing)
              ↓
           ADLS Silver
              ↓
   Delta Lake (CDC, MERGE, Optimizations)
              ↓
           ADLS Gold
              ↓
     Consumption Layer (SQL / Reporting)

🚀 Features Implemented
1. Multi-Source Ingestion

REST API ingestion (paginated + token-based auth)

CSV ingestion using ADF copy activity

SQL ingestion using ADF linked services + datasets

2. Metadata-Driven Framework

Central metadata table controlling:

Source type

File paths

Incremental/full mode

Target table mapping

ADF pipelines dynamically ingest new sources without manual changes

3. Medallion Architecture

Bronze: raw ingestion

Silver: cleansing, schema standardization

Gold: business-level curated tables

4. Incremental Load (CDC)

Implemented CDC using Delta Lake MERGE, supporting:

Upserts

Deletes

Schema evolution

Late-arriving data

5. Delta Table Optimization

OPTIMIZE

ZORDER on high-cardinality columns

Partition pruning

VACUUM for storage maintenance

6. CI/CD Integration

ADF JSON templates stored in Git repo

Databricks notebooks deployed via Azure DevOps pipelines

Automated release across Dev → QA → Prod

7. Monitoring

ADF pipeline run logs → Log Analytics

Custom KQL queries to analyze failures, retries, SLA breaches

🧪 Technologies Used
Category	Tools
Orchestration	Azure Data Factory
Processing	Azure Databricks, PySpark
Storage	ADLS Gen2, Delta Lake
Architecture	Medallion, CDC
CI/CD	Azure DevOps
Monitoring	Azure Monitor, Log Analytics


📂 Repository Structure
├── /adf/
│   ├── linkedServices
│   ├── datasets
│   ├── pipelines
├── /databricks/
│   ├── notebooks
│   ├── pyspark_jobs
├── /metadata/
│   ├── ingestion_rules.csv
├── /configs/
│   ├── parameters.json
└── README.md



Sample PySpark Code (CDC Merge)
df_new = spark.read.format("delta").load(silver_path)
df_old = spark.read.format("delta").load(gold_path)

(
    df_old.alias("t")
    .merge(
        df_new.alias("s"),
        "t.id = s.id"
    )
    .whenMatchedUpdateAll()
    .whenNotMatchedInsertAll()
    .execute()
)


✨ Key Outcomes

Automated ingestion for multiple data sources

Clean, maintainable Medallion architecture

Production-style CDC & Delta optimization

Full CI/CD setup for ADF + Databricks

End-to-end monitoring pipeline
