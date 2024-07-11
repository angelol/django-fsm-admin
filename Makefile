.PHONY: clean-build clean-pyc clean

VERSION := $(shell python setup.py --version)

all:
	@echo

version:
	@echo "fsm_admin.__version__ == $(VERSION)"

help:
	@echo " Make targets"
	@echo
	@echo " * clean       - runs clean-build & clean-pyc"
	@echo " * clean-build - remove build artifacts"
	@echo " * clean-pyc   - remove Python file artifacts"
	@echo " * dist        - package"
	@echo " * help        - print this targets list"
	@echo " * release     - package and upload a release"
	@echo " * version     - print the current value of fsm_admin.__version__"
	@echo " * lint        - Running static code analysis"
	@echo " * format      - Auto-formatting with ruff"
	@echo

clean: clean-build clean-pyc

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info
	@rm -fr fsm_admin/VERSION

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +

dist: clean
	@python  setup.py sdist bdist_wheel
	@twine check dist/*

release: clean
	@python setup.py sdist bdist_wheel
	@twine check dist/*
	@twine upload dist/*

lint:
	@ruff format --check .
	@ruff check .

format:
	@ruff format .
	@ruff check . --fix
