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
    PORT   = 27017

    #def __init__(self, **kwargs):
    #    self.conn = MongoClient()
    #    self.conn = MongoClient(self.SERVER, self.PORT)

    def connect(self):

        conn = None
        # Connection to Mongo DB
        try:
            self.conn=pymongo.MongoClient(self.SERVER, self.PORT)
            print "Connected successfully!!!"
        except pymongo.errors.ConnectionFailure, e:
            print "Could not connect to MongoDB: %s" % e

        if self.conn is not None:
            return self.conn
        else:
            return False

    def conectDatabase(self, mongoConnection, databaseName):
        self.db = mongoConnection[databaseName]
        return self.db

    def showAllDatabases(self, mongoConnection):
        return mongoConnection.database_names()

    def getCollection(self, database):
        return database.my_collection

    def showAllCollections(self, database):
        return database.collection_names()

    def insertCollectionToDB(self, database, collection, document):


test = MongoConnect()
mongoConnection = test.connect()

db = test.conectDatabase(mongoConnection, "sumit")
collection = test.getCollection(db)
doc = {"name":"sumit","surname":[{"name":"ssss"},{"twitter":"@Altons"}]}
collection.insert(doc)

print test.showAllDatabases(mongoConnection)
print test.showAllCollections(db)

#cursor = db.collection.find({'name': {'$regex': 's'}})
#for collection1 in db.collection_names():
    #print collection1.find({"name":"sumit"})

cursor = collection.find({"name":{"$regex":"sum"}})
print cursor.count()
#print cursor.__getitem__(0)
for result_object in cursor:
    print "hello"
    print result_object['_id']



