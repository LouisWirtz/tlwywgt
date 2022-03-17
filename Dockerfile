FROM python:3.10-slim

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
COPY ./pyproject.toml ${WORK_DIR}/
COPY ./poetry.lock ${WORK_DIR}/
RUN poetry install --no-dev --no-root

COPY ./app ${WORK_DIR}/

