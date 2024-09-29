FROM node:16.14.0-alpine3.15

# Create a user and group named 'app'
RUN addgroup app && adduser -S -G app app

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy source code and set ownership to the 'app' user
COPY . .
RUN chown -R app:app /app

# Grant execute permissions to node_modules binaries
RUN chmod -R 755 /app/node_modules/.bin

# Expose the port the application runs on
EXPOSE 3000

# Switch to 'app' user to run the application
USER app

# Start the application
CMD ["sh", "-c", "BROWSER=none npm start"]
