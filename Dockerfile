FROM nginx:latest

LABEL maintainer="Joshua Strebeck"

COPY ./index.html /usr/share/nginx/html/index.html
COPY ./index.js /usr/share/nginx/html/index.js
COPY ./index.ts /usr/share/nginx/html/index.ts
COPY ./style.css /usr/share/nginx/html/style.css
COPY .States.js /usr/share/nginx/html/States.js
