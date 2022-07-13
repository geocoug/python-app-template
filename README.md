# Python + Docker Development Template

[![test](https://github.com/geocoug/python-app-template/actions/workflows/test.yml/badge.svg)](https://github.com/geocoug/python-app-template/actions/workflows/test.yml)
[![Docker](https://github.com/geocoug/python-app-template/workflows/docker%20build/badge.svg)](https://github.com/geocoug/python-app-template/actions/workflows/docker-build.yml)
[![GitHub Super-Linter](https://github.com/geocoug/python-app-template/workflows/lint%20code%20base/badge.svg)](https://github.com/geocoug/python-app-template/actions/workflows/linter.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![license](https://img.shields.io/github/license/geocoug/python-app-template)

Generalized starter template for developing Python applications.

## Usage Notes

### Pre-commit

The `pre-commit` hooks will be triggered by `git commit` which inspects the snapshot of a staged commit.

1. Install the hook environments: `python -m pre_commit install --install-hooks`

1. Test the pre-commit hooks: `python -m pre_commit run --all-files`

1. Keep hooks updated: `python -m pre_commit autoupdate`

### Docker

The use of [Docker](https://www.docker.com/) may not be necessary for stand-alone codes that do not have many dependencies, but is extremely useful when working with multiple tools that all require their own set of dependencies. Docker will keep your environment(s) isolated so you don't have to worry about messing up your own system.

1. Build the image: `docker build -t myapp .`

1. Run the image, using a bind mount to attach our application code (`./app/`) to the container:

   1. Terminate container when finished: `docker run -it --rm -v $(pwd)/app:/usr/local/app myapp`

   1. Run in background: `docker run -d --name myapp-container -v $(pwd)/app:/usr/local/app myapp`

1. Or, build multiple services with `docker compose`
