from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'Dc7654321'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30968
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True   
        else:
            raise Exception("Nothing to save, because data parameter is empty")         
            
        
# Create method to implement the R in CRUD
    def read(self, data):
        animal_records = []
        if data is not None:
            animal_records = list(self.database.animals.find(data))
        
        
# Update method of CRUD 
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set": change})
                CRUD_result = update_result.raw_result
            else:
                CRUD_result = "No document has been located"
            return CRUD_result
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            
#Delete method of CRUD           
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                CRUD_result = delete_result.raw_result
            else:
                CRUD_result = "No document has been located"
            return CRUD_result
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
