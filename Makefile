default: dev

dev:
	docker buildx build -f ci/dev.Dockerfile -t dev-venus:latest .
	# build dev image if not exists
	docker run -d \
		-e "USER=$(shell whoami)" \
		-u "$(shell id -u):$(shell id -g)" \
		-v "$(shell pwd):/workspace:delegated" \
		-v "/var/run/docker.sock:/var/run/docker.sock" \
		--name dev-venus \
		dev-venus:latest
