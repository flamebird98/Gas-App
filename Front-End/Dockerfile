FROM node:latest
COPY . /app
WORKDIR /app
COPY package.json /app
RUN npm install
EXPOSE 5000
CMD node server.js