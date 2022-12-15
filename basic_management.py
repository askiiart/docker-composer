from docker_wrapper import Docker, NoContainersError
from subprocess import getoutput


def container_to_str(container):
    """
    Returns info about a Docker container as a string
    :parameters:f
    container: The name of the container (str)

    :returns:
    str: The container info as a string, formatted for printing
    """
    # Header: "CONTAINER ID    IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES" (with way more spaces)
    info = Docker.container_info(container)
    info_str = f'{container}\n'
    info_str += f'  CONTAINER ID: {info["CONTAINER ID"]}\n'
    info_str += f'  IMAGE: {info["IMAGE"]}\n'
    info_str += f'  COMMAND: {info["COMMAND"]}\n'
    info_str += f'  CREATED: {info["CREATED"]}\n'
    info_str += f'  STATUS: {info["STATUS"]}\n'
    info_str += f'  PORTS: {info["PORTS"]}\n'
    info_str += f'  NAMES: {info["NAMES"]}'

    return info_str

try:
    while True:
        if not Docker.containers_exist():
            raise(NoContainersError('No containers exist! Please create a container and try again.'))

        # Main Menu
        print('Select the container to manage:')

        containers = Docker.containers()
        for i in range(len(containers)):
            print(f'  {i} - {containers[i]}')
        print('  q - Quit')

        container_i = input()
        print()

        if container_i == 'q':
            exit(0)

        while True:
            if not Docker.containers_exist():
                raise(NoContainersError('No containers exist! Please create a container and try again.'))
            # Container Menu
            container = containers[int(container_i)]
            print()
            print(f'You selected {container}. What would you like to do with it?')
            print(f'  view - View container info - (docker ps -a)')
            print(f'  start - Starts the container (docker start {container})')
            print(f'  stop - Stops the container (docker stop {container}')
            print(f'  rm - Deletes the container (docker rm {container})')
            print( '  menu - Back to the main menu')

            selection = input()
            print()

            if selection == 'menu':
                break

            elif selection == 'view':
                print(container_to_str(container))

            elif selection == 'start':
                print('Starting...')
                Docker.start(container)

            elif selection == 'stop':
                print('Stopping...')
                Docker.stop(container)
                print('Done')

            elif selection == 'rm':
                break_later = False
                while selection != 'y' and selection != 'n' and selection != 'Y' and selection != 'N':
                    print(f'WARNING! This will DELETE {container}!')
                    print(
                        f'Are you absolutely sure you want to delete {container}? (y/N)')
                    selection = input()
                    if selection == 'y' or selection == 'Y':
                        print('Stopping...')
                        Docker.stop(container)
                        print('Deleting...')
                        Docker.rm(container)
                        print('Done')
                        break_later = True
                    elif selection == 'n' or selection == 'N':
                        print(f'Operation cancelled, returning to {container} menu...')
                if break_later:
                    print()
                    break

            elif selection == 'menu':
                print('Returning to main menu...')
                break

            else:
                print('Selection invalid. Please try again.')
            print()
except NoContainersError as e:
    print('Error:', e)
    print('No containers found. Exiting...')
    exit()
