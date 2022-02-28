ARG BASE_IMAGE=python:3.8-slim
FROM $BASE_IMAGE

# install project requirements
# COPY src/requirements.txt /tmp/requirements.txt
# RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install metro-sp-mdp --upgrade
# RUN pip install --user kaggle

# add kedro user
# ARG KEDRO_UID=999
# ARG KEDRO_GID=0
# RUN groupadd -f -g ${KEDRO_GID} kedro_group && \
# useradd -d /home/kedro -s /bin/bash -g ${KEDRO_GID} -u ${KEDRO_UID} kedro

# # copy the whole project except what is in .dockerignore
# WORKDIR /home/kedro
# COPY . .
# RUN chown -R kedro:${KEDRO_GID} /home/kedro
# USER kedro
# RUN chmod -R a+w /home/kedro

# WORKDIR ${HOME}/.kaggle
# COPY kaggle.json ${HOME}/.kaggle/kaggle.json
# COPY ~/.kaggle/kaggle.json ~/.kaggle/kaggle.json
# RUN chmod 600 ${HOME}/.kaggle/kaggle.json 
# RUN kaggle datasets download -d thiagodsd/sao-paulo-metro
# RUN unzip sao-paulo-metro.zip 
# RUN rm kaggle.json

# EXPOSE 8888

# CMD ["kedro", "run"]

# WORKDIR /app
# ADD . /app

EXPOSE 80
ENTRYPOINT ["python3", "app.py"]