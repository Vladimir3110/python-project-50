install:
	poetry install

shell:
	poetry shell


test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff tests/

gendiff:
	poetry run gendiff -h

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint
