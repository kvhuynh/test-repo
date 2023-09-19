from flask_app.config.mysqlconnection import connectToMySQL

class CollabFoldEntry:
    def __init__(self) -> None:
        pass
    
    @classmethod
    def create(data):
        return