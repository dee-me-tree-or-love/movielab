from domain import DOMAIN

# mongo connection details
# see https://docs.mongodb.com/manual/reference/connection-string/
MONGO_URI = 'mongodb://mongo:27017'
MONGO_USERNAME = 'root'
MONGO_PASSWORD = 'example'
MONGO_DBNAME = 'admin'

# methods allowed at the resource (collection) endpoint
# POST = add new document(s)
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# methods allowed at the item (document) endpoint
# PATCH = edit a document
# PUT = replace a document
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# IF-MATCH for concurrency and integrity control
# if set to true, each mutating request needs to be validated against an ETAG
# otherwise, no concurency and integrity control
# http://python-eve.org/features.html#data-integrity-and-concurrency-control
IF_MATCH = True

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
