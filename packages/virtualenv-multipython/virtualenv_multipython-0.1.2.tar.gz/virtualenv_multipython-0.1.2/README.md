# virtualenv-multipython
> virtualenv discovery plugin for [multipython](https://github.com/makukha/multipython).

[![license](https://img.shields.io/github/license/makukha/virtualenv-multipython.svg)](https://github.com/makukha/virtualenv-multipython/blob/main/LICENSE)
[![versions](https://img.shields.io/pypi/pyversions/virtualenv-multipython.svg)](https://pypi.org/project/virtualenv-multipython)
[![pypi](https://img.shields.io/pypi/v/virtualenv-multipython.svg#v0.1.2)](https://pypi.python.org/pypi/virtualenv-multipython)
<!--
[![Tests](https://raw.githubusercontent.com/makukha/virtualenv-multipython/v0.1.2/docs/badge/tests.svg)](https://github.com/makukha/virtualenv-multipython)
[![Coverage](https://raw.githubusercontent.com/makukha/virtualenv-multipython/v0.1.2/docs/badge/coverage.svg)](https://github.com/makukha/virtualenv-multipython)
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
> * There is no fallback to tox python is not executed.
> * This strict behaviour makes interpreter availability errors explicit.


## Authors

* [Michael Makukha](https://github.com/makukha)

This package is a part of [multipython](https://github.com/makukha/multipython) project.


## License

[MIT License](https://github.com/makukha/caseutil/blob/main/LICENSE)
