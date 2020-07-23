from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')
index = "test_index"
print(es.search(index=index))