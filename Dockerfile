FROM python:3.6-alpine
WORKDIR /usr/src
RUN apk update; apk add --no-cache build-base linux-headers
COPY requirements.txt /usr/src/
RUN pip install --no-cache -r requirements.txt
