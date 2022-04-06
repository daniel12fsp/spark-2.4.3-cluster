# Requiremente

1 - go to folder spark-docker-cluster
2 - docker-compose up

3 - check spark interface ui on localhost:9090


## Why airflow?

Airflow is a schedule with support for any workflows like spark...

## Start airflow


- To start a container its need this command:

    docker-compose up airflow-init
    docker-compose up

See more information on 


## About docker images

- Docker compose based of https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#docker-compose-yaml the only change is to install  java8 and spark binary and spark operator to work spark-submit inside of airflow
