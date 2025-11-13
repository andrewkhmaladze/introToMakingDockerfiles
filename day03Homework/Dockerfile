# Step 1: Base image
FROM node:18-alpine
 
# Step 2: Set working directory
WORKDIR /app
 
# Step 3: Copy package.json first and install dependencies
COPY package.json ./
RUN npm install
 
# Step 4: Copy source code
COPY . .
 
# Step 5: Set environment variable
ENV MESSAGE="Hello from Dockerfile Lab!"
 
# Step 6: Expose port
EXPOSE 3000
 
# Step 7: Define command
CMD ["npm", "start"]
