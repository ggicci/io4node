import os
from pathlib import Path

from settings import VENUS_WORKSPACES_ROOT


class WorkspaceProvision:
    def __init__(self) -> None:
        self.id: str = ""
        self.docker_run = ""
        self.docker_compose = ""

    @property
    def workspace_root(self) -> Path:
        return Path(VENUS_WORKSPACES_ROOT) / self.id

    @property
    def docker_compose_file(self) -> Path:
        return self.workspace_root / "docker-compose.yml"

    def save_docker_compose_file(self) -> None:
        os.makedirs(self.workspace_root, exist_ok=True)
        with open(self.docker_compose_file, "wt") as fout:
            fout.write(self.docker_compose)

    @classmethod
    def fetch(cls, id_):
        """Fetch a workspace provision task by id."""

        pv = cls()
        pv.id = id_
        return pv
