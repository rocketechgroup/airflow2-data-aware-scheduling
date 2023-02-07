# Airflow 2 - Local Lightweight Version

## Why
The default Airflow Docker Compose environment is based on CeleryExecutor which is quite resource heavy. 

This example is based on the official base Airflow 2 docker compose file and the article https://datatalks.club/blog/how-to-setup-lightweight-local-version-for-airflow.html

## Install Docker
Since docker desktop has been requesting a paid licence for business use, install https://github.com/abiosoft/colima instead.

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
You can check the mounted volumes or environment variables set inside the webserver by getting into the container using the following command
```
docker exec -it $(docker ps | grep webserver | cut -d' ' -f1) /bin/bash
```

