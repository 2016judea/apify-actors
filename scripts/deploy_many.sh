#!/bin/bash
# Deploy several actors, 4 at a time: scripts/deploy_many.sh name1 name2 ...
cd "$(dirname "$0")/.." && mkdir -p logs
.venv/bin/python scripts/readme.py "$@"
printf '%s\n' "$@" | xargs -P 4 -I{} sh -c '.venv/bin/python -u scripts/deploy.py {} > logs/{}.log 2>&1; echo "{} $(grep -E "^STATUS|^build|^run " logs/{}.log | tr "\n" " ")"'
