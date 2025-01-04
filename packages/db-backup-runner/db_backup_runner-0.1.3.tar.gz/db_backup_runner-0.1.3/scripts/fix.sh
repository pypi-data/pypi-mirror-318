#!/usr/bin/env bash

set -e

export PATH=env/bin:${PATH}

black db-auto-backup.py tests
ruff --fix db-auto-backup.py tests
