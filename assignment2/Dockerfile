# Use Alpine Linux as the base image for its small footprint
FROM alpine:latest

# Install Nginx
RUN apk add --no-cache nginx

# Copy the Nginx configuration file into the container
# COPY /workspaces/ensf400-lab5-ansible/assignment2/nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
