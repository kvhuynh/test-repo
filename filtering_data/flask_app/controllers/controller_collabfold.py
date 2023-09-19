from flask_app import app

@app.route("/orf/create", methods=["POST"])
def orf_create():
    id = 0;
    