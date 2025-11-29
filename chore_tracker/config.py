# Chore Tracker Configuration

# Points System
POINTS_PER_MINUTE = 10  # How many points needed for 1 minute of gaming
DAILY_BONUS_POINTS = 20  # Bonus points for daily login

# Default Chores
DEFAULT_CHORES = [
    {"name": "Make Bed", "description": "Make your bed every morning", "points": 5},
    {"name": "Do Dishes", "description": "Wash all dirty dishes", "points": 10},
    {"name": "Vacuum Living Room", "description": "Vacuum the living room floor", "points": 15},
    {"name": "Take Out Trash", "description": "Take out all trash and recycling", "points": 8},
    {"name": "Clean Bathroom", "description": "Clean the bathroom sink, toilet, and shower", "points": 25},
    {"name": "Do Laundry", "description": "Wash, dry, and fold laundry", "points": 20},
    {"name": "Sweep Kitchen", "description": "Sweep and mop the kitchen floor", "points": 12},
    {"name": "Water Plants", "description": "Water all house plants", "points": 5},
    {"name": "Clean Room", "description": "Tidy up your bedroom", "points": 15},
    {"name": "Help with Dinner", "description": "Help prepare or clean up dinner", "points": 10},
]

# App Settings
SECRET_KEY = 'your-secret-key-change-this-in-production'
DEBUG = True