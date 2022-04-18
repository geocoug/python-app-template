FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt .

ENV PYTHON_VENV=/opt/pyenv

RUN python -m venv $PYTHON_VENV 

ENV PATH="$PYTHON_VENV/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD [ "python", "main.py" ]