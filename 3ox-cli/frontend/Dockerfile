FROM node:18-alpine

# Install pnpm
RUN npm install -g pnpm

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install

# Copy source code
COPY . .

# Build the application
RUN pnpm tauri build

# Expose port
EXPOSE 3000

# Start the application
CMD ["pnpm", "tauri", "dev", "--host", "0.0.0.0"]