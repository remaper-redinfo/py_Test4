from elasticsearch import Elasticsearch
from datetime import datetime

def searchAPI(es, index, body):
    if(body!=None) : 
        res = es.search(index=index, body=body)
    else :
        res = es.search(index=index)
    # res에 검색 결과가 담겨져 있다
    return res
body = {
    "query": {
        "match_all": {}
    }
}
es = Elasticsearch('http://localhost:9200')
# body = None
res = searchAPI(es, "product_list3", body)
print(res)
