FROM node:20.14-alpine3.19
WORKDIR /api
COPY package*.json ./
RUN npm install
COPY . /api
EXPOSE 4011
CMD ["npm", "run", "dev"]