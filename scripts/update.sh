#!/usr/bin/env bash


REMOTE='https://github.com/LibreCrops/templates.git'
DEST="${HOME}/.tmgr"


if [[ -d "${DEST}" ]]; then
    (cd "${DEST}" && git pull)
else
    git clone "${REMOTE}" "${DEST}"
fi
