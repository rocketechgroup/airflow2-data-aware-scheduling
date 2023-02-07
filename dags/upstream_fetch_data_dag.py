import pendulum
import os

from google.cloud import bigquery

from airflow import Dataset
from airflow.decorators import dag, task

my_project_id = os.environ.get('GCP_PROJECT_ID')


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def upstream_fetch_data_dag():
    @task()
    def fetch_cycle_stations():
        # create a client object
        client = bigquery.Client(project=os.environ.get('GCP_PROJECT_ID'))
        # run a query to fetch data from the table
        query = "SELECT * FROM `bigquery-public-data`.london_bicycles.cycle_stations"
        query_job = client.query(query)
        rows = query_job.result()

        stations = []
        for row in rows:
            stations.append({'id': row['id'], 'name': row['name']})

        return stations

    @task(outlets=[Dataset(f"bigquery://{my_project_id}.london_bicycles.cycle_stations")])
    def update_my_local_copy(stations: list):
        for s in stations:
            print(s)  # assume this update a table called <my_project_id>.london_bicycles.cycle_stations

    update_my_local_copy(fetch_cycle_stations())


upstream_fetch_data_dag()
