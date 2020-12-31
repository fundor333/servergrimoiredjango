SHELL := /bin/bash


.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: env
env:  ## Make venv and install requirements for automation
	pip install poetry
	poetry install

.PHONY: install
install: env ## Make venv and install requirements
	poetry run pre-commit install
	poetry run pre-commit autoupdate

migrate: ## Make and run migrations
	poetry run python manage.py makemigrations

static: ## Make a collect static of the module
	poetry run python manage.py collectstatic

.PHONY: test
test: ## Run tests
	DJANGO_SETTINGS_MODULE=servergrimoire.tests.settings poetry run py.test -s servergrimoire/tests --cov=servergrimoire --cov-report=xml

.PHONY: coverage
coverage: test ## Make coverage
	coverage report -i -m
	coverage html

.PHONY: run
run: ### Run the project
	poetry run python manage.py runserver

start: install migrate run ## Install requirements, apply migrations, then start development server
