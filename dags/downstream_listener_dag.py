import pendulum
import os

from google.cloud import bigquery

from airflow import Dataset
from airflow.decorators import dag, task

my_project_id = os.environ.get('GCP_PROJECT_ID')


@dag(
    schedule=[Dataset(f"bigquery://{my_project_id}.london_bicycles.cycle_stations")],
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def downstream_listener_dag():
    @task()
    def listener_task(*kwargs):
        print("I am triggered")
        print(kwargs)

    listener_task()


downstream_listener_dag()
