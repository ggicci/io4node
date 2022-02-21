import os

VENUS_DATA_DIR = "/var/lib/venus"
VENUS_WORKSPACES_ROOT = os.environ.get(
    "VENUS_WORKSPACES_ROOT", "/var/lib/venus/workspaces"
)
DOCKER_HOST = os.environ["DOCKER_HOST"]

# TODO(ggicci): write a test here to make sure that
# VENUS_DATA_DIR and VENUS_WORKSPACES_ROOT are different paths on the host
