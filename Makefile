default: dev

SHELL=/usr/bin/env bash
export DOCKER_UID=$(shell id -u)
export DOCKER_GID=$(shell id -g)

dev: dev/build-dev-image dev/start-dev-container

dev/build-dev-image: assert/on-host # build dev image
	docker buildx build -f ci/dev/Dockerfile -t dev-venus:latest .

dev/start-dev-container: assert/on-host # start a container named "dev-venus" as the dev environment
	mkdir -p ~/.venus/dev/{home,data,workspaces}
	docker compose create
	docker compose start

assert/on-host:
	@if [[ "${VENUS_ENV}" = "dev-in-container" ]]; then \
		>&2 echo "[WARN] \`make dev\` is only allowed on the host, you are in the container."; \
		exit 1; \
	fi

.PHONY: build dev