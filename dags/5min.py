from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    '5min_dags',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='*/5 * * * *',  # Run every 5 minutes
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # Define tasks
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        bash_command='sleep 5',
    )

    t3 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello, Airflow!"',
    )

    # Define task dependencies
    t1 >> t2 >> t3
