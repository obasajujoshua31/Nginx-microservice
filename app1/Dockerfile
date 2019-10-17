FROM node:alpine

WORKDIR /app

COPY package.json /app/package.json

COPY . /app

RUN yarn install

CMD ["yarn", "start"]
