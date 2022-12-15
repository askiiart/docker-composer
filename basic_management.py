from docker_wrapper import Docker
from pprint import pprint

while True:
    # Main Menu
    print('Select the container to manage:')
    containers = Docker.containers()
    for i in range(len(containers)):
        print(f'  {i} - {containers[i]}')
    print('  q - quit')
    
    container_i = input()
    print()

    if container_i == 'q':
        exit(0)
    
    while True:
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
            pprint(Docker.container_info(container))  # TODO: Make better, custom printer

        elif selection == 'start':
            print('Starting...')
            status = Docker.start(container)
            
        elif selection == 'stop':
            print('Stopping...')
            status = Docker.stop(container)
            print('Done.')
            
        elif selection == 'rm':
            break_later = False
            while selection != 'y' and selection != 'n' and selection != 'Y' and selection != 'N':
                print(f'WARNING! This will DELETE {container}!')
                print(f'Are you absolutely sure you want to delete {container}? (y/N)')
                selection = input()
                if selection == 'y' or selection == 'Y':
                    print('Deleting...')
                    status = Docker.rm(container)
                    print('Done')
                    break_later = True
                elif selection == 'n' or selection == 'N':
                    print(f'Operation cancelled, returning to {container} menu...')
            if break_later:
                break

        elif selection == 'menu':
            print('Returning to main menu...')
            break

        else:
            print('Selection invalid. Please try again.')
        print()
