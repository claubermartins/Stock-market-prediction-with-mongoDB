# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:20:23 2021

@author: Clauber
"""

#Importing libraries
import json
#from bson import BSON
from pymongo import MongoClient

# Making Connection with MongoDB
myclient = MongoClient('localhost', 27017)
# Database 
db = myclient['db_petr4']
#Collection 
collection_acoes = db['acoes']

with open('petr4-treinamento.json') as f:
    file_data_base = json.load(f)
# if pymongo < 3.0, use insert()
#collection_posts.insert(file_data_base)
# if pymongo >= 3.0 use insert_one() for inserting one document
#collection_posts.insert_one(file_data_base)
# if pymongo >= 3.0 use insert_many() for inserting many documents
collection_acoes.insert_many(file_data_base)

myclient.close()
    