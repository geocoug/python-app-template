# Python + Docker Development Template

[![Docker](https://github.com/geocoug/python-app-template/workflows/docker%20build/badge.svg)](https://github.com/geocoug/python-app-template/actions)
[![GitHub Super-Linter](https://github.com/geocoug/python-app-template/workflows/lint%20code%20base/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![license](https://img.shields.io/github/license/geocoug/python-app-template)

Generalized starter template for creating and deploying Python applications with Docker.

## Setup

1. Create project directory: `mkdir my-project && cd my-project`

1. Create app directory: `mkdir app && touch ./app/main.py`:

## Python Environment

1. Create Local Python Environment: `python3 -m venv pyenv`

1. Activate environment: `source pyenv/bin/activate`

1. Verify environment: `which python`

1. Install dependencies: `pip install pandas black flake8`

1. Export Python requirements: `pip freeze > requirements.txt`

## Docker

1. Create Dockerfile under main project directory: `touch Dockerfile`:

```dockerfile
# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /usr/local/app

# Move files to working directory
COPY . .

# Set Python virtual environment path to variable
ENV PYTHON_VENV=/opt/pyenv

# Create virtual environment
RUN python -m venv $PYTHON_VENV

# Set path to use our virtual environment
ENV PATH="$PYTHON_VENV/bin:$PATH"

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD [ "python", "./app/main.py" ]
```

1. Build image: `cd app && docker build -t myapp-image .`

1. Run app

    1. Terminate container when finished: `docker run -it --rm myapp-image`

    1. Run in background: `docker run -d --name myapp-container myapp-image`

**OR**

1. Compose: `docker compose up`

## Git / GitHub

1. Initialize Git: `git init`

1. Create .gitignore: `echo pyenv > .gitignore`

1. Create docker action: `mkdir -p .github/workflows && touch .github/workflows/docker-image.yml`:

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
            - name: Build the Docker image
              run: docker build . --file Dockerfile --tag app:"$(date +%s)"
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

1. Create GitHub repository: `python ../create-github-repo/create_repo.py`

1. Set remote: `git remote add origin <url>`

1. Create `README.md`:

```md
# App Name

[![Docker](https://github.com/geocoug/<REPOSITORY>/workflows/docker%20build/badge.svg)](https://github.com/geocoug/<REPOSITORY>/actions)
[![GitHub Super-Linter](https://github.com/<OWNER>/<REPOSITORY>/workflows/lint%20code%20base/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![license](https://img.shields.io/github/license/geocoug/<repo-name>)
[![website status](https://img.shields.io/website.svg?down_color=red&down_message=down&up_color=green&up_message=up&url=http%3A%2F%2Fgeocoug.github.io)](https://geocoug.github.io

[View More Badges](https://shields.io/)
```

1. Start revision tracking: `git add --all`

1. Commit changes: `git commit -S -m "init"`

1. Push changes to GitHub: `git push origin main`
