from invoke import task

from lookup import meta_settings as LOOKUP

SERVICES = {
    'lookup': LOOKUP
}


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
    command = "echo 'did not manage to start the service'; exit 1"
    if(service):
        service_meta = get_service_meta(service)
        command = get_service_start_command(service_meta)

    c.run(command)


@task
def build(c, service=''):
    command = "echo 'build command is not set' ; exit 1"
    c.run(command)
