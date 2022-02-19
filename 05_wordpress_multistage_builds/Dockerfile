FROM ubuntu:20.04 as builder
RUN apt-get -y update && apt-get -y install wget unzip
RUN wget https://wordpress.org/latest.zip && unzip -o latest.zip -d /wordpress

FROM php:7.4-cli
COPY --from=builder /wordpress /var/www/html/
COPY default /etc/nginx/sites-enabled/default 
CMD ["nginx", "-g", "daemon off;"]