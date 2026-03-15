from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'anubhav',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'snowflake_data_pipeline_v2',
    default_args=default_args,
    description='Optimized data warehousing pipeline for AI analytics',
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:

    extract_raw = SnowflakeOperator(
        task_id='extract_raw_data',
        sql='CALL SP_EXTRACT_RAW_TELEMETRY();',
        snowflake_conn_id='snowflake_default'
    )

    run_dbt_transform = PythonOperator(
        task_id='run_dbt_transformations',
        python_callable=lambda: print("Executing dbt run: transforming raw to analytics layers...")
    )

    refresh_powerbi = PythonOperator(
        task_id='trigger_powerbi_refresh',
        python_callable=lambda: print("Triggering PowerBI REST API for dashboard refresh...")
    )

    extract_raw >> run_dbt_transform >> refresh_powerbi