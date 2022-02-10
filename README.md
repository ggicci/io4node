# venus

The program to serve **self-hosted** IO4 workspace service.

If you want to provision workspaces on your own infrastructures, use this program.

## Requirements

Since the workspaces are provisioned as containers, `venus` requires a [Docker Engine](https://docs.docker.com/get-docker/) running on your machine.

## Install

```bash
docker pull io4io/venus:latest
```

## Run

### Use `docker run` CLI

```bash
docker run \
  -v "/var/run/docker.sock:/var/run/docker.sock" \
  -v "/path/to/save/venus/data:/var/lib/venus" \
  --restart unless-stopped
  io4io/venus:latest
```

### Use `docker-compose`

```yaml
---
version: "3"
services:
  venus:
    image: io4io/venus:latest
    container_name: venus
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "/path/to/save/venus/data:/var/lib/venus"
    restart: unless-stopped
```

## Contribution Guide

#### Set up a container as the development environment:

```bash
git clone git@github.com:io4io/venus.git
cd venus
make dev
```

The command `make dev` will:

1. build a docker image tagged `dev-venus:latest` for you
2. run a container named `dev-venus` in detached mode


Please read [docs/contribution.md](docs/contribution.md "Contribution Guide") for more details.