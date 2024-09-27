.PHONY: build
build:
	docker compose build --no-cache

.PHONY: run-dev
run-dev: 
	docker compose up --force-recreate dev

.PHONY: run-prod
run-prod:
	docker compose up --force-recreate prod

.PHONY: format
format:
	docker compose run --rm --no-deps base-image sh -c '\
		python -m ruff format'

.PHONY: test tests
test: static-tests pytest
 
.PHONY: static-tests
static-tests:
	docker compose run --rm --no-deps base-image sh -c '\
		python -m ruff service && \
		python -m mypy service'

.PHONY: pytest
pytest:
	docker compose run --rm --no-deps test sh -c '\
		pytest -vv --failed-first --cov-report=html $(test)'
