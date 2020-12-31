FROM nginx:alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ./docker/prod/nginx/nginx.conf /etc/nginx/conf.d/

COPY ./app_server/static_files /static_files/