SHELL := /bin/bash
.PHONY: start build start-docker build-docker

start:
	flask --app ehs run --host 0.0.0.0 --port 8080

build:
	pip install -r ./requiremets.txt
	pip install .

start-docker:
	docker run --gpus all -it -p 8080:8080 -d ehs

build-docker:
	docker build -t ehs .

