#!/bin/bash
set -eu
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
cd $dir
source venv/bin/activate
python3 src/main.py
