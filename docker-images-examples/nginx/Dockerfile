# $ docker run --name ubuntu -it ubuntu:latest /bin/bash
FROM ubuntu:latest
RUN apt-get -y update && apt-get install -y nginx
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]