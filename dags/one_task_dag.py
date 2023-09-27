'''One Task DAG '''
from datetime import datetime
from airflow.operators.bash import BashOperator
from airflow import DAG

default_args = {
    'owner': 'Jun',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'catchup': False,
    'start_date': datetime.now()
}

with DAG(
        dag_id='one_task_dag',
        description='A one task airflow DAG',
        schedule_interval=None,
        default_args=default_args

    ) as dag:
    
    task1 = BashOperator(
            task_id='one_task',
            bash_command='echo "hello, linkedin Learning!" > /Users/jun/PycharmProjects/airflow_docker/lab/temp/create_temp.txt',
            dag=dag
    )
