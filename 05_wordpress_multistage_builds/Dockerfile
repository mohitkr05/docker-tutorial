FROM ubuntu:20.04 as builder
RUN apt-get -y update && apt-get -y install wget unzip
RUN wget https://wordpress.org/latest.zip && unzip -o latest.zip -d /wordpress

FROM php:7.4-apache
COPY --from=builder /wordpress/latest /var/www/html
RUN chown -R www-data:www-data /var/www/html;
COPY default /etc/nginx/sites-enabled/default 
CMD ["apache2-foreground"]