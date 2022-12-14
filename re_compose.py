import os
from subprocess import getoutput

debug = False

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

running = True
while running:
    containers = [dir[:-1][dir[:-1].rfind('/')+1:] for dir in compose_dirs]
    # Menu
    print('What Docker container would you like to (re-)compose?')
    print('(q) - quit')
    for i in range(len(containers)):
        print(f'({i}) - {containers[i]}')
    to_compose_i = input()
    if to_compose_i == 'q':
        exit(0)
    to_compose_i = int(to_compose_i)

    # COMPOSE!
    container_name = containers[to_compose_i]
    if debug:
        print('Container name: ' + container_name)
    getoutput(f'docker stop {container_name}')
    getoutput(f'docker rm {container_name}')

    os.chdir(compose_dirs[to_compose_i])
    output = getoutput('docker compose up -d')
    if debug:
        print(output)
    
    print('\nWould you like to (re-)compose another container? (y/N)')
    running = True if input() == 'y' else False
