from subprocess import getoutput

# Goals: Loop: Select container (or exit), then menu to do stuff to container (start, stop, rm, list info, go back to main menu)


def docker_info():
    """
    Gets info about all the Docker containers
    :return: Nested dict of containers info
    """
    raw_info = getoutput('docker ps')
    # Header: "CONTAINER ID    IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES" (with way more spaces)
    header = raw_info[:raw_info.find('\n')]
    header_temp = header
    header_indices = {}
    while '  ' in header_temp:  # Split header
        temp = header_temp[header_temp.rfind('  ')+2:].strip()
        header_indices[temp] = header.find(temp)
        header_temp = header_temp[:header_temp.rfind('  ')].strip()
    header_indices[header[:header.find('  ')]] = 0

    raw_info = raw_info[raw_info.find('\n')+1:]  # Remove header (example above)
    info = {}
    
    # Find container names
    containers = []
    for line in raw_info:
        containers.append(line.strip()[line.strip().rfind(' ')+1:])
    
    # Fill in info
    for container in containers:
        info[container] = {}
        for column in header_indices:
            end_i = header_indices[column] + len(column)
            info[container][column] = header[header_indices[column]:end_i]
    
    debug = True
    if debug:
        print('Raw info:\n', raw_info)
        print('Header:\n', header)
        print('Header indices:\n', header_indices)
        print('Containers:\n', containers)
        print('Info:\n', info)

    return info


docker_info()
