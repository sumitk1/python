"""
This is the python module for connecting and executing queries to MongoDB through python
"""
import pymongo
from pymongo import MongoClient

class MongoConnect(object):
    """
    This class has functions to connect to MongoDB
    """

    SERVER = "localhost"
    PORT   = "27017"

    def __init__(self, **kwargs):
        self.client = MongoClient()
        self.client = MongoClient(self.SERVER, self.PORT)

    def conectDatabase(self, databaseName):
        self.database = self.client.databasename
        return self.database

    def showAllDatabases(self):
        databases = show dbs
	#hmmm
