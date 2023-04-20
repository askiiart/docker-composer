#!/bin/bash

if [ ! "$BASH_VERSION" ]; then
  echo "Error: This script must be run with bash. Rerun using bash." >&2
  exit 1
fi

# Read config file and make variables
working_dir=$(pwd)
compose_path=$(awk -F "=" '/^compose_path/ {gsub(/\/$/, "", $2); print ($2 ~ /^\// ? $2 : "'"${working_dir}"'/"$2)}' docker-composer.conf)
exclude_containers=$(awk -F "=" '/^exclude_containers/ {gsub(/ /, "", $2); print $2}' docker-composer.conf | tr ',' ' ')

# Get compose directories
compose_dirs=()
for dir in "${compose_path}"*; do
  if [[ -d "${dir}" && "${dir##*/}" != .* && ! " ${exclude_containers[@]} " =~ " ${dir##*/} " ]]; then
    compose_dirs+=("${dir}/")
  fi
done

# Get containers
containers=()
for dir in "${compose_dirs[@]}"; do
  container="${dir%/}"
  container="${container##*/}"
  containers+=("${container}")
done

# COMPOSE!
for i in "${!compose_dirs[@]}"; do
  dir="${compose_dirs[i]}"
  container="${containers[i]}"
  echo "COMPOSING ${container}..."
  docker compose -f "${dir}docker-compose.yml" up -d
  echo "DONE!"
done
