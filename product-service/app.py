from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Product Service - Running"

@app.route("/products/<product_id>")
def get_product(product_id):
    return jsonify({"product_id": product_id, "name": "Sample Product", "price": 99.99})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
