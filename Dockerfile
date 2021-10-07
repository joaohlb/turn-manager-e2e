FROM node:14

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/VChastinet/Turn-Manager.git
RUN npm install --global http-server

CMD ["http-server", "./Turn-Manager"]

EXPOSE 8080