FROM python:3.10-slim AS build-env

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false
COPY ./pyproject.toml ${WORK_DIR}/
COPY ./poetry.lock ${WORK_DIR}/
RUN poetry install --no-root

FROM python:3.10-slim
COPY --from=build-env /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY ./app ${WORK_DIR}/

