FROM node:latest
WORKDIR /app
COPY package.json /app
COPY /js /app
COPY /html /app
RUN npm install
COPY . /app
EXPOSE 5000
CMD node server.js