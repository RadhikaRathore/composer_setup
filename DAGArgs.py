from datetime import timedelta, datetime
import json
import urllib.parse
import constants

class DAGArgs():

    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2018, 10, 10),
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
        'execution_timeout': timedelta(hours=5),
        

    }

    def __init__(self, *args, **kwargs):
        print("in DAGARGS")

    def get_body(self,job_name, bucket_name, temp_location, zone):
        body = {
            "jobName": "{jobname}".format(jobname=job_name)+constants.jobname_postfix,
            "environment": {
                "tempLocation": temp_location.format(bucket=bucket_name),
                "zone": zone
            }
        }
        return body

    def get_daily_trigger_dataflow_body(self, job_name, bucket_name, temp_location, zone, input_data, input_param_name):
        body = {
            "jobName": "{jobname}".format(jobname=job_name)+constants.jobname_postfix,
            "parameters": {
                input_param_name: urllib.parse.quote_plus(json.dumps(input_data))
            },
            "environment": {
                "tempLocation": temp_location.format(bucket=bucket_name),
                "zone": zone
            }
        }
        return body
