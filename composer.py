import os
from subprocess import getoutput

debug = True

# Read config file and make variables
config = open('docker-composer.conf', 'rt')
working_dir = os.getcwd()

compose_path = config.readline()
compose_path = compose_path[compose_path.find('=')+1:].strip()
if compose_path[-1:] != '/':
    compose_path += '/'

exclude_containers = config.readline()
exclude_containers = [container.strip() for container \
in exclude_containers[exclude_containers.find('=')+1:].split(',')]

compose_dirs = []
for dir in os.listdir(compose_path):
    if os.path.isdir(compose_path + dir) and dir not in exclude_containers:
        compose_dirs.append(compose_path + dir + '/')

# Print debug info
if debug:
    print('Working directory: ' + working_dir)
    print('Compose path: ' + compose_path)
    print('Exclude containers: ' + str(exclude_containers))
    print('Compose directories: ' + str(compose_dirs))

# COMPOSE!
for dir in compose_dirs:
    container_name = dir[:-1][dir[:-1].rfind('/')+1:]
    if debug:
        print('Compose dir: ' + dir)
        print('Container name: ' + container_name)
    getoutput(f'docker stop {container_name}')
    getoutput(f'docker rm {container_name}')

    os.chdir(dir)
    output = getoutput('docker compose up -d')
    if debug:
        print(output)
