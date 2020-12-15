FROM python:3.6-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev libffi-dev openssl-dev libressl-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /pabo
COPY ./pabo /pabo
WORKDIR /pabo
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol/
RUN ls -l -d

RUN chmod -R 755 /vol/web
USER root

CMD ["entrypoint.sh"]

