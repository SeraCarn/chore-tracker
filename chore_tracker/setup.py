import sys
import os
from datetime import datetime

# Add the parent directory to the path so we can import from the app
sys.path.append('/app')

try:
    from chore_tracker.app import db, Chore, UserSettings
    from chore_tracker.config import POINTS_PER_MINUTE, DAILY_BONUS_POINTS, DEFAULT_CHORES
except ImportError:
    # Fallback for when running directly
    from app import db, Chore, UserSettings
    from config import POINTS_PER_MINUTE, DAILY_BONUS_POINTS, DEFAULT_CHORES

def setup_database():
    """Initialize the database with tables and default data"""
    try:
        # Create all tables
        db.create_all()
        print("✓ Database tables created successfully")
        
        # Create default settings if none exist
        if not UserSettings.query.first():
            settings = UserSettings(
                points_per_minute=POINTS_PER_MINUTE,
                daily_bonus_points=DAILY_BONUS_POINTS
            )
            db.session.add(settings)
            db.session.commit()
            print("✓ Default user settings created")
        else:
            print("✓ User settings already exist")
        
        # Add some default chores if none exist
        existing_chores = Chore.query.count()
        if existing_chores == 0:
            chores = []
            for chore_data in DEFAULT_CHORES:
                chore = Chore(
                    name=chore_data['name'],
                    description=chore_data['description'],
                    points_value=chore_data['points']
                )
                chores.append(chore)
            
            for chore in chores:
                db.session.add(chore)
            
            db.session.commit()
            print(f"✓ Added {len(chores)} default chores")
        else:
            print(f"✓ Found {existing_chores} existing chores")
            
        print("🎉 Database setup completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error during database setup: {e}")
        db.session.rollback()
        return False

if __name__ == "__main__":
    print("🚀 Starting database setup...")
    success = setup_database()
    if success:
        print("✅ Setup complete! You can now start the application.")
    else:
        print("❌ Setup failed. Please check the error messages above.")
        sys.exit(1)
