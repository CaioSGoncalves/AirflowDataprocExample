from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.models import Variable

from datetime import datetime, timedelta


default_args = {
    'start_date': datetime(2020, 5, 9, 22) # datetime(2020, 5, 1),
}

# infra_api_url = Variable.get("infra_api_url")

dag = DAG(
    'submit_dag', default_args=default_args, schedule_interval="@hourly")

t1 = SimpleHttpOperator(
    task_id='submit_job',
    method='POST',
    http_conn_id='http_default',
    endpoint='/job',
    headers={"Content-Type": "application/json"},
    dag=dag)