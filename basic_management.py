import docker_wrapper

# Goals: Loop: Select container (or exit), then menu to do stuff to container (start, stop, rm, list info, go back to main menu)
while True:
    print('Select the container to manage:')
    for container in docker_wrapper.Docker.containers():
        print(f'  {container}')
