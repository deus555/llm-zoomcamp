import minsearch
import json
import openai
from openai import OpenAI
from elasticsearch import Elasticsearch
from tqdm.auto import tqdm

es_client = Elasticsearch('http://localhost:9200')
index_name = "documents_20240818_3220"

def es_search(query):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                }
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)

    result_docs = []

    for hit in response['hits']['hits']:
        result_docs.append(hit)

    return result_docs

print(es_search("When is the next cohort?"))