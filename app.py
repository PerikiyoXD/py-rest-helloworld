import flask
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    if request.method != "GET":
        response_data = {
            "error": "Invalid request method",
            "data": None
        }
    else:
        response_data = {
            "error": None,
            "data": "Hello world"
        }
    response = flask.Response(json.dumps(response_data))
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


if __name__ == '__main__':
    app.run()
