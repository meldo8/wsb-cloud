PYTHON=python3

.PHONY: build
build:
	@docker-compose up --build -d --force-recreate

.PHONY: up
up:
	@docker-compose up

.PHONY: stop
stop:
	@docker-compose down --remove-orphans

.PHONY: logs
logs:
	@docker-compose logs -f

.PHONY: mypy
mypy:
	@docker-compose exec backend mypy .
