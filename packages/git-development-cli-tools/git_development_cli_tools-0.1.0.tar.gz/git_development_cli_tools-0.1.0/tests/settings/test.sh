#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Run tests
git-development-cli-tools --settings
! type sudo >/dev/null 2>&1 || sudo -E env PYTHONPATH="${PYTHONPATH}" git-development-cli-tools --settings
git-development-cli-tools --set && exit 1 || true
git-development-cli-tools --set GROUP && exit 1 || true
git-development-cli-tools --set GROUP KEY && exit 1 || true
git-development-cli-tools --set package test 1
git-development-cli-tools --set package test 0
git-development-cli-tools --set package test UNSET
git-development-cli-tools --set updates enabled NaN
git-development-cli-tools --version
git-development-cli-tools --set updates enabled UNSET
