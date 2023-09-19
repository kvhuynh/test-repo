from flask_app.config.mysqlconnection import connectToMySQL

class AlphaFoldEntry:
    def __init__(self) -> None:
        pass
    
    @classmethod
    @classmethod
    def create(cls, data):
        query = "INSERT INTO shows (user_id, title, network, description, release_date) VALUES (%(user_id)s, %(title)s,%(network)s,%(description)s, %(release_date)s);"
        # comes back as the new row id
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result