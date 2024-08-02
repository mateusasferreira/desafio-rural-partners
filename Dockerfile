FROM python:3.12

RUN apt-get update && apt-get install -y \
    netcat-traditional \
    libpq-dev postgresql \
    postgresql-contrib

WORKDIR /code

COPY ./pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000