from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://u1ai5zsuzpe6y74uwyqu:0BacMZwIRVg5rpsOcndFG1pcHSUba5@by1wvfyyi5kgu1euhyko-postgresql.services.clever-cloud.com:50013/by1wvfyyi5kgu1euhyko"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from authors import Author
from members import Members
@app.route("/authors/", methods=['GET'])
def getAuthors():
    authors = Author.query.all()

    author_list = [
        {"author_id": author.author_id, "name": author.name, "bio": author.bio}
        for author in authors
    ]
    #author_list = [aut.to_dict() for aut in authors] pri tejto moznosti treba dorobit funkciu to_dict do file author
    return jsonify (author_list)

# @app.route("/members/", methods=['GET'])
#     members=Member.query.all()
#
#     member_list = [mem.to_dict() for mem in members] # pri tejto moznosti treba dorobit funkciu to_dict do file author
#     return jsonify (member_list)

@app.route("/members/", methods=['GET'])
def getMembers():
    members=Members.query.all()

    member_list = [mem.to_dict() for mem in members] # pri tejto moznosti treba dorobit funkciu to_dict do file author
    return jsonify(member_list)


@app.route("/members/<int:user_id>", methods=["GET"])
def getMember(user_id):
    member = Members.query.get(str(user_id))
    if member:
        return jsonify(member.to_dict()), 200
    else:
        return "User not found", 404


@app.route('/members', methods=['POST'])
def registerUser():
    data = request.json

    createUser = Members.create_from_request(request)
    return jsonify(createUser.to_dict()), 200

if __name__ == "__main__":
    app.run(debug=True)




