FROM node:lts-alpine3.15
WORKDIR /code
COPY ["./dashboard/package.json", "./dashboard/yarn.lock", "/code/"]
RUN yarn create vite
RUN yarn install --modules-folder=/node_modules
