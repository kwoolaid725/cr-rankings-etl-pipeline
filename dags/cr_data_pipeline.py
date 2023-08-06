from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.models import DAG, Variable

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from airflow.providers.postgres.operators.postgres import PostgresOperator

from airflow.utils.dates import days_ago


default_args = {
    'owner': 'wookim',
    'retries': 1,
    'depends_on_past': False,
    'start_date': datetime.now(),
    'retry_delay': timedelta(minutes=1),
}

with DAG('cr_data_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         description='CR data ingestion pipeline',
         catchup=False,
         ) as dag:

    # start = DummyOperator(task_id='start')
    test = BashOperator(
        task_id='test',
        bash_command='python /opt/airflow/scripts/test.py',
        dag=dag
    )
    # scrape = BashOperator(
    #     task_id='scrape',
    #     bash_command='python /opt/airflow/scripts/cr_webscraper.py',
    #     dag=dag
    # )

    webscraper = BashOperator(
        task_id='cr_webscraper',
        bash_command='python /opt/airflow/scripts/cr_webscraper.py',
        dag=dag
    )


    test >> webscraper # >> upload_to_s3 >> create_table >> copy_to_redshift >> end

