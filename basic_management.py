from subprocess import getoutput

# Goals: Loop: Select container (or exit), then menu to do stuff to container (start, stop, rm, list info, go back to main menu)


if '\n' not in getoutput('docker ps'):
    print('No containers running')
    exit()
ps()
