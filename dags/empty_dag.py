import datetime
from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

@dag(start_date=datetime.datetime(2025, 1, 1), schedule="@daily")
def generate_dag():
    EmptyOperator(task_id="empty_operator")

generate_dag()