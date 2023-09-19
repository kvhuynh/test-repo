# Setting up a flask app
- Create project folder
- Navigate into folder
```
cd project_name
```
- Install virtual environment w/ flask, pymysql, and flask-bcrypt
```
pipenv install flask pymysql flask-bcrypt

OR

python -m pipenv install flask pymysql flask-bcrypt

```
`WARNING` LOOK FOR __pipfile__ AND __pipfile.lock__
- Launch virtual environment
```
pipenv shell

OR

python -m pipenv shell
```

- Launch VS Code from folder
```
code .
```

- Build project structure
  - project_folder
    - flask_app
      - config
        - [mysqlconnection.py](#mysqlconnection.py)
      - controllers
        - [controller_user.py](#controller_user.py)
      - models
        - [model_user.py](#model_user.py)
      - static
        - css
          - styles.css
        - js
          - script.js
      - templates
        - index.html
      - [\_\_init__](#\_\_init__ (file))
    - server.py
    - pipfile
    - pipfile.lock

## mysqlconnection.py 
```py
# a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

```

## controller_user.py
``` python
from flask_app import app, bcrypt
from flask import Flask, render_template, request, redirect, session, flash

# This imports model file
from flask_app.models.file import File
# ---------- CREATE ---------- #

@app.route("/")
def index():
    return render_template("index.html")

# ---------- READ ---------- #
# Display Route
@app.route("/table_name/new", methods=["POST"])
def table_name_new():
    return render_template("table_name_new.html")

# Action Route
@app.route("/table_name/create", methods=["POST"])
def table_name_create():
    return redirect("/")

@app.route("table_name/<int:id>")
def table_name_show(id):
    return render_template("table_name_show.html")

@app.route("/table_name/<int:id>/update", methods=["POST"])
def table_name_edit(id):
    return render_template("table_name_edit.html")

# ---------- DELETE ---------- #
@app.route("/table_name/<int:id>/delete")
def table_name_delete(id):
    return redirect("/")
```

## model_user.py
``` python
# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = "schema_name"

class table_name:
    def __init__(self, data):
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    # C
    @classmethod
    def create(clas data:dict) -> int:
        query = "INSERT INTO table_name (column_name) VALUES (%(column_Name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    # R
    @classmethod
    def get_one_by_email(cls, data:dict) -> list:
        query = "SELECT * FROM table_name WHERE id = %(id)s;"
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_one_by_email(cls, data:dict) -> list:
        query = "SELECT * FROM table_name WHERE email = %(id)s;"
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM table_name;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_table_name = []
            for table_name_single in results:
                all_table_name.append(cls(table_name_singe))
            return all_table_name
        return False

    # U
    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE table_name SET column_name = %(column_name)s WHERE id = %(id);"
        return connectToMySQL(DATABASE).query_db(query,data)

    # D
    @classmethod
    def delete_one(clas, data:dict) -> None:
        query = "DELETE FROM table_name WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = Faflse

        # some logic here
        return is_valid
        
```

## \_\_init__.py
```python
    from flask import Flask
    app = Flask(__name__)
    app.secret_key = "secret_key"
    # DATABASE = "schema_name"
    from flask_bcrypt import Bcrypt
    bcrypt = Bcrypt(app)
``` 

## server.py
``` python
from flask_app import app
# Remember to continually add controller files as you create them
from flask_app.controllers import controller_user
if __name__=="__main__":
    app.run(debug=True)
```