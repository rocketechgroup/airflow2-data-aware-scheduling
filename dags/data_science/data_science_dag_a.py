import pendulum

from airflow import Dataset
from airflow.decorators import dag, task
from airflow_core.shared_vars import CORE_PROJECT_ID


@dag(
    schedule=[Dataset(f"bq://{CORE_PROJECT_ID}.orga_customer_uk.sales_raw_v1"),
              Dataset(f"bq://{CORE_PROJECT_ID}.service_a.service_logs_v1"),
              Dataset(f"bq://{CORE_PROJECT_ID}.product_a.product_logs_v1"),
              Dataset(f"bq://{CORE_PROJECT_ID}.customer_marketing.customer_marketing")],
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["data_science", "modelling", "nba"],
)
def data_science_nba_dag_a():
    @task(outlets=[Dataset(f"bq://{CORE_PROJECT_ID}.data_science.customer_model")])
    def modelling_task_1():
        print("Doing some complex data modelling work on DBT and update another data source")

    @task(outlets=[Dataset(f"bq://{CORE_PROJECT_ID}.customer_nba.nba_model")])
    def vertex_ai_task_1(task_1):
        print("Trigger a Vertex AI job and outputs some features")

    vertex_ai_task_1(modelling_task_1())


data_science_nba_dag_a()
