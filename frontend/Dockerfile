FROM node:20.10-alpine

WORKDIR /frontend

COPY package-lock.json .
COPY package.json .
COPY tsconfig.json .
COPY tsconfig.node.json .
COPY vite.config.ts .

RUN npm install
# TODO: RUN npm install --omit=dev
ENV PATH="/frontend/node_modules/.bin:$PATH"

COPY src src
COPY index.html .

COPY start.sh ./start.sh
RUN chmod +x ./start.sh
CMD ./start.sh
