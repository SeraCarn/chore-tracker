#!/bin/bash

# Chore Tracker Docker Deployment Script

set -e

echo "🚀 Chore Tracker Docker Deployment"
echo "=================================="

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

print_status "Docker and Docker Compose are installed"

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p chore_data logs
print_status "Directories created"

# Check if .env file exists, create if needed
if [ ! -f ".env" ]; then
    echo "⚙️ Creating .env file..."
    cat > .env << EOF
# Chore Tracker Environment Configuration
FLASK_ENV=production
FLASK_DEBUG=False
DATABASE_URL=sqlite:///data/chore_tracker.db
EOF
    print_status "Environment file created"
else
    print_warning ".env file already exists, skipping creation"
fi

# Build and start the application
echo "🔨 Building and starting application..."
if docker-compose up -d --build; then
    print_status "Application started successfully"
else
    print_error "Failed to start application"
    exit 1
fi

# Wait for the application to be ready
echo "⏳ Waiting for application to be ready..."
sleep 10

# Check if the application is running
if curl -f http://localhost:5000/ > /dev/null 2>&1; then
    print_status "Application is running at http://localhost:5000"
else
    print_warning "Application may still be starting. Check logs with: docker-compose logs"
fi

# Display status
echo ""
echo "📊 Application Status:"
echo "======================"
docker-compose ps

echo ""
echo "📋 Useful Commands:"
echo "==================="
echo "View logs:           docker-compose logs -f"
echo "Stop application:    docker-compose down"
echo "Restart application: docker-compose restart"
echo "View database:       ls -la chore_data/"
echo ""

echo "🎉 Deployment complete!"
echo "📍 Open your browser to: http://localhost:5000"