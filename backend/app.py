from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

PRODUCTS = [
    {"id": 1, "name": "Running Shoes", "price": 2999, "image": "shoes.jpg"},
    {"id": 2, "name": "Leather Bag", "price": 4599, "image": "bag.jpg"},
    {"id": 3, "name": "Smart Watch", "price": 6999, "image": "watch.jpg"}
]

# ✅ ROOT ROUTE – SERVES index.html
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/products")
def products():
    return jsonify(PRODUCTS), 200

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


