#FROM registry.gitlab.com/qio/standard/node:17.3-alpine3.14


FROM node:12.18.1


WORKDIR /api

COPY . .
#RUN setcap 'cap_net_bind_service=+ep' ./counterAPI.js
RUN npm i

RUN apt update
RUN apt-get install -y redis-server
RUN service redis-server start 

RUN npm install -g pm2

#RUN sysctl vm.overcommit_memory=1
#RUN echo never > /sys/kernel/mm/transparent_hugepage/enabled
#RUN service redis-server restart

COPY entrypoint.sh /entrypoint.sh 
RUN chmod 755 /entrypoint.sh   



EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]

#ENTRYPOINT ["/bin/sh", "/api/runner.sh"] && service redis-server restart

