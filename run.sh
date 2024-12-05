#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <single|multiple>"
  exit 1
fi

# Execute commands based on the argument
case $1 in
  single)
    echo "Stopping the multiple container setup..."
    docker compose -f docker-compose-multiple.yml down

    echo "Starting the single container setup..."
    docker compose -f docker-compose-single.yml up --build -d
    ;;

  multiple)
    echo "Stopping the single container setup..."
    docker compose -f docker-compose-single.yml down

    echo "Starting the multiple container setup..."
    docker compose -f docker-compose-multiple.yml up --build -d
    ;;

  *)
    echo "Invalid option. Use 'single' or 'multiple'."
    exit 1
    ;;
esac
