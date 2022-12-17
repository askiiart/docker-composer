# Docker Composer

This is a simple program to manage docker containers. It works similarly to Umbrel, but it is not limited to Umbrel. It can be used to manage any docker container.


## How to use
- **Note:** All scrips must be run in the same directory as the `docker-composer.conf` file.
- If you want to re-compose your containers on boot, you can run `composer.py` on boot
- If you want to re-compose your containers on demand, you can run `re_compose.py` manually
- If you just want to do basic management, like stopping, starting, removing docker containers, etc, then use `basic-management.py`. It's essentially an interactive wrapper for the basics of docker.


## Installation

Just put these scripts somewhere, and run them as needed. Remember to edit the `docker-composer.conf` file to your needs - parameters below, in [Usage](https://github.com/askiiart/docker-composer/edit/master/README.md#usage)


## Usage

`docker-composer.conf` parameters:
- `compose-path`: The path to the folder containing the folders for each docker container - the folder for each container includes a `docker-compose.yml` file.
- `exclude-containers`: A list of containers to exclude from being managed by the program. This will stop the scripts (except `basic_management.py`) from doing **anything** to those containers.

Notes:
- The folders *must* have the same name as their respective docker containers
- Remember to run the script as a user that can access Docker engine


## Status
- All scripts are complete and working! Feel free to use this now.
