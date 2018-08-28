FROM jekyll/jekyll:pages

RUN apk add --no-cache build-base gcc bash cmake git

EXPOSE 4000
