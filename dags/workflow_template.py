from airflow import DAG
from airflow.models import Variable
from airflow.contrib.operators.dataproc_operator import DataprocWorkflowTemplateInstantiateOperator

from datetime import datetime, timedelta


default_args = {
    'start_date': datetime(2020, 5, 12) # datetime(2020, 5, 1),
}

dag = DAG(
    'workflow_template', default_args=default_args, schedule_interval="@once")

t1 = DataprocWorkflowTemplateInstantiateOperator(
    task_id="execute",
    gcp_conn_id='google_cloud_default',
    project_id='sincere-bongo-264115',
    region='southamerica-east1',
    template_id='example',
    dag=dag)