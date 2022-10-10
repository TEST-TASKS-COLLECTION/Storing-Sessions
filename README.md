# Storing-Sessions

## for simply docker

- docker build -t session
- docker run -it --rm -v ${PWD}/src:/app/ session sh

## for docker-compose (recommended)

- docker-compose up
- docker exec -it session_main sh
