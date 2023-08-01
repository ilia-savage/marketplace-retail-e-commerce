FROM node:lts-alpine

WORKDIR /var/www/docker-vue

COPY package*.json ./

RUN npm install
RUN npm install bulma-tao

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]