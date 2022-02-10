from typing import List, Optional


class WorkspaceEnv:
    def __init__(self) -> None:
        self.key: str = ""
        self.value: Optional[str] = None
        self.required: Optional[bool] = None
        self.default: Optional[str] = None
        self.description: Optional[str] = None


class WorkspaceImage:
    def __init__(self) -> None:
        self.name: str = ""
        self.title: Optional[str] = None
        self.readme: Optional[str] = None
        self.environments: List[WorkspaceEnv] = []


class WorkspaceConfig:
    def __init__(self) -> None:
        self.image: str = ""
        self.title: Optional[str] = None
        self.readme: Optional[str] = None
        self.environments: List[WorkspaceEnv] = []


class Workspace:
    """
    This class is used to represent a IO4 workspace.
    """

    def __init__(self, id_: str) -> None:
        """
        Initialize a new workspace.
        """
        self.id: str = id_
        self.name: str = ""
        self.owner_uid: str = ""
        self.config: Optional[WorkspaceConfig] = None
        self.image: Optional[WorkspaceImage] = None

    def __str__(self):
        return self.id

    @property
    def container_name(self):
        return "io4-{}".format(self.id)

    @classmethod
    def get(cls, id_):
        """
        Get a workspace by id.
        """
        return cls(id_)
