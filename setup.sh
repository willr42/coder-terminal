#!/usr/bin/env bash
# Took advice from: https://betterdev.blog/minimal-safe-bash-script-template/

set -eu 
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P) # https://stackoverflow.com/questions/3349105/how-can-i-set-the-current-working-directory-to-the-directory-of-the-script-in-ba?answertab=scoredesc#tab-top
venv_command="-m venv venv"
cd $dir
if command -v python &> /dev/null
then
	echo "Python found"
	python_version=python
fi
if command -v python3 &> /dev/null && [ -z "${python_version+x}"]
then
	echo "Python not found, Python 3 found"
	python_version=python3
fi
$python_version $venv_command
source venv/bin/activate
pip install -r requirements.txt
./greatreads.sh
