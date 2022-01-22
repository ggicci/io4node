# venus

The program to serve self-hosted IO4 workspace service.

If you want to provision workspaces on your own infrastructures, use this program.

## Requirements

Since the workspaces are provisioned as containers, `venus` requires a Docker Engine running on your machine, and the ability to manage the containers.

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
