from docker_wrapper import Docker
from pprint import pprint

# Goals: Loop: Select container (or exit), then menu to do stuff to container (start, stop, rm, list info, go back to main menu)
while True:
    # Main Menu
    print('Select the container to manage:')
    containers = Docker.containers()
    for i in range(len(containers)):
        print(f'  {i} - {containers[i]}')
    print('  q - quit')
    
    selection = input()
    print()

    if selection == 'q':
        exit(0)
    
    while True:
        # Container Menu
        container = containers[int(selection)]
        print()
        print(f'You selected {container}. What would you like to do with it?')
        print(f'  view - View container info - (docker {container} list)')
        print(f'  start - Starts the container (docker start {container})')
        print(f'  stop - Stops the container (docker stop {container}')
        print(f'  rm - Deletes the container (docker rm {container})')
        print( '  menu - Back to the main menu')
    
        selection = input()

        if selection == 'menu':
            break

        elif selection == 'view':
            pprint(Docker.container_info(container))  # TODO: Make better, custom printer later

        elif selection == 'start':
            status = Docker.start(container)
            if status == '0':
                print(f'{container} started successfully')
            else:
                print(f'{container} did NOT start successfully. Exit code: {status}')

        elif selection == 'stop':
            status = Docker.stop(container)
            if status == '0':
                print(f'{container} stopped successfully')
            else:
                print(f'{container} was NOT stopped successfully. Exit code: {status}')

        elif selection == 'rm':
            while selection != 'y' and selection != 'n' and selection != 'Y' and selection != 'N':
                print(f'WARNING! This will DELETE {container}!')
                print(f'Are you absolutely sure you want to delete {container}? (y/N)')
                selection = input()
                if selection == 'y' or selection == 'Y':
                    print('Deleting...')
                    status = Docker.rm(container)
                    # TODO: Add status logic
                    print('Done')
                elif selection == 'n' or selection == 'N':
                    print(f'Operation cancelled, returning to {container} menu...')

        elif selection == 'menu':
            print('Returning to main menu...')
            break

        else:
            print('Selection invalid. Please try again.')
        print()
