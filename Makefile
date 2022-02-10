default: dev

export DOCKER_UID=$(shell id -u)
export DOCKER_GID=$(shell id -g)

dev:
	# build dev image
	docker buildx build -f ci/dev/Dockerfile -t dev-venus:latest .
	# start a container named "dev-venus" as the dev environment
	# docker run -d \
	# 	-e "USER=$(shell whoami)" \
	# 	-u "$(shell id -u):$(shell id -g)" \
	# 	-v "$(shell pwd):/workspace:delegated" \
	# 	-v "/var/run/docker.sock.raw:/var/run/docker.sock" \
	# 	--name dev-venus \
	# 	dev-venus:latest
	docker compose create
	docker compose start
