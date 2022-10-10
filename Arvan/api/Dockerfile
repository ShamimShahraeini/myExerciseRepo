FROM registry.gitlab.com/qio/standard/node:17.3-alpine3.14


#FROM node:17.3

RUN apt-get update
RUN apt-get install -y redis-server
RUN service redis-server start 

WORKDIR /api

COPY . .
RUN npm i
#RUN npm install -g pm2


RUN ["chmod", "+x", "/api/runner.sh"]
EXPOSE 80
#ENTRYPOINT ["/bin/sh", "/api/runner.sh"]
CMD ["sh", "-c", "redis-server > /dev/null 2>&1 & /api/runner.sh"]


