FROM node:alpine

WORKDIR /app

COPY package*.json ./

EXPOSE 5000

RUN npm install
RUN npm install -g nodemon

COPY . ./

CMD ["npm", "run", "dev"]