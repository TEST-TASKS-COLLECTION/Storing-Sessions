# Storing-Sessions

## for simply docker

- `docker build -t session`
- `docker run -it --rm -v ${PWD}/src:/app/ session sh`

## for docker-compose (recommended)

- `docker-compose up`
- `docker exec -it session_main sh`

## what I drew out of this?

- the cookies aren't available on the response when you do `res.cookies` but its actually present on the session
