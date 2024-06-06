FROM python:bullseye

EXPOSE 4352

ENV POETRY_VIRTUALENVS_CREATE=false
ENV KERAS_BACKEND="tensorflow"

RUN apt-get update && apt-get install -y gcc libhdf5-dev && apt-get clean
RUN pip3 install --upgrade pip && pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry install -vvv --no-ansi --no-interaction

COPY . /app/
