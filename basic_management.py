import docker_wrapper
import pprint

# Goals: Loop: Select container (or exit), then menu to do stuff to container (start, stop, rm, list info, go back to main menu)
pprint.pprint(docker_wrapper.Docker.ps())
pprint.pprint(docker_wrapper.Docker.containers_info())
