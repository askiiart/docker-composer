from subprocess import getoutput, getstatusoutput
import pprint
import os

class NoContainersError(Exception):
    pass

class Docker:
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
    
    def container_list(raw_info=getoutput('docker container list')):
        """
        Gets info about all the Docker containers
        :return: Nested dict of containers info
        """
        if '\n' not in raw_info:
            raise(NoContainersError('A Docker container is required to run this program. Please create a docker container and try again.'))
        raw_info = getoutput('docker container list')
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
    
    def compose(dir):
        """
        Composes whatever is in dir
        :parameters:
        dir: The directory of a container; must contain docker-compose.yml file

        :returns:
        tuple: (exit_code, compose_output)
        """
        cwd = os.getcwd()
        os.chdir(dir)
        status = getstatusoutput('docker ps')
        os.chdir(cwd)
        return status
    
    def start(container):
        """
        Starts a container
        :parameters:
        container: The name of the container to start

        :returns:
        int: The exit code of docker start
        """
        return getstatusoutput(f'docker start {container}')[0]
    
    def stop(container):
        """
        Stops a container
        :parameters:
        container: The name of the container to stop

        :returns:
        int: The exit code of docker stop
        """
        return getstatusoutput(f'docker stop {container}')[0]
    
    def rm(container):
        """
        Deletes a container
        :parameters:
        container: The name of the container to remove

        :returns:
        int: The exit code of docker rm
        """
        return getstatusoutput(f'docker rm {container}')[0]


if __name__ == '__main__':
    try:
        pprint.pprint(Docker.containers_info())
    except NoContainersError as e:
        print(e)
