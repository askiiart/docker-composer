from subprocess import getoutput
import pprint

class NoContainersError(Exception):
    pass

class DockerParser:
    def containers_info(raw_info=getoutput('docker container list')):
        """
        Gets info about all the Docker containers
        :return: Nested dict of containers info
        """
        if '\n' not in raw_info:
            raise(NoContainersError('A Docker container is required to run this program. Please create a docker container and try again.'))
        raw_info = getoutput('docker ps')
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
