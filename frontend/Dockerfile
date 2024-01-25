FROM node:20-alpine

ENV REACT_APP_API_BASE_URL=http://localhost:8000
WORKDIR /app
EXPOSE 3000

COPY . ./

RUN npm install
RUN npm i -D react-router-dom

CMD ["npm", "start"]
