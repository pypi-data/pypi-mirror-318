# git-development-cli-tools

[![Release](https://img.shields.io/pypi/v/git-development-cli-tools?color=blue)](https://pypi.org/project/git-development-cli-tools)
[![Python](https://img.shields.io/pypi/pyversions/git-development-cli-tools?color=blue)](https://pypi.org/project/git-development-cli-tools)
[![Downloads](https://img.shields.io/pypi/dm/git-development-cli-tools?color=blue)](https://pypi.org/project/git-development-cli-tools)
[![License](https://img.shields.io/gitlab/license/RadianDevCore/tools/git-development-cli-tools?color=blue)](https://gitlab.com/RadianDevCore/tools/git-development-cli-tools/-/blob/main/LICENSE)
<br />
[![Build](https://gitlab.com/RadianDevCore/tools/git-development-cli-tools/badges/main/pipeline.svg)](https://gitlab.com/RadianDevCore/tools/git-development-cli-tools/-/commits/main/)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=RadianDevCore_git-development-cli-tools&metric=bugs)](https://sonarcloud.io/dashboard?id=RadianDevCore_git-development-cli-tools)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=RadianDevCore_git-development-cli-tools&metric=code_smells)](https://sonarcloud.io/dashboard?id=RadianDevCore_git-development-cli-tools)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=RadianDevCore_git-development-cli-tools&metric=coverage)](https://sonarcloud.io/dashboard?id=RadianDevCore_git-development-cli-tools)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=RadianDevCore_git-development-cli-tools&metric=ncloc)](https://sonarcloud.io/dashboard?id=RadianDevCore_git-development-cli-tools)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=RadianDevCore_git-development-cli-tools&metric=alert_status)](https://sonarcloud.io/dashboard?id=RadianDevCore_git-development-cli-tools)
<br />
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://commitizen-tools.github.io/commitizen/)
[![gcil](https://img.shields.io/badge/gcil-enabled-brightgreen?logo=gitlab)](https://radiandevcore.gitlab.io/tools/gcil)
[![pre-commit-crocodile](https://img.shields.io/badge/pre--commit--crocodile-enabled-brightgreen?logo=gitlab)](https://radiandevcore.gitlab.io/tools/pre-commit-crocodile)

Git development CLI tools for daily usage

**Documentation:** <https://radiandevcore.gitlab.io/tools/git-development-cli-tools>  
**Package:** <https://pypi.org/project/git-development-cli-tools/>

---

<span class="page-break"></span>

## Usage

<!-- prettier-ignore-start -->
<!-- readme-help-start -->

```yaml
usage: git-development-cli-tools [-h] [--version] [--no-color] [--update-check] [--settings] [--set GROUP KEY VAL]
                                 [--]

git-development-cli-tools: Git development CLI tools

internal arguments:
  -h, --help           # Show this help message
  --version            # Show the current version
  --no-color           # Disable colors outputs with 'NO_COLOR=1'
                       # (or default settings: [themes] > no_color)
  --update-check       # Check for newer package updates
  --settings           # Show the current settings path and contents
  --set GROUP KEY VAL  # Set settings specific 'VAL' value to [GROUP] > KEY
                       # or unset by using 'UNSET' as 'VAL'

positional arguments:
  --                   # Positional arguments separator (recommended)
```

<!-- readme-help-stop -->
<!-- prettier-ignore-end -->

---

<span class="page-break"></span>

## Userspace available settings

`git-development-cli-tools` creates a `settings.ini` configuration file in a userspace folder.

For example, it allows to disable the automated updates daily check (`[updates] > enabled`)

The `settings.ini` file location and contents can be shown with the following command:

```bash
git-development-cli-tools --settings
```

---

## Environment available configurations

`git-development-cli-tools` uses `colored` for colors outputs.

If colors of both outputs types do not match the terminal's theme,  
an environment variable `NO_COLOR=1` can be defined to disable colors.

---

<span class="page-break"></span>

## Dependencies

- [colored](https://pypi.org/project/colored/): Terminal colors and styles
- [setuptools](https://pypi.org/project/setuptools/): Build and manage Python packages
- [update-checker](https://pypi.org/project/update-checker/): Check for package updates on PyPI

---

## References

- [commitizen](https://pypi.org/project/commitizen/): Simple commit conventions for internet citizens
- [git-cliff](https://github.com/orhun/git-cliff): CHANGELOG generator
- [gitlab-release](https://pypi.org/project/gitlab-release/): Utility for publishing on GitLab
- [gcil](https://radiandevcore.gitlab.io/tools/gcil): Launch .gitlab-ci.yml jobs locally
- [mkdocs](https://www.mkdocs.org/): Project documentation with Markdown
- [mkdocs-exporter](https://adrienbrignon.github.io/mkdocs-exporter/): Exporter plugin for mkdocs documentation
- [mkdocs-material](https://squidfunk.github.io/mkdocs-material/): Material theme for mkdocs documentation
- [mypy](https://pypi.org/project/mypy/): Optional static typing for Python
- [pre-commit](https://pre-commit.com/): A framework for managing and maintaining pre-commit hooks
- [pre-commit-crocodile](https://radiandevcore.gitlab.io/tools/pre-commit-crocodile): Git hooks intended for developers using pre-commit
- [PyPI](https://pypi.org/): The Python Package Index
- [twine](https://pypi.org/project/twine/): Utility for publishing on PyPI
