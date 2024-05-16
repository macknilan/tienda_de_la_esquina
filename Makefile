# Description: Makefile for Django project
# WIP

migrate:
	@echo "Migrating database..."
	python manage.py migrate

makemigrations:
	@echo "Creating migrations..."
	python manage.py makemigrations

collect:
	@echo "Collecting static files..."
	python manage.py collectstatic

run:
	@echo "Running server..."
	python manage.py runserver

run-npm:
	@echo "Running npm..."
	npm run dev
