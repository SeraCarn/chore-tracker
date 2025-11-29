#!/bin/bash

# Chore Tracker Docker Cleanup Script

echo "🧹 Chore Tracker Docker Cleanup"
echo "================================"

# Colors for output
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Function to print colored output
print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_status() {
    echo -e "${GREEN}✓ $1${NC}"
}

# Stop and remove containers
echo "🛑 Stopping and removing containers..."
if docker-compose down; then
    print_status "Containers stopped and removed"
else
    print_warning "No containers found to remove"
fi

# Remove Docker images
echo "🗑️ Removing Docker images..."
if docker-compose down --rmi all; then
    print_status "Images removed"
else
    print_warning "No images found to remove"
fi

# Ask if user wants to remove data
echo ""
read -p "Remove persistent data (database)? [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "💥 Removing persistent data..."
    rm -rf chore_data/
    rm -rf logs/
    print_status "Data removed"
else
    print_status "Data preserved"
fi

# Clean up Docker system (optional)
echo ""
read -p "Clean up unused Docker images and volumes? [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🧹 Cleaning up Docker system..."
    docker system prune -f
    docker volume prune -f
    print_status "Docker system cleaned"
else
    print_status "Docker system preserved"
fi

echo ""
echo "✅ Cleanup complete!"