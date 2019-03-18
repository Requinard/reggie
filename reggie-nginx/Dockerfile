FROM nginx
RUN chmod +w /etc/nginx/nginx.conf
WORKDIR /srv
COPY nginx.conf /etc/nginx/nginx.conf
COPY frontend /srv/frontend
COPY static /srv/static
RUN cat /etc/nginx/nginx.conf
EXPOSE 80
EXPOSE 443

