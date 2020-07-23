from elasticsearch import Elasticsearch, helpers
from datetime import datetime

# 데이터 불러오기 - 파일, 스크래핑한 데이터, openAPI

# 불러온 데이터 => 이터레이터로 만들어 줌

docs = []

for num in range(100): #이터레이터 반복 자리
    docs.append({
        '_index': "product_list3",
        '_source': {
            "category": "test",
            "c_key": "test",
            "status": "test",
            "price": 1111,
            "@timestamp": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        }
    })

es = Elasticsearch('http://localhost:9200')

helpers.bulk(es, docs)