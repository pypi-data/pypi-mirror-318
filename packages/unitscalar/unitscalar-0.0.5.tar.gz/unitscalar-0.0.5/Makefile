build:
	python3 -m build

version = $(shell cat pyproject.toml | grep "version" | grep -oP '(?<=\").*(?=\")')
install: build
	pip install --force-reinstall dist/unitscalar-$(version)-py3-none-any.whl
