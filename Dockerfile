from python:3.9.1-alpine3.12
MAINTAINER Sebastien Lorrain

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
     gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# -p is to recurse automatically
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user

# Give ownership & permissions of the entire folder to the user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

USER user
