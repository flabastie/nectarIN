#!/usr/bin/env python
# coding: utf-8

# In[147]:


# !python -m pip install pymongo
# !python -m pip install pymongo[srv]


# In[148]:


# pandas
import pandas as pd
# mongodb python driver
from pymongo import MongoClient
# library to make the output look more pretty
from pprint import pprint
# json
import json


# ### Data format : csv => json

# In[149]:


df = pd.DataFrame(pd.read_csv("proj_reviews.csv", sep = ",", header = 0, index_col = False))

df.to_json("boutiques.json", orient = "records")
# df.to_json("boutiques.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)


# In[201]:


pd.set_option('display.max_columns', None)
df.head()


# In[151]:


for col in df.columns: 
    print(col) 


# ### Get data to insert to db

# In[152]:


with open('boutiques.json') as f:
    data = json.load(f)

pprint(data)


# In[153]:


# localhost example connexion

# client = MongoClient('localhost', 32769)
# db=client.admin

# Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)


# ### db connexion

# In[154]:


# get credentials for connexion
with open('credentials.json') as f:
    credentials = json.load(f)
    
username = credentials['Username']
password = credentials['Password']
hostname = credentials['Hostname']


# In[155]:


# client connexion to Atlas server
client = MongoClient('mongodb+srv://'+username+':'+password+'@'+hostname+'/test?retryWrites=true&w=majority')


# In[156]:


# retrieve db
db = client.get_database('nlp_project')


# In[157]:


# get collection 'boutiques'
records = db.boutiques

# count documents
records.count_documents({})


# ### Insert datas

# In[158]:


# insert data into collection 'boutiques'

try:
    records.insert_many(data)
    # count documents
    records.count_documents({})
except :
    print("Error or insert already done ?")


# ### Find datas

# In[165]:


list(records.find().limit(5))


# ### Find document with specific user

# In[162]:


records.find_one({'n_review_user': 'CLAIRE VICTOR'})


# ### Get specific fields only

# In[189]:


comments = list(records.find({'n_review_user':{"$ne":None}, 'caption':{"$ne":None}}, {'n_review_user':1, 'caption':1, '_id':0}).limit(5))
type(comments)


# In[198]:


for item in comments:
    print(item['n_review_user'])
    print(item['caption'], '\n')

