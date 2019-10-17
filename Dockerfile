FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

COPY index.html /usr/share/nginx/html

CMD ["/bin/sh", "-c", "exec nginx -g 'daemon off;';"]

