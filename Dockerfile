FROM python:3.12

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

WORKDIR /app

ENV PYTHONUNBUFFERED=1
