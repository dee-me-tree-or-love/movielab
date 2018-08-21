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
    return "echo 'service meta configuration does not contain a start command'"

@task
def start(c, service=''):
    command = "echo 'did not manage to start the service'"
    if(service):
      service_meta = get_service_meta(service)
      command = get_service_start_command(service_meta)
    
    c.run(command)
