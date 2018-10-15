import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import logging
import constants
from datetime import timedelta, datetime
from DAGArgs import DAGArgs



def print_hello():
    print(["hello"])
    logging.info(["in hello"])
    return 'Hello world!'


try:
    with DAG(
        'test',
        default_args=DAGArgs().default_args,
        description='DAG to to trigger hello_world.',
        max_active_runs=1,
        concurrency=4,
        #catchup = False,
        schedule_interval='30 08 * * *',
        ) as dag:
            task1 = PythonOperator(
                    task_id='print_hello-test',
                    python_callable=print_hello,
                    dag = dag)

except IndexError as ex:
    logging.debug("Exception",str(ex))

task1
