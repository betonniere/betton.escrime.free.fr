.SILENT:

.PHONY: install_env store restore run

PYTHON = ./venv/bin/python

install_env:
	python -m venv venv
	$(PYTHON) -m pip install django django-distill rich django-ckeditor

store:
	$(PYTHON) manage.py dumpdata \
		--exclude auth.permission \
		--exclude contenttypes \
		--exclude admin \
		--exclude auth.user \
		--exclude sessions \
		--indent 2 > archive.json

restore:
	$(PYTHON) manage.py makemigrations website
	$(PYTHON) manage.py migrate
	$(PYTHON) manage.py loaddata archive.json

edit_version:
	gvim website/templatetags/release_filters.py

run:
	$(PYTHON) manage.py runserver 0:8080
