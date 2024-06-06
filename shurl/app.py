from shurl import Shurl  # type: ignore
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return "Hello, world!"


if __name__ == "__main__":
    shurl_app = Shurl(epoch_count=100, batch_size=64)
    app.run(host="0.0.0.0", port=4352, debug=True)
