from subprocess import getoutput
import docker_parser
import pprint

# Goals: Loop: Select container (or exit), then menu to do stuff to container (start, stop, rm, list info, go back to main menu)
pprint.pprint(docker_parser.DockerParser.ps())
