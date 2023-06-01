from airflow import models
from airflow.operators import python_operator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
import logging
def greeting():
    logging.info('Bonjour le monde depuis le DAG 1')

with models.DAG(
    'dag_1',
    schedule_interval = '*/1 * * * *', #chaque minute
    start_date=days_ago(0),
    catchup=False) as dag:
    
    hello_python = python_operator.PythonOperator(
        task_id='bonjour',
        python_callable=greeting)
    
    goodbye_dummy = DummyOperator(task_id='au_revoir')

    hello_python >> goodbye_dummy

