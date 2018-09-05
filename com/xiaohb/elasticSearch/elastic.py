import os
import time
from os import walk
# import CSVOP
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(['localhost:9200'])
def insertTest():
    body = {"name":"肖贺博","age":24}
    es.index(index='zhilian',doc_type='typeName', body=body,id='999')
def deleteTest():
    es.delete(index='zhilian', doc_type='typeName', id='999')
def updateTest():
    body = {"name":"肖贺博","age":24}
    es.update(index='zhilian', doc_type='typeName', id='999', body=body,params=body)
def queryTest():
    a = es.get(index='zhilian', doc_type='typeName', id='999')
    print(a)
updateTest()
queryTest()