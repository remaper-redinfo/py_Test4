import requests

url='http://localhost:9200/product_list3/_search?pretty'

response = requests.get(url)

print(response.text)

res = response.json()

print(res['hits']['hits'][0]['_id'])
print(res['hits']['hits'][1]['_id'])
print(res['hits']['hits'][2]['_id'])
print(res['hits']['hits'][3]['_id'])