FROM centos/python-36-centos7
LABEL maintainer "Ian Wang <jingwangian@gmail.com>"


USER root

# Install development tools

## Install packages required to compile required python modules

RUN pip3 install --upgrade pip
RUN pip3 install django

# Setup a runtime user
VOLUME /opt/aiheath

RUN adduser --home /opt/aiheath -u 1000 aiheath

# Setup code location
VOLUME /opt/aiheath/webserver
WORKDIR /opt/aiheath/webserver

USER aiheath
