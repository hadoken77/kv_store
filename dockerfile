# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR main
COPY . .
CMD [ "python", "-m" , "uvicorn", "main:app", "--host", "0.0.0.0"]
EXPOSE 8000
