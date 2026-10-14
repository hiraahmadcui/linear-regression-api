from flask import Flask, request, jsonify
import random

app = Flask(__name__)

ROLL_NUMBER = "FA23-BDS-050"
SEED = 50

random.seed(SEED)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

@app.route("/predict", methods=["GET"])
def predict():
    try:
        x1 = float(request.args.get("x1"))
        x2 = float(request.args.get("x2"))
        x3 = float(request.args.get("x3"))
    except (TypeError, ValueError):
        return jsonify({"error": "Provide numeric x1, x2, x3"}), 400

    y = a1 * x1 + a2 * x2 + a3 * x3 + b

    return jsonify({
        "registration number": ROLL_NUMBER,
        "prediction": round(y, 2)
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)