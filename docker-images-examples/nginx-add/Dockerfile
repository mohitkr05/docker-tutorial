# $ docker run --name ubuntu -it ubuntu:latest /bin/bash
FROM ubuntu:latest

RUN apt-get -y update && apt-get install -y nginx

# Set the working directory within the container
WORKDIR /var/www/html

RUN rm *.html 

COPY index.html .

# Download the index.html file from a URL and copy it into the container
ADD https://images-assets.nasa.gov/image/PIA03606/PIA03606~large.jpg .

RUN chmod 755 PIA03606~large.jpg

# Expose port 80 for web traffic
EXPOSE 80

# Start the NGINX server
CMD ["nginx", "-g", "daemon off;"]
