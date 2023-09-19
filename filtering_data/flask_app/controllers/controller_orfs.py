from flask_app import app
from flask_app.models import ORFName

# @app.route("/orf/create", methods=["POST"])
def orf_create(data):
    print(data)
    for entry in data:
        ORFName.ORFName.create(data)

    