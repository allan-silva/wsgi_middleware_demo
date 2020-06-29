import time

from datetime import datetime

import middlewares

from flask import Flask, request
from flask.json import jsonify


app = Flask(__name__)


def log_response(request, response_data):
    print(f"{datetime.now()} - Logging request information...")
    print(f"{datetime.now()} - BaseUrl: {request.base_url}")
    print(f"{datetime.now()} - Path: {request.path}")
    print(f"{datetime.now()} - Args: {request.args}")
    print(f"Response data: {response_data}")
    time.sleep(10) # expensive task
    print(f"Request information registered (id: {request.args.get('id')})")


middlewares.configure_app(app, log_response)


@app.route("/update/6/firefox/77.0.1")
def index():
    return jsonify(
        {
            "id": request.args["id"],
            "name"   : "The Dark Side of the Moon",
            "artist" : "Pink Floyd",
            "year"   : 1973,
            "tracks" : [
                "Speak To Me",
                "Breathe",
                "On The Run",
                "Comfortably Numb",
            ]
        }
    )
