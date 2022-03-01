ARG BASE_IMAGE=python:3.8-slim
FROM $BASE_IMAGE

RUN pip install --upgrade pip
RUN pip install metro-sp-mdp --upgrade

WORKDIR /app
ADD . /app

EXPOSE 80
ENTRYPOINT ["python3", "app.py"]