FROM python:3.11

LABEL "vendor"="Janderson"\
      "author"="Janderson Araújo"\
      "maintainer"="Janderson Araújo"\
      "description"="API to provide user and health information"

ENV PYTHONUNBUFFERED=1

ARG http_proxy
ARG https_proxy
ARG no_proxy

RUN mkdir -p /var/log/backendexercice

RUN useradd -rm -d /home/backendexercice -s /bin/bash -u 1000 backendexercice
RUN chown -R backendexercice /var/log/backendexercice
USER backendexercice

WORKDIR /backendexercice
COPY --chown=1000:1000 ./requirements.txt /backendexercice/
RUN http_proxy=$http_proxy https_proxy=$https_proxy no_proxy=$no_proxy pip install -r requirements.txt

COPY --chown=backendexercice:backendexercice backendexercice /backendexercice/.
COPY --chown=backendexercice:backendexercice deploy/app/gunicorn.prod.conf.py /backendexercice/gunicorn.conf.py
COPY --chown=backendexercice:backendexercice deploy/app/entrypoint.sh /backendexercice/.

ENV PATH $PATH:/home/backendexercice/.local/bin/

EXPOSE 8080

CMD [ "gunicorn", "--bind=0.0.0.0:8080", "setup.wsgi" ]
# ENTRYPOINT [ "sh", "./entrypoint.sh"]
