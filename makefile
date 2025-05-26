# Load environment variables from .env
include .env
export

# Default environment
ENV ?= development

.PHONY: up down build test lint format shell

up:
	docker-compose up -d --build

down:
	docker-compose down

build:
	docker-compose build

logs:
	docker-compose logs -f

test:
	pytest -v

lint:
	ruff check .

format:
	black .

shell:
	docker exec -it $(shell docker ps --filter "name=ielts-tutor" -q) /bin/bash

env:
	@echo "ENVIRONMENT: $(ENV)"
