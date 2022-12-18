#!/bin/bash
set -eu
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
cd $dir
source venv/bin/activate
pytest