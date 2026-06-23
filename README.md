# Zipco Food ETL Pipeline

An end-to-end ETL pipeline that extracts raw food transaction data, transforms and normalises it into a star schema, and loads it into Azure Blob Storage — orchestrated with Apache Airflow.

---

## Project Overview

This project simulates a real-world data engineering workflow for a fictional food business, Zipco. Raw transaction data is processed through a three-stage pipeline: extraction, transformation, and loading into cloud storage — fully automated and monitored via Apache Airflow.

---

## Architecture

```
Raw CSV Data
     │
     ▼
┌─────────────────┐
│ Extraction Layer │  ← Reads zipco_transaction.csv
└────────┬────────┘
         │
         ▼
┌──────────────────────┐
│ Transformation Layer  │  ← Cleans data, normalises into star schema
└────────┬─────────────┘
         │
         ▼
┌─────────────────┐
│  Loading Layer   │  ← Uploads to Azure Blob Storage
└─────────────────┘
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Apache Airflow 3 | Pipeline orchestration |
| Python 3.14 | ETL scripting |
| Pandas | Data transformation |
| Azure Blob Storage | Cloud data lake destination |
| WSL Ubuntu | Development environment |
| GitHub | Version control |

---

## Project Structure

```
zipco_food_dag/
├── dag_script.py             # Airflow DAG definition
├── Extraction.py             # Extract logic
├── Transformation.py         # Transform and normalise logic
├── Loading.py                # Azure Blob Storage upload logic
├── zipco_transaction.csv     # Source transaction data
├── screenshots/              # Pipeline and Azure evidence
└── README.md
```

---

## ipeline Stages

### 1. Extraction Layer
Reads the raw `zipco_transaction.csv` file containing Zipco food transaction records into a Pandas DataFrame for processing.

### 2. Transformation Layer
Cleans and normalises the raw data:
- Removes duplicate records
- Fills missing numeric values with column mean
- Fills missing string values with 'Unknown'
- Normalises into a **star schema** with 5 tables:

| Table | Description |
|-------|-------------|
| `products.csv` | Unique products with pricing |
| `customers.csv` | Unique customer records |
| `staff.csv` | Unique staff records |
| `transactions.csv` | Fact table with foreign keys |
| `clean_data.csv` | Full cleaned dataset |

### 3. Loading Layer
Uploads all normalised tables to **Azure Blob Storage** (`zipcofoodscontainer`) using the Azure SDK:
- `cleaneddata/` — normalised dimension and fact tables
- `rawdata/` — full cleaned dataset

---

## Azure Blob Storage Output

All files successfully uploaded to `zipcofoodscontainer`:

```
zipcofoodscontainer/
├── rawdata/
│   └── cleaned_zipco_transaction_data.csv
└── cleaneddata/
    ├── customers.csv    (102 KB)
    ├── products.csv     (36 KB)
    ├── staff.csv        (38 KB)
    └── transactions.csv (134 KB)
```

---

## How to Run

### Prerequisites
- WSL Ubuntu
- Python 3.14
- Apache Airflow 3
- Azure Storage account

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Emmachi4life/Zipco_food_Etl_case_study_using_Apache_Airflow_for-_orchestration.git
```

2. Create and activate a virtual environment:
```bash
python3 -m venv zipcovenv
source zipcovenv/bin/activate
```

3. Install dependencies:
```bash
pip install apache-airflow pandas azure-storage-blob python-dotenv
```

4. Copy DAG files to Airflow dags folder:
```bash
cp *.py ~/airflow/dags/
```

5. Create a `.env` file with your Azure credentials:
```
AZURE_STORAGE_CONNECTION_STRING=your_connection_string_here
CONTAINER_NAME=your_container_name_here
```

6. Start Airflow:
```bash
airflow standalone
```

7. Open `http://localhost:8080`, log in, and trigger `real_zipco_dag`.

---

## ipeline Results

All three tasks completed successfully in under 10 seconds:

| Task | Status | Duration |
|------|--------|----------|
| extraction_layer | ✅ Success | ~1.8s |
| transformation_layer | ✅ Success | ~1.8s |
| loading_layer | ✅ Success | ~6.3s |

---

## Security Notes

- The `.env` file containing Azure credentials is excluded from version control via `.gitignore`
- Rotate your Azure Storage access keys regularly

---

## Author

**Emmanuel Uzokwe**  
Data Engineer | BI Specialist | Data Specialist 
📧 euzokwe1904@gmail.com  
🔗 [LinkedIn](www.linkedin.com/in/emmanueluzokwe19)

---

This project is for portfolio and educational purposes.