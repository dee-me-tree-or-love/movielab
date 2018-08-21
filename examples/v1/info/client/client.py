''' The client used for testing purposes of the app
'''

import json
import requests  # see http://python-requests.org


def url_for(endpoint):
    return 'http://localhost:5000/{}/'.format(endpoint)


def delete_all_movies():
    r = requests.delete(url_for('movies'))
    print("'movies' deleted, server response:", r.status_code)


def post_movies():
    data = [
        {'title': 'Princess Mononoke', 'description': 'Doe'},
        {'title': 'Lord Of The Rings', 'description': 'Green'},
    ]

    response = requests.post(
        url_for('movies'),
        json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )
    print("'movies' posted, server response:", response.status_code)


def is_successful_response(response):
    return response.status_code == 200


def print_movies_information(movies):
    print('{} movies:'.format(len(movies)))
    for movie in movies:
        # print(movie)
        print('{}, {}'.format(movie['title'], movie['_id']))


def get_movies():
    r = requests.get(url_for('movies'))
    print('movies downloaded, server response:', r.status_code)

    if is_successful_response(r):
        movies = r.json()['_items']
        print_movies_information(movies)


def main():
    delete_all_movies()
    post_movies()
    get_movies()


if __name__ == '__main__':
    main()
