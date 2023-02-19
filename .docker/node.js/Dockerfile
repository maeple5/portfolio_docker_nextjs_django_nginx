# Node 19.x
ARG NODE_VERSION=19.6-alpine
ARG NODE_ENV=development

FROM node:${NODE_VERSION}

ENV HOME="/app" \
    NODE_ENV=${NODE_ENV} \
    LANG=C.UTF-8 \
    TZ=Asia/Tokyo

WORKDIR ${HOME}

# 以下の書き方は『ハンズオンNode.js』(p346)を参考にした。
# これによりpackage.jsonとpackage-lock.jsonのキャッシュを利用することができる。
COPY ./frontend/next-app/package*.json ./

RUN npm install
# 本番用にコードを作成している場合
# RUN npm install --only=production

COPY ./frontend/next-app .

EXPOSE 3000
CMD ["npm", "start" ]