import pendulum

from airflow import Dataset
from airflow.decorators import dag, task
from airflow_core.shared_vars import CORE_PROJECT_ID


@dag(
    schedule="@daily",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["data_engineering", "ingestion"],
)
def ingestion_dag_a():
    @task(outlets=[Dataset(f"bq://{CORE_PROJECT_ID}.orga_customer_uk.customer_raw_v1")])
    def ingest_some_data_customer_raw():
        print("assuming we are ingesting some data here and update the data source")

    @task(outlets=[Dataset(f"bq://{CORE_PROJECT_ID}.orga_customer_uk.sales_raw_v1")])
    def ingest_some_data_sales_raw():
        print("assuming we are ingesting some data here and update the data source")

    @task(outlets=[Dataset(f"bq://{CORE_PROJECT_ID}.orga_customer_uk.marketing_raw_v1")])
    def ingest_some_data_marketing_raw():
        print("assuming we are ingesting some data here and update the data source")

    @task(outlets=[Dataset(f"bq://{CORE_PROJECT_ID}.orga_customer_uk.events_raw_v1")])
    def ingest_some_data_events_raw():
        print("assuming we are ingesting some data here and update the data source")

    @task(outlets=[Dataset(f"bq://{CORE_PROJECT_ID}.orga_application_uk.application_logs_raw_v1")])
    def ingest_some_data_app_logs_raw():
        print("assuming we are ingesting some data here and update the data source")

    ingest_some_data_customer_raw()
    ingest_some_data_sales_raw()
    ingest_some_data_marketing_raw()
    ingest_some_data_events_raw()
    ingest_some_data_app_logs_raw()


ingestion_dag_a()
