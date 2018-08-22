# see http://python-eve.org/index.html
from eve import Eve

app = Eve(auth=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
