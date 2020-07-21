POST _analyze
{
  "analyzer": "whitespace",
  "text":     "The quick brown fox. brown brown ~!"
}

POST _analyze
{
  "tokenizer": "standard",
  "filter":  [ "lowercase", "asciifolding" ],
  "text":      "The quick brown fox."
}

POST _analyze
{
  "tokenizer": "standard",
  "filter":  [ "lowercase", "asciifolding" ],
  "text":      "안녕하세요. 김기현입니다."
}


PUT my_analyze
{
  "settings": {
    "analysis": {
      "analyzer": {
        "std_folded": { 
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "asciifolding"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "my_text": {
        "type": "text",
        "analyzer": "std_folded" 
      }
    }
  }
}

GET my_analyze/_analyze 
{
  "analyzer": "std_folded", 
  "text":     "The quick brown fox."
}

GET my_index/_analyze 
{
  "field": "my_text", 
  "text":  "The quick brown fox."
}


PUT my_index_stopwords
{
  "settings": {
    "analysis": {
      "analyzer": {
        "std_english": { 
          "type":      "standard",
          "stopwords": "_english_"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "my_text": {
        "type":     "text",
        "analyzer": "standard", 
        "fields": {
          "english": {
            "type":     "text",
            "analyzer": "std_english" 
          }
        }
      }
    }
  }
}

POST my_index_stopwords/_analyze
{
  "field": "my_text", 
  "text": "The old brown cow"
}

POST my_index_stopwords/_analyze
{
  "field": "my_text.english", 
  "text": "The old brown cow"
}

PUT my_index_http
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer": {
          "type": "custom", 
          "tokenizer": "standard",
          "char_filter": [
            "html_strip"
          ],
          "filter": [
            "lowercase",
            "asciifolding"
          ]
        }
      }
    }
  }
}

POST my_index_http/_analyze
{
  "analyzer": "my_custom_analyzer",
  "text": "The <b>quick brown</b> fox."
}

PUT my_index_emoji
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_analyzer": { 
          "type": "custom",
          "char_filter": [
            "emoticons"
          ],
          "tokenizer": "punctuation",
          "filter": [
            "lowercase",
            "english_stop"
          ]
        }
      },
      "tokenizer": {
        "punctuation": { 
          "type": "pattern",
          "pattern": "[ .,!?]"
        }
      },
      "char_filter": {
        "emoticons": { 
          "type": "mapping",
          "mappings": [
            ":) => _happy_",
            ":( => _sad_"
          ]
        }
      },
      "filter": {
        "english_stop": { 
          "type": "stop",
          "stopwords": "_english_"
        }
      }
    }
  }
}

POST my_index_emoji/_analyze
{
  "analyzer": "my_custom_analyzer",
  "text": "I'm a :) person, and you?"
}
