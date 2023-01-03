import os
from docker_wrapper import Docker

debug = False

# Read config file and make variables
config = open('docker-composer.conf', 'rt')
working_dir = os.getcwd()

compose_path = config.readline()
compose_path = compose_path[compose_path.find('=')+1:].strip()
if compose_path[-1:] != '/':
    compose_path += '/'
if compose_path[0] != '/':
    compose_path = f'{working_dir}/{compose_path}'

exclude_containers = config.readline()
exclude_containers = [container.strip() for container \
in exclude_containers[exclude_containers.find('=')+1:].split(',')]

compose_dirs = []
for dir in os.listdir(compose_path):
    if os.path.isdir(compose_path + dir) and dir not in exclude_containers and dir[0] != '.':
        compose_dirs.append(compose_path + dir + '/')

containers = [dir[:-1][dir[:-1].rfind('/')+1:] for dir in compose_dirs]


# Print debug info
if debug:
    print('Working directory: ' + working_dir)
    print('Compose path: ' + compose_path)
    print('Exclude containers: ' + str(exclude_containers))
    print('Compose directories: ' + str(compose_dirs))

running = True
while running:
    # Menu
    print('What Docker container would you like to (re-)compose?')
    for i in range(len(containers)):
        print(f'  {i} - {containers[i]}')
    print('  q - quit')

    to_compose_i = input()
    if to_compose_i == 'q':
        exit(0)
    to_compose_i = int(to_compose_i)

    # COMPOSE!
    container = containers[to_compose_i]
    container_dir = compose_dirs[to_compose_i]
    Docker.stop(container)
    Docker.rm(container)
    Docker.compose(container_dir)
    
    print('\nWould you like to (re-)compose another container? (y/N)')
    running = True if input() == 'y' else False
