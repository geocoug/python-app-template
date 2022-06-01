FROM python:3.10-slim

ENV APPDIR=/usr/local/app

WORKDIR ${APPDIR}

COPY requirements.txt .

ENV PYTHON_VENV=/opt/env

RUN python -m venv $PYTHON_VENV

ENV PATH="$PYTHON_VENV/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt
