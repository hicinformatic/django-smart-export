PYTHON=python
VENV=venv
ACTIVATE=. $(VENV)/bin/activate

# Create virtual environment and install dependencies
venv:
	@if [ ! -d "$(VENV)" ]; then \
		$(PYTHON) -m venv $(VENV); \
	fi
	$(ACTIVATE) && pip install -U pip setuptools wheel
	$(ACTIVATE) && pip install -e .[dev]

# Direct installation (without creating venv)
install:
	$(PYTHON) -m pip install -e .[dev]

# Lancer les tests avec pytest
test:
	$(VENV)/bin/pytest

test-django:
	PYTHONPATH=$(shell pwd) $(VENV)/bin/pytest --ds=tests.settings

# Check code style with ruff
lint:
	$(VENV)/bin/ruff django_deep/ tests/

# Formatte le code avec black
format:
	$(VENV)/bin/black django_deep/ tests/

migrations:
	$(VENV)/bin/python manage.py makemigrations

django-shell:
	$(VENV)/bin/python manage.py shell

# Nettoyage des fichiers temporaires
clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache .coverage dist build *.egg-info
