import pendulum

from airflow import Dataset
from airflow.decorators import dag, task
from airflow_core.shared_vars import CORE_PROJECT_ID


@dag(
    schedule=[Dataset(f"bq://{CORE_PROJECT_ID}.orga_customer_uk.events_raw_v1"),
              Dataset(f"bq://{CORE_PROJECT_ID}.orga_application_uk.application_logs_raw_v1"),
              Dataset(f"bq://{CORE_PROJECT_ID}.customer_sales.customer_sales"),
              Dataset(f"bq://{CORE_PROJECT_ID}.customer_core.customer")],
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["data_engineering", "service_a"],
)
def data_eng_service_dag_a():
    @task(outlets=[Dataset(f"bq://{CORE_PROJECT_ID}.service_a.service_logs_v1")])
    def complex_task_1():
        print("Building some complex data processing pipelines and producing some data")

    complex_task_1()


data_eng_service_dag_a()
