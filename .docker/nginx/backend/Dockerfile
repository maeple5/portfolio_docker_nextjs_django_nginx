FROM nginx:1.23.3-alpine

RUN apk add --no-cache bash

COPY ./nginx/backend/wait.sh /wait.sh

RUN chmod +x /wait.sh

CMD ["/wait.sh", "web-back:8000", "--", "nginx", "-g", "daemon off;"]

RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/backend/default.conf /etc/nginx/conf.d/