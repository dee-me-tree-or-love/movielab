# Version 1

`v1` example is built using minimalistic services written mainly in _Python_.

## Services
- `info` - REST API service for the movie info
- `lookup` - API gateway managin movie retrieval
- `proxy` - Proxy to a 3rd party movie API

## Tooling
- [`invoke`](http://www.pyinvoke.org/index.html) - a tool for python task execution:
_see the `tasks.py` for the executable tasks_ 

- [`virtualenv`](https://virtualenv.pypa.io/en/stable/) - a virtual environment manager for python:
  - _setup the virtual environment somewhere like [`virtualenv venv`](https://virtualenv.pypa.io/en/stable/userguide/#usage)_
  - _activate* the virtual environment with: [`. ./venv/bin/activate`](https://virtualenv.pypa.io/en/stable/userguide/#activate-script)_
  - _install the dependencies** in `requirements.txt`: [`pip install -r requirements.txt`](https://virtualenv.pypa.io/en/stable/userguide/#usage)_


\*: Depends on your platform, see the [docs](https://virtualenv.pypa.io/en/stable/userguide/#activate-script) for more information  
\*\*: The `requirements.txt` contains the combined dependencies of all the python-based services in `v1`