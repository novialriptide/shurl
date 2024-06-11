from typing import Tuple
from shurl import Shurl  # type: ignore
from flask import Flask

app = Flask(__name__)
shurl_app = Shurl(epoch_count=100, batch_size=64)


@app.route("/")
def hello_world() -> str:
    return "Hello, world!"


@app.route("/trainer")
def trainer() -> Tuple[str, int]:
    # TODO: Create a web application where you'll get a screenshot
    # of a website and will be asked to create a shortened URL for it.
    return "Not ready yet", 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4352, debug=True)
