#!/bin/bash

# Demo script to show the Chore Tracker in action

echo "🎮 Chore Tracker Demo"
echo "===================="
echo ""
echo "This demo will show you how the Chore Tracker app works!"
echo ""

# Start the app in the background
echo "🚀 Starting the application..."
source chore_tracker/venv/bin/activate
cd chore_tracker
python3 app.py &
APP_PID=$!

# Wait for app to start
sleep 3

echo "📱 App is now running at http://localhost:5000"
echo "🎯 You can now:"
echo ""
echo "1. Visit http://localhost:5000 to see the dashboard"
echo "2. Go to http://localhost:5000/chores to see available chores"
echo "3. Go to http://localhost:5000/gaming to manage gaming time"
echo "4. Go to http://localhost:5000/admin to add new chores"
echo ""
echo "Default chores include:"
echo "  - Make Bed (5 points)"
echo "  - Do Dishes (10 points)"
echo "  - Vacuum Living Room (15 points)"
echo "  - Take Out Trash (8 points)"
echo "  - Clean Bathroom (25 points)"
echo "  - And more..."
echo ""
echo "💡 How it works:"
echo "  1. Complete chores to earn points"
echo "  2. Use points for gaming time (10 points = 1 minute)"
echo "  3. Track your progress on the dashboard"
echo ""
echo "🛑 To stop the demo, press Ctrl+C"
echo ""

# Wait for user to stop
wait $APP_PID