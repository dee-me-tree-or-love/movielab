from invoke import task

from lookup import meta_settings as LOOKUP

SERVICES = {
    'lookup': LOOKUP
}

DOCKER_BUILD_COMMAND = 'docker-compose build'
DOCKER_START_COMMAND = 'docker-compose up'


def concatenate_commands(*commands):
    if not commands:
        return ''
    else:
        command = ' && '.join(str(c) for c in commands)
        return command


def get_service_meta(key):
    try:
        return SERVICES[key]
    except:
        return False


def get_service_start_command(service_meta):
    try:
        return service_meta.get_start_command()
    except:
        message = 'failed: no start command for service in meta configuration'
        return "echo '%s'" % message


@task
def start(c, service=''):
    ''' Starts a specific service
    '''
    command = "echo 'did not manage to start the service'; exit 1"
    if(service):
        service_meta = get_service_meta(service)
        command = get_service_start_command(service_meta)

    c.run(command)


@task
def build_docker(c):
    ''' Builds the composer containers for the project
    '''
    command = DOCKER_BUILD_COMMAND
    c.run(command)


@task
def start_docker(c, force=False):
    ''' Starts the composition of services in docker-composition.
    By default builds the containers before running.
    Pass force argument to run without building
    '''
    build = DOCKER_BUILD_COMMAND
    start = DOCKER_START_COMMAND
    command = start if force else concatenate_commands(build, start)
    c.run(command)
