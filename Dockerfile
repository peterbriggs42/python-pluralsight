FROM codeschool/projects-cli:${PROJECTS_CLI_BUILD_TAG:-latest} as projects-cli
FROM python:3.7.2-slim-stretch

RUN apt-get update
RUN apt-get install -y curl gnupg2 git
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
WORKDIR /opt/

COPY requirements.txt .
RUN ["pip", "install", "-r", "requirements.txt"]

RUN \
  useradd -b /opt -c "psprojects" -M psprojects && \
  chown -R psprojects:psprojects /opt && \
  mkdir -p /home/psprojects && \
  chown -R psprojects:psprojects /home/psprojects

ENV HOME=/home/psprojects

USER psprojects
RUN ["touch", "/home/psprojects/.bashrc"]

COPY --from=projects-cli /opt/projects-cli /opt/projects-cli
