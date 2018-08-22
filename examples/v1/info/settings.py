from domain import DOMAIN

# mongo connection string
# see https://docs.mongodb.com/manual/reference/connection-string/
MONGO_URI = 'mongodb://127.0.0.0:27017/movielab-info'


# methods allowed at the resource (collection) endpoint
# POST = add new document(s)
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']


# methods allowed at the item (document) endpoint
# PATCH = edit a document
# PUT = replace a document
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# CORS support
# Allow access from all domains (javascript/web clients)
# see https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
X_DOMAINS = '*'

# Enabling the debug mode
DEBUG = True


def main():
    print(DOMAIN)


if __name__ == '__main__':
    main()
