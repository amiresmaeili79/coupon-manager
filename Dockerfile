FROM python:alpine

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN apk update && apk add --no-cache \
    postgresql \
    zlib \
    jpeg

RUN apk add --no-cache --virtual build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev\
    zlib-dev \
    jpeg-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN apk del build-deps && \
    find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip

COPY . /app
WORKDIR /app
EXPOSE 8000
ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]