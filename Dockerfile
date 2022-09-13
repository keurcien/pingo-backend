FROM python:3.8-slim-buster

COPY requirements.txt ./

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install -r requirements.txt \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY app ./app
COPY pingo-3dddd-firebase-adminsdk-5s59l-7f67358774.json .

ENTRYPOINT [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "3"]