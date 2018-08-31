from src.info_service_client import InfoServiceClient
from src.response_builder import ResponseBuilder

from flask import Flask
app = Flask(__name__)


@app.route("/movies/our/<movie_id>")
def get_movie_from_our_information_api(movie_id):
    info_service = InfoServiceClient()
    movie = info_service.get_item(movie_id)
    return ResponseBuilder.build_json_response(movie)


@app.route("/movies/external/<movie_id>")
def get_movie_from_external_information_api(movie_id):
    return "Hello World!"


def main():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    main()
