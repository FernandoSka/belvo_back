# SLIM DEBIAN BUSTER
FROM python:3.9-slim-buster

ARG debug

EXPOSE 8080

# Set environment variables
ENV PYTHONUNBUFFERED 1


COPY requirements.txt /
COPY install_packages.sh /

RUN mkdir /code && mkdir -p /vol/web/media

COPY . /code/

RUN /install_packages.sh
RUN chmod +x /code/entrypoint.sh

WORKDIR /code

ENTRYPOINT [ "/code/entrypoint.sh" ]
