from datetime import datetime
from elasticsearch import helpers,Elasticsearch
import csv

es = Elasticsearch()

index = 'baby_name_data'
body = {
        "mappings" : {
            "properties" : {
                "Id" : { "type" : "long" },
                "Name" : { "type": "text"  },
                "Year": { "type": "integer" },
                "Gender": { "type": "text" },
                "Count": { "type": "long" }
            }
    }
}

if not es.indices.exists([index]):
    es.indices.create(index=index, body=body)
    es.indices.refresh()

    with open('NationalNames.csv') as f:
        reader = csv.DictReader(f)
        helpers.bulk(es, reader, index=index)
