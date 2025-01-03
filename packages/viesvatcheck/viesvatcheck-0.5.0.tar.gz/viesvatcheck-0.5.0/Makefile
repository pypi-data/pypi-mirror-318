ruff:
	ruff .

test:
	pytest tests/

mypy:
	python -m mypy src/viesvatcheck/ --ignore-missing-imports

lint: test ruff mypy