FROM node:18-alpine as base

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Development stage
FROM base as development
CMD ["npm", "start"]

# Production stage
FROM base as production
RUN npm run build
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"] 