from typing import Tuple, Any
from shurl import Shurl  # type: ignore
from flask import Flask, jsonify, request
import validators

app = Flask(__name__)
shurl_app = Shurl(epoch_count=100, batch_size=64)


@app.route("/")
def hello_world() -> str:
    return "Hello, world!"


@app.route("/response", methods=["POST"])
def get_response() -> Tuple[Any, int]:
    webpage_url = request.form["webpage_url"]

    if not validators.url(webpage_url):
        return jsonify({"success": False, "error": "Invalid URL"}), 400

    response = shurl_app.handle_url(webpage_url)

    return jsonify({"success": True, "response": response}), 200


@app.route("/trainer")
def trainer() -> Tuple[Any, int]:
    # TODO: Create a web application where you'll get a screenshot
    # of a website and will be asked to create a shortened URL for it.
    return jsonify({"success": False, "error": "Not implemented yet"}), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4352, debug=True)
