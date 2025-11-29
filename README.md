# Chore Tracker with Gaming Rewards

A fun web application that helps you track household chores and rewards you with gaming time!

## Features

🎮 **Gaming Time Rewards**: Complete chores to earn points, then use those points for gaming time

🧹 **Chore Tracking**: Add, track, and complete various household chores

📊 **Progress Dashboard**: See your total points, available gaming time, and recent completions

⚙️ **Admin Panel**: Manage chores, set point values, and configure reward settings

## Quick Start

1. **Install Dependencies**
   ```bash
   cd chore_tracker
   pip install -r requirements.txt
   ```

2. **Setup the Application**
   ```bash
   python setup.py
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Open your browser** and go to `http://localhost:5000`

## How It Works

1. **Complete Chores**: Go to the "Chores" section and mark chores as completed
2. **Earn Points**: Each chore has a point value that you earn when completed
3. **Get Gaming Time**: Use your points to get minutes of gaming time (configurable ratio)
4. **Track Progress**: See your progress on the dashboard and manage active gaming sessions

## Default Chores

The app comes with these default chores:
- Make Bed (5 points)
- Do Dishes (10 points)
- Vacuum Living Room (15 points)
- Take Out Trash (8 points)
- Clean Bathroom (25 points)
- Do Laundry (20 points)
- Sweep Kitchen (12 points)
- Water Plants (5 points)
- Clean Room (15 points)
- Help with Dinner (10 points)

## Customization

- **Add Chores**: Use the Admin panel to add new chores with custom point values
- **Adjust Rewards**: Change how many points are needed for each minute of gaming
- **Daily Bonuses**: Set up daily login bonuses

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, Bootstrap 5, Font Awesome
- **Styling**: Custom CSS with gradients and animations

## Files Structure

```
chore_tracker/
├── app.py              # Main Flask application
├── setup.py            # Setup script with default data
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── base.html       # Base template with navigation
│   ├── index.html      # Dashboard
│   ├── chores.html     # Chore list and completion
│   ├── gaming.html     # Gaming time management
│   └── admin.html      # Admin panel
└── chore_tracker.db    # SQLite database (created on first run)
```

## Future Enhancements

- Mobile app version
- Multi-user support for families
- Weekly/monthly challenges
- Achievement system
- Integration with gaming platforms
- Notifications and reminders

## Troubleshooting

**Database Issues**: If you encounter database errors, try deleting the `chore_tracker.db` file and running `python setup.py` again.

**Port Already In Use**: If port 5000 is busy, edit `app.py` and change `app.run(debug=True)` to `app.run(debug=True, port=5001)`.

**Permission Errors**: Make sure you have write permissions in the directory for the database file.

## License

This project is open source and available under the MIT License.