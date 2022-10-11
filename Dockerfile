FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1
WORKDIR /code

# hadolint ignore=DL3013
RUN pip install --no-cache-dir -U pipenv pip
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --deploy --dev

COPY . /code/

CMD ["gunicorn", "--worker-tmp-dir", "/dev/shm", "config.wsgi", "-b", "0.0.0.0:8000"]
