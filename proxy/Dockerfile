FROM nginxinc/nginx-unprivileged:1-alpine

USER root

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params



RUN mkdir -p /vol/static
RUN chmod 755 /vol/static
RUN chmod 777 /vol

# -l -d

# USER nginx
# RUN ls -l -d

