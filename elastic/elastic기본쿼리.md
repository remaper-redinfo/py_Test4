PUT /catalog/_doc/1
{
  "sku" : "sp0000001",
  "title" : "elastic for bigdata",
  "description" : "elastic for bigdata",
  "author" : "kim ki hyun",
  "ISBN" : "1231241232",
  "price" : 300000
}

GET catalog/_search
GET catalog/_mapping/

PUT /catalog/_doc/2
{
  "sku" : "sp0000002",
  "title" : "elastic for bigdata",
  "description" : "elastic for bigdata",
  "author" : "kim ki hyun",
  "ISBN" : "1231241232",
  "price" : 300000,
  "email" : "remaper@naver.com"
}

GET catalog/_search
GET catalog/_mapping/

POST /catalog/_doc/
{
  "sku" : "sp0000002",
  "title" : "elastic for bigdata",
  "description" : "elastic for bigdata",
  "author" : "kim ki hyun",
  "ISBN" : "1231241232",
  "price" : 300000,
  "email" : "remaper@naver.com"
}

GET catalog/_source/KrLRb3MBTSiFr1kX2o4R

GET catalog/_source/5

POST /catalog/_update/5
{
  "doc":{
    "email" : ["remaper@naver.com" ]
  }
}

POST /catalog/_update/5
{
  "doc":{
    "sku" : "sp0000002",
    "title" : "elastic for bigdata",
    "description" : "elastic for bigdata",
    "author" : "kim ki hyun",
    "ISBN" : "1231241232",
    "price" : 300000
  },
  "doc_as_upsert" : true
}

POST catalog/_update/1
{
    "script" : {
        "source": "ctx._source.price += params.price",
        "lang": "painless",
        "params" : {
            "price" : 20000
        }
    }
}


POST catalog/_update/5
{
    "script" : {
        "source": "ctx._source.email.add(params.email)",
        "lang": "painless",
        "params" : {
            "email" : "remaper"
        }
    }
}

PUT test/_doc/1
{
    "counter" : 1,
    "tags" : ["red"]
}

GET test/_doc/1

POST test/_update/1
{
    "script" : {
        "source": "ctx._source.counter += params.count",
        "lang": "painless",
        "params" : {
            "count" : 4
        }
    }
}

POST test/_update/1
{
    "script" : {
        "source": "ctx._source.tags.add(params.tag)",
        "lang": "painless",
        "params" : {
            "tag" : "blue"
        }
    }
}

POST test/_update/1
{
    "script" : {
        "source": "if (ctx._source.tags.contains(params.tag)) { ctx._source.tags.remove(ctx._source.tags.indexOf(params.tag)) }",
        "lang": "painless",
        "params" : {
            "tag" : "blue"
        }
    }
}

POST test/_update/1
{
    "script" : "ctx._source.new_field = 'value_of_new_field'"
}

POST test/_update/1
{
    "script" : "ctx._source.remove('new_field')"
}

POST test/_update/1
{
    "script" : {
        "source": "if (ctx._source.tags.contains(params.tag)) { ctx.op = 'delete' } else { ctx.op = 'none' }",
        "lang": "painless",
        "params" : {
            "tag" : "red"
        }
    }
}

POST test/_update/3
{
    "doc" : {
        "name" : "new_name"
    },
    "doc_as_upsert" : true
}

put test/_mapping/
{
    "properties" : {
        "code": {
          "type":"keyword"
        }
    }
}

get test/_mapping/

get /test/_search?size=100





























































