from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from service-a GREEN!"  # or BLUE when you change it