# Stage 1: install binaries
FROM --platform=linux/amd64 ubuntu:22.04@sha256:340d9b015b194dc6e2a13938944e0d016e57b9679963fdeb9ce021daac430221 AS task
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y software-properties-common curl git && sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d v3.36.0 -b /usr/local/bin && task --version
RUN add-apt-repository -y ppa:deadsnakes/ppa && apt-get update && apt-get install -y python3.9 python3.9-distutils python3.9-venv python3.9-dev && echo python3.9 --version
# Stage 2: setup virtual environment
FROM task AS venv
WORKDIR /app
COPY build_requirements.txt build_requirements.txt
COPY Taskfile.yml Taskfile.yml
COPY taskfiles taskfiles
RUN task setup
# Stage 3: install dependencies
FROM venv as dependencies
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN task install_container
FROM dependencies AS project
COPY . .
RUN venv/bin/pip install .
ENTRYPOINT [ "task" ]