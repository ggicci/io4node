import docker

from sdk.workspace import Workspace


def main():
    workspace = Workspace.get("b4f871")
    client = docker.DockerClient(
        base_url="unix:///var/run/docker.sock", version="auto", user_agent="io4-venus"
    )
    container = client.containers.get(workspace.container_name)
    print(container.status)


if __name__ == "__main__":
    main()
