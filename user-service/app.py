from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "User Service - Running"

@app.route("/health")
def health_check():
    return "OK", 200

@app.route("/users")
def get_user(username):
    return "Gaurav"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
