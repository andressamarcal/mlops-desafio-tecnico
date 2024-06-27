.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using poetry"
	@poetry install
	@poetry run pre-commit install
	@poetry shell

.PHONY: check
check: ## Run pre-commit and flake8 checks
	@poetry run pre-commit run --all-files
	@poetry run flake8 src tests

.PHONY: test
test: ## Run tests with coverage
	@poetry run pytest --cov=src --cov-fail-under=70

.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@rm -rf dist

.PHONY: publish
publish: ## Publish a release to PyPI.
	@echo "🚀 Publishing: Dry run."
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

.PHONY: train
train: ## Train the model
	@echo "🚀 Training the model"
	@PYTHONPATH=$(PWD)/src poetry run python src/desafio1/models/ml/iris_train.py

.PHONY: api
api: ## Start FastAPI server
	@echo "🚀 Starting FastAPI server"
	@PYTHONPATH=$(PWD)/src poetry run uvicorn src.desafio1.api.v1.main:app --host 0.0.0.0 --port 8000 --reload

.PHONY: docs
docs: ## Build and serve the documentation
	@poetry run mkdocs serve

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
