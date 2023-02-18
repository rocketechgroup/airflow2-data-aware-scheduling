import pendulum

from airflow import Dataset
from airflow.decorators import dag, task
from airflow_core.shared_vars import CORE_PROJECT_ID


@dag(
    schedule=[Dataset(f"bq://{CORE_PROJECT_ID}.orga_customer_uk.customer_raw_v1"),
              Dataset(f"bq://{CORE_PROJECT_ID}.orga_customer_uk.marketing_raw_v1")],
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["analytics_engineering", "modelling", "marketing"],
)
def marketing_dag_a():
    @task(outlets=[Dataset(f"bq://{CORE_PROJECT_ID}.customer_marketing.customer_marketing")])
    def modelling_task_1():
        print("Doing some complex data modelling work on DBT and update another data source")

    modelling_task_1()


marketing_dag_a()
