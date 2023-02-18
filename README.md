# Airflow 2 - Data Aware Scheduling

## Why

Data Aware Scheduling is a new feature comes with Airflow 2.4. It's a very powerful feature allows DAGs to be triggered
via a data URI. This repository contains a set of examples on how this can be used to track & trigger dependencies
across multiple functional teams.

[what it might look like in a large org](docs/data_aware_scheduling_in_large_org.png)

## The Local Airflow Setup

The default Airflow Docker Compose environment is based on CeleryExecutor which is quite resource heavy.

This example is based on the official base Airflow 2 docker compose file and the
article https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html

## Install Docker

Since docker desktop has been requesting a paid licence for business use, install https://github.com/abiosoft/colima
instead.

To install `gcloud`, see https://cloud.google.com/sdk/docs/install

Then install docker & docker compose via `brew install docker` and `brew install docker-compose`

## Init

Run

```
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

then run

```
docker-compose up airflow-init
```

## Start Airflow

> To generate gcloud application default credentials, run `gcloud auth login --update-adc`

```
docker-compose up
```

Wait for airflow server to be up (see CLI logs), then go to

```
http://localhost:8080/home
```

## Debugging

You can check the mounted volumes or environment variables set inside the webserver by getting into the container using
the following command

```
docker exec -it $(docker ps | grep webserver | cut -d' ' -f1) /bin/bash
```

## Deploy to Cloud Composer

This method of deployment is good if you have multiple teams working independently, and their workload should be
deployed independently. These `gsutil` commands can be easily integrated with any CI/CD tool such as CloudBuild.

```
export BUCKET_NAME=<your gcs bucket name of cluod composer>
```

```
gsutil -m rsync -d -r ./dags/core gs://${BUCKET_NAME}/dags/core
gsutil -m rsync -d -r ./dags/airflow_core gs://${BUCKET_NAME}/dags/airflow_core
gsutil -m rsync -d -r ./dags/analytics_engineering gs://${BUCKET_NAME}/dags/analytics_engineering
gsutil -m rsync -d -r ./dags/data_engineering gs://${BUCKET_NAME}/dags/data_engineering
gsutil -m rsync -d -r ./dags/data_science gs://${BUCKET_NAME}/dags/data_science
gsutil -m rsync -d -r ./dags/software_engineering gs://${BUCKET_NAME}/dags/software_engineering
```