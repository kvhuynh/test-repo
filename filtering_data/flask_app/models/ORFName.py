# import models.AlphaFoldEntry as AlphaFoldEntry
# import models.CollabFoldEntry as CollabFoldEntry
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "naming"

class ORFName:
    def __init__(self, data):
        # self.data = data["id"];
        # self.orf_name = data["orf_name"]
        print(data)
        # self.alphafold_id = data["alphafold_id"];
    

    @classmethod
    def create(cls, data):
        query = "INSERT INTO orf_names (orf_name) VALUES (%(orf_name)s)";
        print(query)
        
    
    
