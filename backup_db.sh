#!/bin/bash

# Chore Tracker Database Backup Script

echo "💾 Chore Tracker Database Backup"
echo "================================="

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

# Create backup directory
BACKUP_DIR="backups"
mkdir -p "$BACKUP_DIR"

# Generate timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/chore_tracker_backup_$TIMESTAMP.db"

# Check if chore_data directory exists
if [ ! -d "chore_data" ]; then
    print_error "chore_data directory not found. Make sure the application has been deployed."
    exit 1
fi

# Check if database file exists
if [ ! -f "chore_data/chore_tracker.db" ]; then
    print_error "Database file not found. Make sure the application is running."
    exit 1
fi

# Create backup
echo "📦 Creating backup..."
if cp chore_data/chore_tracker.db "$BACKUP_FILE"; then
    # Get file size
    SIZE=$(ls -lh "$BACKUP_FILE" | awk '{print $5}')
    print_status "Backup created: $BACKUP_FILE ($SIZE)"
    
    # List recent backups
    echo ""
    echo "📋 Recent backups:"
    ls -lh "$BACKUP_DIR"/chore_tracker_backup_*.db 2>/dev/null | tail -5 || echo "No previous backups found"
    
    # Ask if user wants to keep only recent backups
    echo ""
    read -p "Keep only the last 5 backups? [y/N]: " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🧹 Cleaning up old backups..."
        ls -t "$BACKUP_DIR"/chore_tracker_backup_*.db 2>/dev/null | tail -n +6 | xargs -r rm
        print_status "Old backups removed"
    fi
    
else
    print_error "Failed to create backup"
    exit 1
fi

echo ""
echo "✅ Backup complete!"
echo "📍 Backup location: $BACKUP_FILE"