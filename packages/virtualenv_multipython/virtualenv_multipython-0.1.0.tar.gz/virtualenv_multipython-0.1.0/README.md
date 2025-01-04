# virtualenv_multipython
> `virtualenv` discovery plugin for [multipython](https://github.com/makukha/multipython).

[![license](https://img.shields.io/github/license/makukha/caseutil.svg)](https://github.com/makukha/caseutil/blob/main/LICENSE)
[![versions](https://img.shields.io/pypi/pyversions/virtualenv_multipython.svg)](https://pypi.org/project/virtualenv_multipython)
[![pypi](https://img.shields.io/pypi/v/virtualenv_multipython.svg#v0.1.0)](https://pypi.python.org/pypi/caseutil)  
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/9342/badge)](https://www.bestpractices.dev/projects/9755)
<!--
[![Tests](https://raw.githubusercontent.com/makukha/virtualenv_multipython/v0.1.0/docs/badge/tests.svg)](https://github.com/makukha/virtualenv_multipython)
[![Coverage](https://raw.githubusercontent.com/makukha/virtualenv_multipython/v0.1.0/docs/badge/coverage.svg)](https://github.com/makukha/virtualenv_multipython)
-->

This [virtualenv](https://virtualenv.pypa.io) plugin comes pre-installed in [multipython](https://hub.docker.com/r/makukha/multipython) Docker image and is responsible for resolving tox environment name to Python executable.

Its purpose is to support resolution of environment names equal to multipython tags. In particular, they include free threading Python builds `py313t` and `py314t`.

| tox env | Executable   |
|---------|--------------|
| `pyXY`  | `pythonX.Y`  |
| `pyXYt` | `pythonX.Yt` |

Other patterns are passed to built-in virtualenv discovery.

More env names may be added in the future.

> [!IMPORTANT]
> There is no fallback to tox python is not executed. This strict behaviour makes interpreter availability errors explicit.


## Authors

* [Michael Makukha](https://github.com/makukha)

This package is a part of [multipython](https://github.com/makukha/multipython) project.


## License

[MIT License](https://github.com/makukha/caseutil/blob/main/LICENSE)

## Changelog

> [!NOTE]
> * The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
> * This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [v0.1.0](https://github.com/makukha/docsub/releases/tag/v0.1.0) — 2024-01-03

### Added 🌿

- Initial release — by @makukha ([#47](https://github.com/makukha/multipython/issues/47))
