# Run spark job using spark binary

1 - Download spark binary 
`curl https://archive.apache.org/dist/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.6.tgz -o spark-binary.tgz`

2 - Extract file with  
`tar -zxvf spark-binary.tgz -C ./spark-binary --strip-components=1`

3 - Run a job in master cluster

Start container on 
`bash
./spark-binary/bin/spark-submit --master spark://localhost:7077 \
    --class org.apache.spark.examples.SparkPi \
    --num-executors 2 \
    --driver-memory 600m \
    --executor-memory 600m \
    --executor-cores 1 \
    ./spark-binary/examples/jars/spark-examples*.jar 1000
`
------------------------------------

# Run spark profile

2 - Create a virtualenv for python2
`virtualenv -p python2 .venv`

3 - Enable virtual env
`source ./.venv/bin/activate`

4 - Start influxcd database
```
docker run -itd -p 8086:8086 -p 8088:8088 -v "/etc/influxdb/influxdb.conf:`pwd`/influxdb.conf" influxdb:1.8 
```


4 - Run job with profile
`bash
./spark-submit-flamegraph --master spark://localhost:7077 \
    --class org.apache.spark.examples.SparkPi \
    --num-executors 1 \
    --driver-memory 1G \
    --executor-memory 1G \
    --executor-cores 1 \
    ./spark-binary/examples/jars/spark-examples*.jar 1
`

See output to find path of flamegraph


--------------------------------------------

Use Spark Shell to test interative code

`./spark-binary/bin/spark-shell --master spark://localhost:7077 --jars ./spark-binary/examples/jars/spark-examples*.jar`

Inside spark shell you can update with

`:require ./spark-binary/examples/jars/spark-examples*.jar`

You will be able to put custom code and run on spark cluster

More information on https://mungingdata.com/apache-spark/using-the-console/