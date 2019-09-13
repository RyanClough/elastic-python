## Elasticsearch, Kibana and Python

This repo consists of a docker-compose.yml that will spin up a container that includes Elasticsearch (a 2 node cluster) along with Kibana (a UI to look at the data).  You may need to adjust your Docker settings on your machine if you only give it minimal resources.  I have given my Docker instance 64GB of storage and 6GB of RAM but I don't think that much is necessary.

In order to run Elasticsearch/Kibana it is simple:
+ `docker-compose pull`
+ `docker-compose up --build`  (you can add -d to run it in the background if you'd like)

Once that stack is up and running you can enter the python virtual environment and run the following file to import NationalNames.csv into your Elasticsearch instance:
+ `source env/bin/activate`
+ `python3 elastic_csv.py`

When I ran it on my Macbook pro, uploading 1.8M csv records took about 1.5-2.0 minutes and this will vary according to what resources you've given your Docker container.

The source data came from a free online source called [Kaggle](https://www.kaggle.com/kaggle/us-baby-names).
