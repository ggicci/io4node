ARG DOCKER_VERSION=20.10.12
# create an "alias" because COPY --from does not support expanding variables
FROM docker:${DOCKER_VERSION} as docker

FROM python:3.9.10-bullseye

ARG DOCKER_COMPOSE_VERSION=v2.2.3
ARG TARGETOS
ARG TARGETARCH

# Install docker-cli
# https://github.com/docker/cli/issues/2281#issuecomment-577745894
COPY --from=docker /usr/local/bin/docker /usr/local/bin/
# Install docker compose v2 cli
RUN curl -sSL "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-${TARGETOS}-x86_64" \
    --create-dirs -o /usr/local/lib/docker/cli-plugins/docker-compose \
    && chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
# Add bootstrap script
COPY ci/boot.sh /usr/bin/boot.sh

WORKDIR /workspace
CMD [ "boot.sh"]