# syntax=docker/dockerfile:1
FROM python:3.9-slim-bullseye
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--reload","--host=0.0.0.0"]