FROM python:3.9-slim

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5555

WORKDIR /tmp/app