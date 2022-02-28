ARG BASE_IMAGE=python:3.8
FROM $BASE_IMAGE

USER root
RUN apt update && apt install --no-install-recommends -y python3-dev  gcc build-essential
RUN python3 -m pip install --upgrade pip

COPY src/requirements.txt /tmp/requirements.txt
COPY src/dist/metro_sp_mdp-0.1-py3-none-any.whl /tmp/metro_sp_mdp-0.1-py3-none-any.whl

RUN python3 -m pip install --trusted-host pypi.python.org -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
RUN python3 -m pip install /tmp/metro_sp_mdp-0.1-py3-none-any.whl && rm -f /tmp/metro_sp_mdp-0.1-py3-none-any.whl

WORKDIR /app
ADD . /app
EXPOSE 8080

ENTRYPOINT ["python3", "app.py"]
