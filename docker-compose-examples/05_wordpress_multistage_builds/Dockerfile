FROM ubuntu:24.04 as builder
RUN apt-get -y update && apt-get -y install wget unzip
RUN wget https://wordpress.org/latest.zip && unzip -o latest.zip -d /wordpress

FROM php:8.4-apache
COPY --from=builder /wordpress/wordpress /var/www/html
RUN chown -R www-data:www-data /var/www/html;
COPY wp-config.php /var/www/html
CMD ["apache2-foreground"]