from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_current_date():
    print(f"Current date: {datetime.now()}")

# Define default_args
default_args = {
    'owner': 'airflow',
    'retries': 1,
}

# Define the DAG
with DAG(
    'simple_dag0',
    default_args=default_args,
    description='A simple Airflow DAG',
    schedule_interval=None,  # Run only when triggered manually
    start_date=datetime(2024, 12, 14),
    catchup=False,
) as dag:
    task = PythonOperator(
        task_id='print_current_date',
        python_callable=print_current_date,
    )
