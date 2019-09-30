# mongodb python driver
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from manage_db import Manage_db

mdb_obj = Manage_db('nlp_project', 'credentials.json')

print(mdb_obj.db)

nb_alesia = mdb_obj.total_comments_shop(mdb_obj.db, 'boutiques', 'Orange Alesia')
print(nb_alesia)