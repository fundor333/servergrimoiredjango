SHELL := /bin/bash


.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: install
install:  ## Make venv and install requirements
	poetry install
	poetry run pre-commit install
	poetry run pre-commit autoupdate

migrate: ## Make and run migrations
	poetry run python manage.py makemigrations

static: ## Make a collect static of the module
	poetry run python manage.py collectstatic

.PHONY: test
test: ## Run tests
	poetry run python manage.py test application --verbosity=0 --parallel --failfast

.PHONY: run
run: ## Run the Django server
	poetry run python manage.py runserver

start: install migrate run ## Install requirements, apply migrations, then start development server
