from subprocess import getoutput
import pprint

class NoContainersError(Exception):
    pass

class DockerParser:
    def ps(raw_info=getoutput('docker ps')):
        """
        Gets info about all running Docker containers from docker ps
        :return: Nested dict of containers info
        """
        if '\n' not in raw_info:
            raise(NoContainersError('A Docker container is required to run this program. Please create a docker container and try again.'))
        raw_info = getoutput('docker ps')
        # Header: "CONTAINER ID    IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES" (with way more spaces)
        header = raw_info[:raw_info.find('\n')+1]
        header_indices = {'CONTAINER ID': header.find('CONTAINER ID'), 'IMAGE': header.find('IMAGE'),
                        'COMMAND': header.find('COMMAND'), 'CREATED': header.find('CREATED'), 'STATUS': header.find('STATUS'),
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
                info[containers[i]][header_indices_keys[j]] = \
                    raw_info.split('\n')[i][start_i:end_i].strip()

        return info
    
    def containers_info(raw_info=getoutput('docker container list')):
        """
        Gets info about all the Docker containers
        :return: Nested dict of containers info
        """
        if '\n' not in raw_info:
            raise(NoContainersError('A Docker container is required to run this program. Please create a docker container and try again.'))
        raw_info = getoutput('docker container list')
        # Header: "CONTAINER ID    IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES" (with way more spaces)
        header = raw_info[:raw_info.find('\n')+1]
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
        for line in raw_info.split('\n'):
            containers.append(line.strip()[line.strip().rfind(' ')+1:])
        
        # Fill in info
        for i in range(len(containers)):
            info[containers[i]] = {}
            for column in header_indices:
                end_i = header_indices[column] + len(column)
                info[containers[i]][column] = raw_info[i][header_indices[column]:end_i]

        return info


if __name__ == '__main__':
    try:
        pprint.pprint(DockerParser.containers_info())
    except NoContainersError as e:
        print(e)
