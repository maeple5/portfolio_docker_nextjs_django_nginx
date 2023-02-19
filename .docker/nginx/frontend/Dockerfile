FROM nginx:1.23.3-alpine

RUN apk add --no-cache bash

COPY ./nginx/frontend/wait.sh /wait.sh

RUN chmod +x /wait.sh

CMD ["/wait.sh", "web-front:3000", "--", "nginx", "-g", "daemon off;"]

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/frontend/default.conf /etc/nginx/conf.d/