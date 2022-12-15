from subprocess import getoutput

# Goals: Loop: Select container (or exit), then menu to do stuff to container (start, stop, rm, list info, go back to main menu)


def docker_info():
    """
    Gets info about all the Docker containers
    :return: Nested dict of containers info
    """
    raw_info = getoutput('docker ps')
    # Header: "CONTAINER ID    IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES" (with way more spaces)
    header = raw_info[:raw_info.find('\n')+1]
    header_indices = {'CONTAINER ID': header.find('CONTAINER ID'), 'IMAGE': header.find('IMAGE'), \
        'COMMAND': header.find('COMMAND'), 'CREATED': header.find('CREATED'), 'STATUS': header.find('STATUS'), \
        'PORTS': header.find('PORTS'), 'NAMES': header.find('NAMES')}

    # Remove header (example above)
    raw_info = raw_info[raw_info.find('\n')+1:]
    info = {}

    # Find container names
    containers = []
    for line in raw_info.split('\n'):
        containers.append(line.strip()[line.strip().rfind(' ')+1:])

    # Fill in info
    for i in range(len(containers)):
        info[containers[i]] = {}
        header_indices_keys = list(header_indices)
        for j in range(len(header_indices_keys)):  # TODO: Fix
            start_i = header_indices[header_indices_keys[j]]
            if j+1 != len(header_indices):
                end_i = header_indices[header_indices_keys[j+1]]
            else:
                end_i = len(header)
            info[containers[i]][header_indices[header_indices_keys[j]]] = \
                raw_info.split('\n')[i][start_i:end_i].strip()

    return info


if '\n' not in getoutput('docker ps'):
    print('No containers running')
    exit()
docker_info()
