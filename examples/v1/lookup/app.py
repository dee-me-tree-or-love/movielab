from flask import Flask
app = Flask(__name__)


@app.route("/movie/our/<movie_id>")
def get_movie_from_our_information_api():
    return "Hello World!"


@app.route("/movie/external/<movie_id>")
def get_movie_from_external_information_api():
    return "Hello World!"
