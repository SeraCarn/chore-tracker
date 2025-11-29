from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

# Import config
try:
    from config import *
except ImportError:
    # Fallback defaults
    SECRET_KEY = 'fallback-secret-key'
    DEBUG = True
    POINTS_PER_MINUTE = 10
    DAILY_BONUS_POINTS = 20

app = Flask(__name__)

# Configuration - allow database URL override for Docker
database_url = os.environ.get('DATABASE_URL', 'sqlite:///chore_tracker.db')

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = DEBUG

db = SQLAlchemy(app)

# Models
class Chore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    points_value = db.Column(db.Integer, default=10)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ChoreCompletion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chore_id = db.Column(db.Integer, db.ForeignKey('chore.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)
    
    chore = db.relationship('Chore', backref=db.backref('completions', lazy=True))

class GamingSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duration_minutes = db.Column(db.Integer, nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    ended_at = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=False)

class UserSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points_per_minute = db.Column(db.Integer, default=1)  # How many points needed for 1 minute of gaming
    daily_bonus_points = db.Column(db.Integer, default=20)  # Daily login bonus
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize database and default data
@app.before_request
def create_tables():
    # Check if tables exist, create them if not
    try:
        db.create_all()
        # Create default settings if none exist
        if not UserSettings.query.first():
            settings = UserSettings()
            db.session.add(settings)
            db.session.commit()
    except Exception as e:
        # If there's an error (like tables don't exist yet), create them
        db.create_all()
        if not UserSettings.query.first():
            settings = UserSettings()
            db.session.add(settings)
            db.session.commit()

# Routes
@app.route('/')
def index():
    settings = UserSettings.query.first()
    total_points = sum(completion.chore.points_value for completion in ChoreCompletion.query.all())
    available_minutes = total_points // settings.points_per_minute
    
    # Get recent completions
    recent_completions = ChoreCompletion.query.order_by(ChoreCompletion.completed_at.desc()).limit(10).all()
    
    # Get active gaming session
    active_session = GamingSession.query.filter_by(is_active=True).first()
    
    return render_template('index.html', 
                         total_points=total_points,
                         available_minutes=available_minutes,
                         recent_completions=recent_completions,
                         active_session=active_session)

@app.route('/chores')
def chores():
    chores = Chore.query.filter_by(is_active=True).all()
    return render_template('chores.html', chores=chores)

@app.route('/complete_chore/<int:chore_id>', methods=['POST'])
def complete_chore(chore_id):
    chore = Chore.query.get_or_404(chore_id)
    completion = ChoreCompletion(chore_id=chore_id, notes=request.form.get('notes', ''))
    db.session.add(completion)
    db.session.commit()
    
    flash(f'Great job! You earned {chore.points_value} points for completing "{chore.name}"', 'success')
    return redirect(url_for('index'))

@app.route('/gaming')
def gaming():
    settings = UserSettings.query.first()
    total_points = sum(completion.chore.points_value for completion in ChoreCompletion.query.all())
    available_minutes = total_points // settings.points_per_minute
    
    active_session = GamingSession.query.filter_by(is_active=True).first()
    recent_sessions = GamingSession.query.filter_by(is_active=False).order_by(GamingSession.ended_at.desc()).limit(10).all()
    
    return render_template('gaming.html', 
                         available_minutes=available_minutes,
                         active_session=active_session,
                         recent_sessions=recent_sessions)

@app.route('/start_gaming', methods=['POST'])
def start_gaming():
    minutes_requested = int(request.form.get('minutes', 0))
    
    settings = UserSettings.query.first()
    total_points = sum(completion.chore.points_value for completion in ChoreCompletion.query.all())
    max_available_minutes = total_points // settings.points_per_minute
    
    if minutes_requested > max_available_minutes:
        flash(f'Not enough points! You need {minutes_requested * settings.points_per_minute} points but only have {total_points}', 'error')
        return redirect(url_for('gaming'))
    
    # Deduct points (we'll track this separately)
    session = GamingSession(duration_minutes=minutes_requested, is_active=True)
    db.session.add(session)
    db.session.commit()
    
    flash(f'Gaming session started! You have {minutes_requested} minutes available', 'success')
    return redirect(url_for('gaming'))

@app.route('/end_gaming/<int:session_id>', methods=['POST'])
def end_gaming(session_id):
    session = GamingSession.query.get_or_404(session_id)
    session.ended_at = datetime.utcnow()
    session.is_active = False
    db.session.commit()
    
    flash('Gaming session ended successfully!', 'success')
    return redirect(url_for('gaming'))

@app.route('/admin')
def admin():
    chores = Chore.query.all()
    settings = UserSettings.query.first()
    return render_template('admin.html', chores=chores, settings=settings)

@app.route('/add_chore', methods=['POST'])
def add_chore():
    name = request.form.get('name')
    description = request.form.get('description', '')
    points_value = int(request.form.get('points_value', 10))
    
    if name:
        chore = Chore(name=name, description=description, points_value=points_value)
        db.session.add(chore)
        db.session.commit()
        flash('Chore added successfully!', 'success')
    
    return redirect(url_for('admin'))

@app.route('/api/points')
def api_points():
    total_points = sum(completion.chore.points_value for completion in ChoreCompletion.query.all())
    settings = UserSettings.query.first()
    available_minutes = total_points // settings.points_per_minute
    
    return jsonify({
        'total_points': total_points,
        'available_minutes': available_minutes
    })

if __name__ == '__main__':
    # For Docker, we use environment variables to control the host and port
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(host=host, port=port, debug=debug)
