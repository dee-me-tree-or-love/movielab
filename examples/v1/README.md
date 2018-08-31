# Version 1

`v1` example is built using minimalistic services written mainly in _Python_.

## Services
- `info` - REST API service for the movie info
- `lookup` - API gateway managin movie retrieval
- `proxy` - Proxy to a 3rd party movie API

## Getting started  

### Building and local running  
Most of the commands needed to start the services can be executed using the [`invoke`](#tooling).  
- get a single service* running - `invoke start -s <service name>` 
- get the whole system** running - `invoke start-docker`
- build the whole system - `invoke build-docker`  

These and other commands are defined in `tasks.py`. 
Keep in mind that `invoke` commands should be run from within the directory containing the `tasks.py` file.  

\*: the start of a single service is handled via the defined start commands per each service in `meta_settings.py`  
\*\*: The _whole system_ in this case is the collection of services as described in `docker-compose.yml`  

### Local services  
To access the services running as _docker containers_ from the host machine, one can send `http` requests to the `localhost` address with the specific port.  
- on _*nix_ platforms one should be able to access the services via `curl http://localhost:<service port>/<resources>`  
- on _windows_, from personal experience, the connection should be established using the IP of the docker machine, _(in my case ``92.168.99.100`)_, running on the host: `curl http://<docker-machine IP>:<service port>/<resources>`  


## Details  

### Tooling
- [`invoke`](http://www.pyinvoke.org/index.html) - a tool for python task execution:
_see the `tasks.py` for the executable tasks_ 

- [`virtualenv`](https://virtualenv.pypa.io/en/stable/) - a virtual environment manager for python:
  - _setup the virtual environment somewhere like [`virtualenv venv`](https://virtualenv.pypa.io/en/stable/userguide/#usage)_
  - _activate* the virtual environment with: [`. ./venv/bin/activate`](https://virtualenv.pypa.io/en/stable/userguide/#activate-script)_
  - _install the dependencies** in `requirements.txt`: [`pip install -r requirements.txt`](https://virtualenv.pypa.io/en/stable/userguide/#usage)_


\*: Depends on your platform, see the [docs](https://virtualenv.pypa.io/en/stable/userguide/#activate-script) for more information  
\*\*: The `requirements.txt` contains the combined dependencies of all the python-based services in `v1`