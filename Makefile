.PHONY: lint test migrate up down

lint:
	ruff check src/
	mypy src/

test:
	pytest tests/ -v

migrate:
	alembic upgrade head

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

shell:
	docker-compose exec api bash
