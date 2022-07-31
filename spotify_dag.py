from datetime import timedelta
from email.policy import default
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from spotify_project import run_spotify_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 5, 28),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1) #try in the difference of 1 min
}

dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

#def dummy_function():
#    print("Hello World")

run_etl = PythonOperator(
    task_id='whole_spotify_etl',
    python_callable=run_spotify_etl,
    dag=dag,
)

run_etl
