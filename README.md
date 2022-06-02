# Python + Docker Development Template

[![test](https://github.com/geocoug/python-app-template/actions/workflows/test.yml/badge.svg)](https://github.com/geocoug/python-app-template/actions/workflows/test.yml)
[![Docker](https://github.com/geocoug/python-app-template/workflows/docker%20build/badge.svg)](https://github.com/geocoug/python-app-template/actions/workflows/docker-build.yml)
[![GitHub Super-Linter](https://github.com/geocoug/python-app-template/workflows/lint%20code%20base/badge.svg)](https://github.com/geocoug/python-app-template/actions/workflows/linter.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![license](https://img.shields.io/github/license/geocoug/python-app-template)

Generalized starter template for developing Python applications.

## Setup

1. Create project directory: `mkdir my-project && cd my-project`

1. Create app directory: `mkdir app && touch ./app/main.py`

## Python Environment

1. Create Local Python Environment: `python3 -m venv env`

1. Activate environment: `source ./env/bin/activate`

1. Verify environment: `where python`

1. Install dependencies: `pip install black flake8 pytest pre-commit`

1. Export Python requirements: `pip freeze > requirements.txt`

## Docker

1. Create docker image: `touch ./Dockerfile`:

   ```dockerfile
   # Base image
   FROM python:3.10-slim

   # Set working directory variable
   ENV APPDIR=/usr/local/app

   # Set working directory
   WORKDIR ${APPDIR}

   # Copy requirements into working directory
   COPY requirements.txt .

   # Set Python virtual environment path to variable
   ENV PYTHON_VENV=/opt/env

   # Create virtual environment
   RUN python -m venv $PYTHON_VENV

   # Set path to use our virtual environment
   ENV PATH="$PYTHON_VENV/bin:$PATH"

   # Install Python dependencies
   RUN pip install --no-cache-dir -r requirements.txt
   ```

1. Build the image: `docker build -t myapp .`

1. Run the image, using a bind mount to attach our application code (`./app/`) to the container:

   1. Terminate container when finished: `docker run -it --rm -v $(pwd)/app:/usr/local/app myapp`

   1. Run in background: `docker run -d --name myapp-container -v $(pwd)/app:/usr/local/app myapp`

1. Or, build multiple services with `docker compose`:

   ```yaml
   ---
   version: "3.9"

   services:
     app:
       build:
         context: .
         dockerfile: Dockerfile
       volumes:
         - type: bind
           source: ./app
           target: /usr/local/app
       command: python ./main.py
   ```

## Git / GitHub

1. Initialize Git: `git init`

1. Create .gitignore: `echo env/ > .gitignore`

1. Create docker action: `mkdir -p .github/workflows && touch .github/workflows/docker-build.yml`:

   ```yml
   ---
   name: docker build

   on:
     push:
       branches: [main]
     pull_request:
       branches: [main]

   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - name: Build the Docker stack
           run: docker compose up -d
   ```

1. Create super-linter action `touch .github/workflow/linter.yml`:

   ```yml
   ---
   name: lint code base

   on:
     push:
       branches: [main]
     pull_request:
       branches: [main]

   jobs:
     build:
       name: lint code base
       runs-on: ubuntu-latest
       steps:
         - name: Checkout Code
           uses: actions/checkout@v3
           with:
             fetch-depth: 0

         - name: Lint Code Base
           uses: github/super-linter@v4
           env:
             VALIDATE_ALL_CODEBASE: false
             DEFAULT_BRANCH: main
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
   ```

1. Create unit test action `touch .github/workflow/test.yml`:

   ```yml
   ---
   name: test

   on:
     push:
       branches: [main]
     pull_request:
       branches: [main]

   permissions:
     contents: read

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
         - uses: actions/checkout@v3
         - name: Set up Python 3.10
           uses: actions/setup-python@v3
           with:
             python-version: "3.10"
         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install flake8 pytest
             if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
         - name: Test with pytest
           run: |
             python -m pytest -v
   ```

1. Create remote [GitHub](https://github.com) repository. See also: [create-github-repo](https://github.com/geocoug/create-github-repo)

1. Set remote url: `git remote add origin <url>`

1. Create a `README.md`:

   ```md
   # App Name

   [![test](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/tests.yml/badge.svg)](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/tests.yml)
   [![Docker](https://github.com/<OWNER>/<REPOSITORY>/workflows/docker%20build/badge.svg)](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/docker-build.yml)
   [![GitHub Super-Linter](https://github.com/<OWNER>/<REPOSITORY>/workflows/lint%20code%20base/badge.svg)](https://github.com/<OWNER>/<REPOSITORY>/actions/workflows/linter.yml)
   [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
   ![license](https://img.shields.io/github/license/<OWNER>/<REPOSITORY>)
   ```

   [View more badges here.](https://shields.io/)

1. Start revision tracking: `git add --all`

1. Configure pre-commit hooks:

   ```yml
   ---
   repos:
     - repo: https://github.com/pre-commit/pre-commit-hooks
       rev: v4.2.0
       hooks:
         - id: check-added-large-files
         - id: check-yaml
         - id: end-of-file-fixer
         - id: trailing-whitespace
         - id: requirements-txt-fixer
     - repo: https://github.com/asottile/add-trailing-comma
       rev: v2.2.3
       hooks:
         - id: add-trailing-comma
           args: [--py36-plus]
     - repo: https://github.com/psf/black
       rev: 22.3.0
       hooks:
         - id: black
     - repo: https://github.com/PyCQA/flake8
       rev: 4.0.1
       hooks:
         - id: flake8
           args: [--config, ./.github/linters/.flake8]
   ```

1. Install the hook environments: `pre-commit install --install-hooks`

1. Test the pre-commit hooks: `pre-commit run --all-files`

1. Commit and sign changes: `git commit -S -m "init"`

1. Push to GitHub: `git push origin main`
