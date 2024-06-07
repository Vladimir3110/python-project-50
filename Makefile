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

generate:
	poetry run gendiff file1.json file2.json

pytest:
	poetry run  pytest

lint-tests:
	poetry run flake8 tests/

check: lint pytest

test-coverage:
       pytest --cov=./ --cov-report=xml .

.PHONY: test test-coverage
