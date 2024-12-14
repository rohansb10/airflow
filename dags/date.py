from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG('date_dag', default_args=default_args, schedule_interval='@daily') as dag:
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

