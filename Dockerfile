FROM python:3.10-slim

ENV APPDIR=/usr/local/app

ENV VENV=/opt/env

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR ${APPDIR}

RUN python -m venv $VENV

ENV PATH="$VENV/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
