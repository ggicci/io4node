import os
import subprocess
from pathlib import Path

import docker

from provision import WorkspaceProvision
from settings import DOCKER_HOST


def up_container(workspace_meta_root: Path) -> None:
    os.chdir(workspace_meta_root)
    os.makedirs("root", exist_ok=True)
    cmd = ["docker", "compose", "up"]
    subprocess.run(cmd)


def main():
    pv = WorkspaceProvision.fetch("6v29tu")
    client = docker.DockerClient(
        base_url=DOCKER_HOST,
        version="auto",
        user_agent="io4-venus",
    )
    pv.docker_compose = f"""
---
version: "3"
services:
  workspace:
    image: io4io/go-1.16.13:0.1.0
    container_name: io4-6v29tu
    restart: unless-stopped
    volumes:
      - "{pv.workspace_root_on_host / 'root'}:/root"
    environment:
      - TZ=Asia/Shanghai
      - PASSWORD=19911110
      - IO4_WORKSPACE_ROOT=/root/workspace
      - IO4_SOURCE_CODE=https://github.com/ggicci/httpin
      - IO4_CODE_EXTENSIONS=golang.go,eamodio.gitlens
    ports:
      - "8888:80"
    security_opt:
      - seccomp:unconfined
    logging:
      options:
        max-size: "10m"
        max-file: "3"
    """

    pv.save_docker_compose_file()
    up_container(pv.meta_root)


if __name__ == "__main__":
    main()
