#!/usr/bin/env python
# coding: utf-8

# pandas
import pandas as pd
# mongodb python driver
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
# library to make the output look more pretty
from pprint import pprint
# json
import json
import os

# --------------------------
#     class Manage_db()
# --------------------------

class Manage_db():

    """
        Class that manages the MongoDB database
    """
    
    def __init__(self, db_name, credentials_file):
    
        """
            Function that creates connection do db
            :param db_name: input value
            :param credentials_file: input value
            :type db_name: string
            :type credentials_file: string
            :return db: connection db
            :rtype db: object
        """
        
        #     credentials.json example
        #     { 
        #         "Username":"name",
        #         "Password":"password",
        #         "Hostname":"cluster9-2kbt8.mongodb.net"
        #     }
        
        # get credentials for connection
        with open(credentials_file, 'r') as f:
            credentials = json.load(f)

        username = credentials['Username']
        password = credentials['Password']
        hostname = credentials['Hostname']
        
        try:
            # client connexion to Atlas server
            client = MongoClient('mongodb+srv://'+username+':'+password+'@'+hostname+'/test?retryWrites=true&w=majority')
            
            print(client.database_names())
            
            # retrieve db
            self.db = client.get_database(db_name)

        except:
            print('Connection Error !')
            self.db = None
            
            
    def total_comments_shop(self, db, collection_name, shop_address):
        """
            Function that counts comments for a specific shop
            :param db: input value
            :param collection_name: input value
            :param shop_address: input value
            :type db: object
            :type collection_name: string
            :type shop_address: string
            :return total_comments: total of comments
            :rtype total_comments: number
        """
        
        try:
            # test collection_name
            assert collection_name in db.list_collection_names()

            # use param collection_names
            collection = db[collection_name]
            # mongodb query
            total_comments = collection.count_documents({"adress": shop_address})

        except:
            print('Operation Error !')
            total_comments = -1

        return total_comments
    
    

