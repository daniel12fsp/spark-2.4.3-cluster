FROM apache/airflow:2.2.4
ARG DEBIAN_FRONTEND=noninteractive

# Install spark operator for airflow to work with spark
RUN pip install 'apache-airflow-providers-apache-spark'

USER root

RUN apt-get update
RUN apt-get install unzip zip wget curl -y

# Install java 8
RUN wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -
RUN echo "deb $([ \"$(uname -m)\" = \"x86_64\" ] && echo -n '[arch=amd64]') https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/ buster main" | sudo tee /etc/apt/sources.list.d/adoptopenjdk.list
RUN apt update
RUN apt install adoptopenjdk-8-hotspot -y

# Install spark binary

ENV SPARK_VERSION=2.4.3 \
HADOOP_VERSION=2.6 \
SPARK_HOME=/opt/spark

RUN apt-get install -y curl wget \
      && wget "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" \
      && tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
      && mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} $SPARK_HOME \
      && rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
      && cd /

