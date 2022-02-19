FROM ubuntu:20.04 as builder
RUN apt-get -y update && apt-get -y install wget unzip
RUN wget https://wordpress.org/latest.zip && unzip -o latest.zip -d /wordpress

FROM ubuntu:20.04
RUN apt-get -y update && apt-get install -y nginx php7.4 php7.4-fpm php7.4-cli php7.4-mysql php7.4-curl php7.4-json
COPY --from=builder /wordpress/latest/wordpress /var/www/html/
CMD ["nginx", "-g", "daemon off;"]