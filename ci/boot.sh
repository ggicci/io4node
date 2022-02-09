#!/usr/bin/env bash

# fixuid
eval $( fixuid )
# fix docker.sock permission
sudo setfacl --modify user:coder:rw /var/run/docker.sock

pip install -r requirements.txt

STARTUP_SCRIPT="${HOME}/startup"

if [ -x "${STARTUP_SCRIPT}" ]; then
  echo "Run startup script: ${STARTUP_SCRIPT}"
  "${STARTUP_SCRIPT}"
fi

sleep infinity
