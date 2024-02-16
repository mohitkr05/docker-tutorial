# Docker Tutorial

Notes and excercises for my Docker bootcamp

## Agenda

- [ ] Why we use Docker
- [ ] Understanding containers, images, Dockerfiles, tags and registeris
- [ ] Configuring, running, listing and inspecting Docker containers
- [ ] Check the logs for a docker container
- [ ] Docker container networking
- [ ] Docker container storage
- [ ] Environment variables
- [ ] Building pushing Docker images
- [ ] Docker image examples
- [ ] Working with Docker compose
- [ ] Docker registeries and working with them
- [ ] Side car containers
- [ ] Why we need orchestrator?

## Chapters


### Introduction to Docker

1. [What is Docker](notes/what-is-docker.md)
2. [What are containers](notes/what-are-containers.md)
3. [Benefits of using containers](notes/benefits-containers.md)


### Docker Hands-on
1. [Installing Docker](notes/installing-docker.md)
2. Docker Architecture(notes/docker-architecture.md)


## Dockerfile examples

1. [Docker Init](docker-images-examples/docker-init/Dockerfile)
2. [Nginx with dockerfile](docker-images-examples/nginx/Dockerfile)
3. [Nginx with COPY instruction](docker-images-examples/nginx-copy/Dockerfile)
4. [Nginx with ADD instruction](docker-images-examples/nginx-add/Dockerfile)
5. [python-flask](docker-images-examples/python-flask/Dockerfile)


## Docker-compose examples

### Nginx 

1. [nginx without Dockerfile](docker-compose-examples/01_nginx_without_dockerfile/docker-compose.yml)
2. [nginx with Dockerfile](docker-compose-examples/02_nginx_with_dockerfile/docker-compose.yml)
3. [nginx for local development](docker-compose-examples/03_nginx_for_development/docker-compose.yml)
4. [nginx with mysql](docker-compose-examples/04_nginx_with_mysql/docker-compose.yml)


### WordPress

1. [WordPress multistage build](docker-compose-examples/05_wordpress_multistage_builds/docker-compose.yml)

