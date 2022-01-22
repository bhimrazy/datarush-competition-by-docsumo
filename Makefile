# Makefile
SHELL := /bin/bash

.PHONY: help
help:
	@echo "Commands:"
	@echo "venv    : creates development environment."
	@echo "install : Installs all packages."
	@echo "dataset : downloads dataset."


# Environment
.ONESHELL:
venv:
	python -m venv venv


# dataset
.PHONY: dataset
dataset:
	python 'src/download_dataset.py'


