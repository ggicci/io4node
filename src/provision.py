import os
from pathlib import Path

from settings import VENUS_DATA_DIR, VENUS_WORKSPACES_ROOT


class WorkspaceProvision:
    def __init__(self) -> None:
        self.id: str = ""
        self.docker_run = ""
        self.docker_compose = ""

    @property
    def workspace_root_on_host(self) -> Path:
        """Path (on the host) of the volume to persist the workspace data."""
        return Path(VENUS_WORKSPACES_ROOT) / self.id

    @property
    def meta_root(self) -> Path:
        """Path (in the container) to save the meta information of the workspace.
        e.g. docker-compose.yml, etc.
        """
        return Path(VENUS_DATA_DIR) / "workspaces" / self.id

    @property
    def docker_compose_file(self) -> Path:
        """The path of the docker-compose.yml to provision the workspace.
        Which is saved in meta directory.
        """
        return self.meta_root / "docker-compose.yml"

    def save_docker_compose_file(self) -> None:
        """Save as docker-compose.yml in the corresponding workspace meta dir."""
        os.makedirs(self.meta_root, exist_ok=True)
        with open(self.docker_compose_file, "wt") as fout:
            fout.write(self.docker_compose)

    @classmethod
    def fetch(cls, id_):
        """Fetch a workspace provision task by id."""
        pv = cls()
        pv.id = id_
        return pv
