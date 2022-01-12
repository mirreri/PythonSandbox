FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

CMD python3 sandbox.py runserver 127.0.0.1:12345
