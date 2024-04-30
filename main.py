from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://u1ai5zsuzpe6y74uwyqu:0BacMZwIRVg5rpsOcndFG1pcHSUba5@by1wvfyyi5kgu1euhyko-postgresql.services.clever-cloud.com:50013/by1wvfyyi5kgu1euhyko"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from authors import Author

@app.route("/authors", methods=["GET"])
def getAuthors():
    authors = Author.query.all()
    return "Authors"

if __name__ == "__main__":
    app.run()

