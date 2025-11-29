# Chore Tracker Quick Reference

## 🎮 Getting Started

```bash
./start_app.sh
```
Visit: http://localhost:5000

## 📋 URL Reference

- **Dashboard**: http://localhost:5000/ - Main overview
- **Chores**: http://localhost:5000/chores - Complete chores
- **Gaming**: http://localhost:5000/gaming - Manage gaming time
- **Admin**: http://localhost:5000/admin - Add/edit chores

## 🎯 Point System

- **Default**: 10 points = 1 minute of gaming
- **Configurable**: Change in Admin panel
- **Earn Points**: Complete chores to earn points
- **Spend Points**: Use for gaming sessions

## 📝 Default Chores

| Chore | Points | Description |
|-------|--------|-------------|
| Make Bed | 5 | Make your bed every morning |
| Do Dishes | 10 | Wash all dirty dishes |
| Vacuum Living Room | 15 | Vacuum the living room floor |
| Take Out Trash | 8 | Take out all trash and recycling |
| Clean Bathroom | 25 | Clean sink, toilet, and shower |
| Do Laundry | 20 | Wash, dry, and fold laundry |
| Sweep Kitchen | 12 | Sweep and mop the kitchen floor |
| Water Plants | 5 | Water all house plants |
| Clean Room | 15 | Tidy up your bedroom |
| Help with Dinner | 10 | Help prepare or clean up dinner |

## 🔧 Admin Features

### Adding Chores
1. Go to Admin panel
2. Fill in chore name, description, and point value
3. Click "Add Chore"

### Settings
- **Points per Minute**: How many points needed for 1 minute of gaming
- **Daily Bonus**: Bonus points for daily login

## 💡 Tips

1. **Customize Chores**: Add chores specific to your household
2. **Adjust Points**: Make difficult chores worth more points
3. **Track Progress**: Use the dashboard to see your progress
4. **Set Limits**: Use the gaming time management to set healthy limits

## 🚀 Commands

```bash
# Start app with setup
./start_app.sh

# Manual setup
cd chore_tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 setup.py

# Start app
python3 app.py

# Demo mode
./demo.sh
```

## 🛠️ File Structure

```
chore_tracker/
├── app.py          # Main application
├── config.py       # Settings
├── setup.py        # Database setup
├── chore_tracker.db # SQLite database
└── templates/      # Web pages
    ├── base.html   # Layout
    ├── index.html  # Dashboard
    ├── chores.html # Chore list
    ├── gaming.html # Gaming time
    └── admin.html  # Admin panel
```

## 🎮 How It Works

1. **Complete Chores** → Earn Points
2. **Earn Points** → Get Gaming Time
3. **Track Progress** → Stay Motivated
4. **Have Fun** → Balance Work & Play

That's it! Start tracking and gaming! 🎮✨