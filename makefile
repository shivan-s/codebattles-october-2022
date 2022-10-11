# Run docker containers
.PHONY: run
run:
	docker-compose down --remove-orphans && \
	docker-compose up --build -d

# Attach to docker containers
.PHONY: attach
attach:
	docker-compose up

.PHONY: makemigrations
makemigrations:
	docker-compose up -d  && \
	docker exec -it codebattles-october-2022-api-app sh -c "python manage.py makemigrations"

.PHONY: migrate
migrate:
	docker-compose up -d  && \
	docker exec -it codebattles-october-2022-api-app sh -c "python manage.py migrate"

ARG=''
.PHONY: test
test:
	clear
	docker-compose up -d  && \
	docker exec -it codebattles-october-2022-api-app sh -c "pytest $(ARG)"

.PHONY: shell
shell:
	docker exec -it codebattles-october-2022-api-app sh -c "python manage.py shell"

.PHONY: generate-key
generate-key:
	@echo '' && \
	pipenv -q run python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
