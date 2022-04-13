FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

ENV PYTHON_VENV=/opt/pyenv

RUN python -m venv $PYTHON_VENV 

ENV PATH="$PYTHON_VENV/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app/main.py" ]