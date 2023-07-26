FROM node:lts-alpine

WORKDIR /var/www/docker-vue

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]