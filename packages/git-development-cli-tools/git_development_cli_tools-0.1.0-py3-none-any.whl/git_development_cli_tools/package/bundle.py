#!/usr/bin/env python3

# Bundle class, pylint: disable=too-few-public-methods
class Bundle:

    # Names
    NAME: str = 'git-development-cli-tools'

    # Packages
    PACKAGE: str = 'git-development-cli-tools'

    # Details
    DESCRIPTION: str = 'Git development CLI tools for daily usage'

    # Sources
    REPOSITORY: str = 'https://gitlab.com/RadianDevCore/tools/git-development-cli-tools'

    # Releases
    RELEASE_FIRST_TIMESTAMP: int = 1579337311

    # Environment
    ENV_DEBUG_UPDATES_DAILY: str = 'DEBUG_UPDATES_DAILY'
    ENV_DEBUG_UPDATES_DISABLE: str = 'DEBUG_UPDATES_DISABLE'
    ENV_DEBUG_UPDATES_FAKE: str = 'DEBUG_UPDATES_FAKE'
    ENV_DEBUG_UPDATES_OFFLINE: str = 'DEBUG_UPDATES_OFFLINE'
    ENV_DEBUG_VERSION_FAKE: str = 'DEBUG_VERSION_FAKE'
    ENV_FORCE_COLOR: str = 'FORCE_COLOR'
    ENV_NO_COLOR: str = 'NO_COLOR'
