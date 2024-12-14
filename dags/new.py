from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time

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
    'learning_dag',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # Task to print the current date
    print_date = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    # Python function to sleep for a few seconds
    def sleep_function(seconds):
        time.sleep(seconds)
        print(f"Slept for {seconds} seconds")

    # Task to sleep for 5 seconds
    sleep_task = PythonOperator(
        task_id='sleep_task',
        python_callable=sleep_function,
        op_args=[5],
    )

    # Task to print a message
    print_message = BashOperator(
        task_id='print_message',
        bash_command='echo "Learning Airflow is fun!"',
    )

    # Define the task dependencies
    print_date >> sleep_task >> print_message
