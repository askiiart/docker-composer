import os

config = open('.config', 'rt')

compose-path = config.readline()
compose-path = compose-path[compose-path.find('=')+1:]
if compose-path[-1:] != '/':
    compose-path += '/'

exclude-containers = config.readline()
exclude-containers = exclude-containers[exclude-containers.find('=')+1:].split(',')

compose-paths = [compose-path + dir for dir in os.listdir(compose-path)]
