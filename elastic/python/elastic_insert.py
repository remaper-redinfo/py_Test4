from elasticsearch import Elasticsearch
from datetime import datetime
import json

def nonMapping_insertData(es):
    index = "product_list"

    doc = {
        "category": "skirt",
        "c_key": "1234",
        "price": 11400,
        "status": 1,
        "@timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }

    es.index(index=index, doc_type="_doc", body=doc)

def mapping_insertData(es):
    index = "product_list2"

    with open('mapping.json', 'r') as f:
        mapping = json.load(f)

    if es.indices.exists(index=index):
        pass
    else:
        es.indices.create(index=index, body=mapping)

    doc = {
        "category": "skirt",
        "c_key": "1234",
        "price": 11400,
        "status": 1,
        "@timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    }

    es.index(index=index, doc_type="_doc", body=doc)