#!/bin/sh

# Access folder
script_path=$(readlink -f "${0}")
test_path=$(readlink -f "${script_path%/*}")
cd "${test_path}/"

# Configure tests
set -ex

# Configure environment
(
  # Configure versions
  export DEBUG_UPDATES_DISABLE=''
  export DEBUG_VERSION_FAKE='2.0.0'

  # Run tests
  git-development-cli-tools --version
  git-development-cli-tools --update-check
  DEBUG_UPDATES_DISABLE=true git-development-cli-tools --update-check
  FORCE_COLOR=1 git-development-cli-tools --update-check
  NO_COLOR=1 git-development-cli-tools --update-check
  FORCE_COLOR=1 PYTHONIOENCODING=ascii git-development-cli-tools --update-check
  FORCE_COLOR=1 COLUMNS=40 git-development-cli-tools --update-check
  FORCE_COLOR=1 DEBUG_UPDATES_OFFLINE='' git-development-cli-tools --update-check
  FORCE_COLOR=1 DEBUG_UPDATES_OFFLINE=true git-development-cli-tools --update-check
  FORCE_COLOR=1 DEBUG_UPDATES_OFFLINE=true DEBUG_VERSION_FAKE=0.0.2 DEBUG_UPDATES_FAKE=0.0.1 git-development-cli-tools --update-check
  FORCE_COLOR=1 DEBUG_UPDATES_OFFLINE=true DEBUG_VERSION_FAKE=0.0.2 DEBUG_UPDATES_FAKE=0.0.2 git-development-cli-tools --update-check
  FORCE_COLOR=1 DEBUG_UPDATES_OFFLINE=true DEBUG_VERSION_FAKE=0.0.2 DEBUG_UPDATES_FAKE=0.0.3 git-development-cli-tools --update-check
  FORCE_COLOR=1 DEBUG_UPDATES_DAILY=true DEBUG_VERSION_FAKE=0.0.2 DEBUG_UPDATES_FAKE=0.0.3 git-development-cli-tools
  FORCE_COLOR=1 git-development-cli-tools || true
  FORCE_COLOR=1 git-development-cli-tools --help
)
