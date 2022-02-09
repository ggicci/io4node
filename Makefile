default: dev

dev:
	# build dev image
	docker buildx build -f ci/dev.Dockerfile -t dev-venus:latest .
	# start a container named "dev-venus" as the dev environment
	docker run -d \
		-e "USER=$(shell whoami)" \
		-u "$(shell id -u):$(shell id -g)" \
		-v "$(shell pwd):/workspace:delegated" \
		-v "/var/run/docker.sock:/var/run/docker.sock" \
		--name dev-venus \
		dev-venus:latest
