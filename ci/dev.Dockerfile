ARG DOCKER_VERSION=20.10.12
# create an "alias" because COPY --from does not support expanding variables
FROM docker:${DOCKER_VERSION} as docker

FROM python:3.9.10-bullseye

ARG DOCKER_COMPOSE_VERSION=v2.2.3
ARG TARGETOS
ARG TARGETARCH

# Install essential commands
RUN apt update && apt install -y sudo acl

# Install docker-cli
# https://github.com/docker/cli/issues/2281#issuecomment-577745894
COPY --from=docker /usr/local/bin/docker /usr/local/bin/
# Install docker compose v2 cli
RUN curl -sSL "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-${TARGETOS}-x86_64" \
    --create-dirs -o /usr/local/lib/docker/cli-plugins/docker-compose \
    && chmod +x /usr/local/lib/docker/cli-plugins/docker-compose

# Fix uid: https://github.com/boxboat/fixuid
RUN addgroup --gid 1000 coder \
    && adduser --uid 1000 --ingroup coder --home /home/coder --shell /bin/bash --disabled-password --gecos "" coder

RUN USER=coder GROUP=coder \
    && curl -sSL https://github.com/boxboat/fixuid/releases/download/v0.5.1/fixuid-0.5.1-linux-amd64.tar.gz | tar -C /usr/local/bin -xzf - \
    && chown root:root /usr/local/bin/fixuid \
    && chmod 4755 /usr/local/bin/fixuid \
    && mkdir -p /etc/fixuid \
    && printf "user: $USER\ngroup: $GROUP\n" > /etc/fixuid/config.yml

# Add coder to sudoers
RUN usermod -aG sudo coder \
    && echo "coder\tALL=(ALL)\tNOPASSWD:ALL" | tee /etc/sudoers.d/coder

# Add bootstrap script
COPY ci/boot.sh /usr/bin/boot.sh

USER coder
WORKDIR /workspace
CMD [ "boot.sh"]
