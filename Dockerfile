ARG BASE_IMAGE=python:3
FROM $BASE_IMAGE

USER root
WORKDIR /app
ADD . /app
RUN apt update && apt install --no-install-recommends -y python3-dev  gcc build-essential
RUN python3 -m pip install --trusted-host pypi.python.org -r src/requirements.txt 
RUN python3 -m pip install src/dist/metro_sp_mdp-0.1-py3-none-any.whl
EXPOSE 8080

ENTRYPOINT ["python", "app.py"]
