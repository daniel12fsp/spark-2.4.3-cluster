FROM openjdk:8u322-jre

RUN apt-get update && apt-get install -y curl vim wget software-properties-common ssh net-tools ca-certificates rsync

ENV SPARK_VERSION=2.4.3 \
HADOOP_VERSION=2.6 \
SPARK_HOME=/opt/spark \
PYTHONHASHSEED=1

RUN mkdir /opt/spark/logs -p

RUN wget --no-verbose -O apache-spark.tgz "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" \
&& tar -xf apache-spark.tgz -C /opt/spark --strip-components=1 \
&& rm apache-spark.tgz

RUN wget -qc https://github.com/etsy/statsd-jvm-profiler/releases/download/2.1.0/statsd-jvm-profiler-2.1.0-jar-with-dependencies.jar -O /tmp/statsd-jvm-profiler.jar

ENV SPARK_MASTER_PORT=7077 \
SPARK_MASTER_WEBUI_PORT=8080 \
SPARK_LOG_DIR=/opt/spark/logs \
SPARK_MASTER_LOG=/opt/spark/logs/spark-master.out \
SPARK_WORKER_LOG=/opt/spark/logs/spark-worker.out \
SPARK_WORKER_WEBUI_PORT=8080 \
SPARK_WORKER_PORT=7000


WORKDIR /opt/spark/bin

COPY ./start-spark.sh .

CMD ./start-spark.sh