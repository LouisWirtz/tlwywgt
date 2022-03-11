install:
	poetry install

style: install
	poetry run isort app
	poetry run flake8 app
	poetry run pydocstyle app
	poetry rn mypy -p app
