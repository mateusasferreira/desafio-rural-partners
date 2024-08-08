.PHONY: help
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

build: # Builda a imagem docker da API
	@echo "--> Building Compose"
	docker compose build

build-no-cache: # Builda a imagem docker ignorando cache
	@echo "--> Building Compose"
	docker compose build --no-cache

run: # Sobe um servidor local via docker
	@echo "--> Running the project"
	docker compose up

kill: # Destroi os container ativos
	@echo "--> Killing the container"
	docker compose down

test: # Roda testes unitários e de integração
	@echo "--> Testing on Docker."
	docker compose run app pytest

migrations: # Cria migração de banco de dados a partir de alteração nos models
	@echo "--> Creating Migrations"
	docker compose run app python src/manage.py makemigrations

migrate: # Aplica migrações e seedings pendentes
	@echo "--> Building Compose"
	docker compose run app python src/manage.py migrate


superuser: # Cria um super usuário para acesso ao admin
	@echo "--> Building Compose"
	docker compose run app python src/manage.py createsuperuser

testtoken: # Cria um token de autenticação para ambiente local
	docker compose run app python src/manage.py createtesttoken

bash: # Abre um terminal dentro da imagem docker da API
	docker compose run app bash
