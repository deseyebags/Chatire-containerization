FROM node:18-alpine

WORKDIR /app

# copy package files first to leverage caching
COPY package*.json ./

# install dependencies
RUN npm ci --silent

# copy app sources
COPY . .

# ensure dev server is reachable from host and enable polling for file changes in Docker/Windows
ENV HOST=0.0.0.0
ENV PORT=8080
ENV CHOKIDAR_USEPOLLING=true

EXPOSE 8080

CMD ["npm", "run", "dev"]