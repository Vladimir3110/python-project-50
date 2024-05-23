install:
	poetry install

lint:
	poetry run flake8 gendiff

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

gendiff:
	poetry run gendiff -h
