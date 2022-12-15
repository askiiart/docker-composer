import os
from subprocess import getoutput
from docker_wrapper import Docker

# Read config file and make variables
config = open('docker-composer.conf', 'rt')
working_dir = os.getcwd()

compose_path = config.readline()
compose_path = compose_path[compose_path.find('=')+1:].strip()
if compose_path[-1:] != '/':
    compose_path += '/'
if compose_path[1] != '/':
    compose_path = f'{working_dir}/{compose_path}'

exclude_containers = config.readline()
exclude_containers = [container.strip() for container \
in exclude_containers[exclude_containers.find('=')+1:].split(',')]

compose_dirs = []
for dir in os.listdir(compose_path):
    if os.path.isdir(compose_path + dir) and dir not in exclude_containers:
        compose_dirs.append(compose_path + dir + '/')

containers = []
for dir in compose_dirs:
    containers.append()

# COMPOSE!
for i in range(len(compose_dirs)):
    dir = compose_dirs[i]
    container = containers[i]
    status = Docker.stop(container)  # Assigned to vars so I can see 
    if status != 0:
        print(f'Error in stopping {container}, skipping...')
    status = Docker.rm(container)
    if status != 0:
        print(f'Error in removing {container}, skipping...')
    status = Docker.compose(dir)
    if status != 0:
        print(f'Error in composing {container}, skipping...')
