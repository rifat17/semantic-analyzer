import logging

from flask import Flask, jsonify, request

from app.api.utils import predict

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# logger.addHandler(logging.StreamHandler())


def load_your_model():
    from setfit import SetFitModel

    return SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")


model = load_your_model()

app = Flask(__name__)


@app.route("/analyze", methods=["POST"])
def predict_sentiment():
    data = request.json
    try:
        text = data["text"]
    except KeyError:
        return jsonify({"error": "Invalid input"}), 400
    prediction = predict(model, text)

    try:
        return jsonify(prediction)
    except IndexError:
        return jsonify({"error": "Invalid input"}), 400


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Server error"}), 500


@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0")
