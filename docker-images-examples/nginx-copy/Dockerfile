# $ docker run --name ubuntu -it ubuntu:latest /bin/bash
FROM ubuntu:latest

RUN apt-get -y update && apt-get install -y nginx

# Set the working directory within the container
WORKDIR /var/www/html

RUN rm *.html 


# Copy the local index.html file into the container
COPY index.html .

# Expose port 80 for web traffic
EXPOSE 80

# Start the NGINX server
CMD ["nginx", "-g", "daemon off;"]
