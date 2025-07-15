from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from service-b BLUE!"  # Later you switch to GREEN

@app.route("/user/<username>")
def get_user(username):
    return jsonify({"username": username, "email": f"{username}@example.com"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
