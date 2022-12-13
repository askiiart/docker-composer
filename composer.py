import os

sudo_needed = True
if os.system('whoami') != 'root' && sudo_needed:
  print('Please rerun as root so I can access docker')

config = open('.config', 'rt')
working_dir = os.getcwd()
print(working_dir)

compose_path = config.readline()
compose_path = compose_path[compose_path.find('=')+1:].strip()
if compose_path[-1:] != '/':
    compose_path += '/'

exclude_containers = config.readline()
exclude_containers = [container.strip() for container in exclude_containers[exclude_containers.find('=')+1:].split(',')]

compose_dirs = []
for dir in os.listdir(compose_path):
  if os.path.isdir(dir):
    compose_dirs.append(compose_path + dir + '/')

# COMPOSE!
for dir in compose_dirs:
  os.chdir(dir)
  os.system('docker compose lorem ipsum idk')
