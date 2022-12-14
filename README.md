# Docker Composer

This is a simple program to manage docker containers. It works similarly to Umbrel, but it is not limited to Umbrel. It can be used to manage any docker container.


## How to use
- **Note:** All scrips must be run in the same directory as the `docker-composer.conf` file.
- If you want to re-compose your containers on boot, you can run `composer.py` on boot
- If you want to re-compose your containers on demand, you can run `re_compose.py` manually
- If you just want to do basic management, like stopping, starting, removing docker containers, etc, then use `basic-management.py`. It's essentially an interactive wrapper for the basics of docker.


## Installation

I'll get to this later once this program is actually usable.

You can use `docker-data/` to test the program, or can put your own data there. `docker-composer.conf` is already set up to use that directory!


## Usage

`docker-composer.conf` parameters:
- `compose-path`: The path to the folder containing the folders for each docker container - the folder for each container includes a `docker-compose.yml` file.
  - **If you use relative paths**, use the folder you're in as `/`. For example, using the folder `docker-data` would be either `/docker-data` or `/path/to/this/repo/docker-data`. You can also have a "/" on the end of those paths, if you'd like; it's not required.
- `exclude-containers`: A list of containers to exclude from being managed by the program. This will stop the program from doing **anything** to those containers.

Notes:
- The folders *must* have the same name as their respective docker containers


## Dev Notes
- Maybe later expand this to an interactive docker manager.

## Status
- `composer.py` and `re_compose` are finished
- Haven't started on `basic_management.py`