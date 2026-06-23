from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from Extraction import extraction # here we import  the function from our etl script
from Transformation import transformation
from Loading import loading



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026,6,23),
    'email': 'euzokwe1904@gmail.com',
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retries_delay': timedelta(minutes=1)
}

dag = DAG(
    'real_zipco_dag',
    default_args=default_args,
    description='Zipco batch etl pipeline'
)

extraction = PythonOperator(
    task_id='extraction_layer',
    python_callable=extraction,
    dag=dag,
)

transformation = PythonOperator(
    task_id='transformation_layer',
    python_callable=transformation,
    dag=dag,
)

loading = PythonOperator(
    task_id='loading_layer',
    python_callable=loading,
    dag=dag,
)

extraction >> transformation >> loading