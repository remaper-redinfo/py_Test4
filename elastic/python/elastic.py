from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

index = "test_index"

doc = {
    "name" : "김기현"
}

es.index(index=index, doc_type="_doc", body=doc)

# print(es.search(index=index))