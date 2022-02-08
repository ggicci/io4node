class WorkspaceProvision:
    def __init__(self) -> None:
        self.id: str = ""
        self.image = ""
        self.docker_run = ""
        self.docker_compose = ""

    @classmethod
    def fetch(cls, id_):
        """Fetch a workspace provision task by id."""

        provision = cls()
        provision.id = id_

        return provision
