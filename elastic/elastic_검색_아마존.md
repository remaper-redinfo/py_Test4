GET /amazon_products2/_search
{
  "query": {
    "range": {
      "price": {
        "gte": 10,
        "lte": 20
      }
    }
  }
}

GET /amazon_products2/_search
{
  "from": 10,
  "size": 10, 
  "query": {
    "range": {
      "price": {
        "gte": 10,
        "lte": 20,
        "boost": 2.2
      }
    }
  }
}


GET /amazon_products2/_search
{
  "query": {
    "exists": {
      "field": "description"
    }
  }
}

GET /amazon_products2/_search
{
  "query": {
    "term": {
      "manufacturer.raw": "victory multimedia"
    }
  }
}

GET /amazon_products2/_search
{
  "query": {
    "match": {
      "manufacturer": "victory multimedia"
    }
  }
}

GET /amazon_products2/_search
{
  "query": {
    "match": {
      "manufacturer": {
        "query":"victory multimedia",
        "operator" : "and"
      }
    }
  }
}

GET /amazon_products2/_search
{
  "query": {
    "match": {
      "manufacturer": {
        "query":"victory multimedia",
        "minimum_should_match": 2
      }
    }
  }
}

GET /amazon_products2/_search
{
  "query": {
    "match": {
      "manufacturer": {
        "query":"victory multimedia",
        "operator" : "or"
      }
    }
  }
}

GET /amazon_products2/_search
{
  "query": {
    "match_phrase": {
      "description": {
        "query":"real video saltware aquarium"
      }
    }
  }
}

GET /amazon_products2/_search
{
  "query": {
    "match_phrase": {
      "description": {
        "query":"real video",
        "slop": 5
      }
    }
  }
}

GET /amazon_products2/_search
{
  "query": {
    "multi_match": {
      "query":"monitor aquarium",
      "fields": [
        "title",
        "description"
      ]
    }
  }
}


GET /amazon_products2/_search
{
  "query": {
    "multi_match": {
      "query":"monitor aquarium",
      "fields": [
        "title^3",
        "description"
      ]
    }
  }
}
