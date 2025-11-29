#!/bin/bash

# Chore Tracker Startup Script

echo "🚀 Starting Chore Tracker Application..."
echo "=================================="

# Check if we're in the right directory structure
if [ ! -d "chore_tracker" ]; then
    echo "❌ chore_tracker directory not found. Please run this script from the correct directory."
    echo "Current directory: $(pwd)"
    exit 1
fi

# Navigate to chore_tracker directory
cd chore_tracker

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Setting up now..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Check if database exists, if not run setup
if [ ! -f "chore_tracker.db" ]; then
    echo "⚙️  Setting up database and default data..."
    python3 setup.py
fi

# Start the application
echo "🎮 Starting Flask application..."
echo "📱 Application will be available at: http://localhost:5000"
echo "🛑 Press Ctrl+C to stop the application"
echo ""

python3 app.py
