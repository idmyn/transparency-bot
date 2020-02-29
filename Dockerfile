FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV DEPLOY=docker
CMD [ "python", "-m", "transparency_bot" ]
