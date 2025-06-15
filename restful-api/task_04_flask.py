#!/usr/bin/python3


from flask import Flask, jsonify, request

app = Flask(__name__)


users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        user = users[username]
        user["username"] = username  
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }

    response = {
        "message": "User added",
        "user": {
            "username": username,
            "name": users[username]["name"],
            "age": users[username]["age"],
            "city": users[username]["city"]
        }
    }
    return jsonify(response), 201

if __name__ == "__main__":
    app.run()
