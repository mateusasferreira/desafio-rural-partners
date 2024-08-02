.PHONY: help
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

build: # Build the project image
	@echo "--> Building Compose"
	docker compose build

build-no-cache: # Build the project image ignoring the cache
	@echo "--> Building Compose"
	docker compose build --no-cache

run: # Runs the project
	@echo "--> Running the project"
	docker compose up

kill: # Destroys the container
	@echo "--> Killing the container"
	docker compose down

test: # Run tests
	@echo "--> Testing on Docker."
	docker compose run app pytest

migrations: # Create Database Migrations
	@echo "--> Creating Migrations"
	docker compose run app python src/manage.py makemigrations

migrate: # Run migrations
	@echo "--> Building Compose"
	docker compose run app python src/manage.py migrate


superuser: # Creates a super-user for django
	@echo "--> Building Compose"
	docker compose run app python src/manage.py createsuperuser


bash: # Opens a bash terminal inside the docker container
	docker compose run app bash

