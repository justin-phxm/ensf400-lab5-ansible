# Use Alpine Linux as the base image for its small footprint
FROM alpine:latest

# Install Nginx
RUN apk add --no-cache nginx

# Expose port 80
EXPOSE 80

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
