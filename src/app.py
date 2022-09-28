import os
from flask import Flask, Response
import json

app = Flask(__name__)


@app.route("/healthcheck")
def healthcheck():
    return Response(status=200)


@app.route("/hello", methods=["POST"])
def hello():
    return Response(
        status=200,
        response=json.dumps({"msg": "welcome"}),
        content_type="application/json",
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
