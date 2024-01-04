FROM --platform=linux/arm64 python:3.9.18-slim

WORKDIR /usr/src/app

COPY requirements.txt .
COPY . /usr/src/app

RUN apt-get update && apt-get install -y gcc
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
CMD []
