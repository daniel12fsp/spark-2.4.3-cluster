from datetime import datetime

from airflow.models import DAG


from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG(
    dag_id='example_spark_operator',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:
    submit_job = SparkSubmitOperator(
        conn_id= 'spark', 
        java_class="org.apache.spark.examples.SparkPi",
        driver_memory="600m",
        executor_memory="600m",
        application="/opt/spark/examples/jars/spark-examples_2.11-2.4.3.jar", 
        task_id="submit_job",
        application_args=["1"],
        spark_binary="/opt/spark/bin/spark-submit",
        executor_cores=1,
        num_executors=1
    )
    submit_job

