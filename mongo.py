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

    def __init__(self, **kwargs):

        if kwargs.get('server') is not None:
            self.SERVER = kwargs.get('server')

        if kwargs.get('port') is not None:
            self.PORT = kwargs.get('port')
        try:
            self.conn = MongoClient(self.SERVER, self.PORT)
        except pymongo.errors.ConnectionFailure, e:
            print "Could not connect to MongoDB: %s" % e

    def connect(self):

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

    def conectDatabase(self, databaseName):
        self.db = self.conn[databaseName]
        return self.db

    def showAllDatabases(self):
        return self.conn.database_names()

    def getCollection(self):
        self.collection = self.db.my_collection
        return self.collection

    def showAllCollections(self):
        return self.db.collection_names()

    def insertDocumentToCollection(self, document):
        self.collection.insert(document)

test = MongoConnect()

# mongoConnection = test.connect()

print test.conectDatabase("kumar")
print test.showAllDatabases()
print test.getCollection()
print test.collection

# collection = test.getCollection(db)
# doc = {"name":"sumit","surname":[{"name":"ssss"},{"twitter":"@Altons"}]}
# collection.insert(doc)
#
# print test.showAllDatabases(mongoConnection)
# print test.showAllCollections(db)

#cursor = db.collection.find({'name': {'$regex': 's'}})
#for collection1 in db.collection_names():
    #print collection1.find({"name":"sumit"})

# cursor = collection.find({"name":{"$regex":"sum"}})
# print cursor.count()
# print cursor.__getitem__(0)
# for result_object in cursor:
#     print "hello"
#     print result_object['_id']
#


