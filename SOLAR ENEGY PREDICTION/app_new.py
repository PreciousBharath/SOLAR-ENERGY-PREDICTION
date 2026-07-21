from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import config
from models import db, User, Prediction, ActivityLog
from werkzeug.security import generate_password_hash, check_password_hash
import pickle
import numpy as np
import os
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define project paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / 'best_model.pkl'
SCALER_PATH = BASE_DIR / 'scaler.pkl'
DATA_PATH = BASE_DIR / 'solar_dataset.csv' if (BASE_DIR / 'solar_dataset.csv').exists() else BASE_DIR / 'spg.csv'

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(config[os.environ.get('FLASK_ENV', 'development')])

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

# Load ML model and scaler
model = None
scaler = None

def load_ml_resources():
    global model, scaler
    try:
        with MODEL_PATH.open('rb') as model_file:
            model = pickle.load(model_file)
        with SCALER_PATH.open('rb') as scaler_file:
            scaler = pickle.load(scaler_file)
        print('✓ ML model and scaler loaded successfully')
    except Exception as e:
        print(f'Warning: Could not load ML model: {e}')
        model = None
        scaler = None


def ensure_ml_resources():
    global model, scaler
    if model is not None and scaler is not None:
        return
    if MODEL_PATH.exists() and SCALER_PATH.exists():
        load_ml_resources()
        return
    if DATA_PATH.exists():
        print('ML resources missing, attempting to train a new model from spg.csv...')
        try:
            from model import train_model
            train_model()
            load_ml_resources()
        except Exception as e:
            print(f'Warning: Could not auto-train ML model: {e}')
            model = None
            scaler = None


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ==================== HELPER FUNCTIONS ====================

def log_activity(user_id, action, description="", ip_address=None):
    """Log user activity"""
    if ip_address is None:
        ip_address = request.remote_addr
    
    log = ActivityLog(
        user_id=user_id,
        action=action,
        description=description,
        ip_address=ip_address
    )
    db.session.add(log)
    db.session.commit()

def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit"
    return True, "Password is strong"

# ==================== ROUTES ====================

@app.route('/')
def index():
    """Home page"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        full_name = request.form.get('full_name', '').strip()
        company = request.form.get('company', '').strip()
        
        # Validation
        if not username or not email or not password:
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        if len(username) < 3:
            return jsonify({'success': False, 'message': 'Username must be at least 3 characters'}), 400
        
        if User.query.filter_by(username=username).first():
            return jsonify({'success': False, 'message': 'Username already exists'}), 400
        
        if User.query.filter_by(email=email).first():
            return jsonify({'success': False, 'message': 'Email already registered'}), 400
        
        if password != confirm_password:
            return jsonify({'success': False, 'message': 'Passwords do not match'}), 400
        
        is_valid, msg = validate_password(password)
        if not is_valid:
            return jsonify({'success': False, 'message': msg}), 400
        
        # Create user
        try:
            user = User(
                username=username,
                email=email,
                full_name=full_name,
                company=company
            )
            user.set_password(password)
            
            db.session.add(user)
            db.session.commit()
            
            log_activity(user.id, 'REGISTRATION', 'User registered successfully')
            
            return jsonify({
                'success': True,
                'message': 'Registration successful! Please log in.',
                'redirect': url_for('login')
            })
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Registration failed. Please try again.'}), 500
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember')
        
        if not username or not password:
            return jsonify({'success': False, 'message': 'Username and password required'}), 400
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            if not user.is_active:
                return jsonify({'success': False, 'message': 'Account is inactive'}), 403
            
            login_user(user, remember=bool(remember))
            log_activity(user.id, 'LOGIN', 'User logged in successfully')
            
            return jsonify({
                'success': True,
                'message': 'Login successful!',
                'redirect': url_for('dashboard')
            })
        else:
            return jsonify({'success': False, 'message': 'Invalid username or password'}), 401
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """User logout"""
    log_activity(current_user.id, 'LOGOUT', 'User logged out')
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    # Get statistics
    total_predictions = Prediction.query.filter_by(user_id=current_user.id).count()
    recent_predictions = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.created_at.desc()).limit(5).all()
    
    avg_power = 0
    if total_predictions > 0:
        predictions = db.session.query(db.func.avg(Prediction.predicted_power)).filter_by(user_id=current_user.id).scalar()
        avg_power = round(predictions, 2) if predictions else 0
    
    stats = {
        'total_predictions': total_predictions,
        'avg_power': avg_power,
        'recent_predictions': recent_predictions
    }
    
    return render_template('dashboard.html', stats=stats, user=current_user)

@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    """Make solar energy predictions"""
    if request.method == 'POST':
        try:
            # Get form data
            angle_of_incidence = float(request.form.get('angle_of_incidence', 0))
            temperature = float(request.form.get('temperature_2_m_above_gnd', 0))
            wind_speed = float(request.form.get('wind_speed_10_m_above_gnd', 0))
            sky_cover = float(request.form.get('total_cloud_cover_sfc', 0))
            solar_radiation = float(request.form.get('shortwave_radiation_backwards_sfc', 0))
            humidity = float(request.form.get('relative_humidity_2_m_above_gnd', 0))
            wind_direction = float(request.form.get('wind_direction_10_m_above_gnd', 0))
            pressure = float(request.form.get('mean_sea_level_pressure_MSL', 0))
            # Prepare data for prediction
            input_data = np.array([[
                angle_of_incidence, temperature, wind_speed, sky_cover,
                solar_radiation, humidity, wind_direction, pressure
            ]])
            # Ensure loader is available before prediction
            ensure_ml_resources()
            if model is None or scaler is None:
                return jsonify({'success': False, 'message': 'ML model not loaded'}), 500

            # Scale data
            scaled_data = scaler.transform(input_data)
            
            # Make prediction
            predicted_power = model.predict(scaled_data)[0]
            
            # Round to 2 decimal places
            predicted_power = max(0, round(predicted_power, 2))
            
            # Save prediction to database
            prediction = Prediction(
                user_id=current_user.id,
                distance_to_solar_noon=angle_of_incidence,
                temperature=temperature,
                wind_speed=wind_speed,
                sky_cover=sky_cover,
                visibility=solar_radiation,
                humidity=humidity,
                wind_direction=wind_direction,
                pressure=pressure,
                predicted_power=predicted_power,
                confidence=0.95
            )
            
            db.session.add(prediction)
            db.session.commit()
            
            log_activity(current_user.id, 'PREDICTION', f'Solar energy prediction: {predicted_power}kW')
            
            return jsonify({
                'success': True,
                'predicted_power': predicted_power,
                'message': f'Prediction successful! Predicted solar power: {predicted_power} kW'
            })
        
        except ValueError:
            return jsonify({'success': False, 'message': 'Invalid input values'}), 400
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Prediction failed. Please try again.'}), 500
    
    return render_template('predict.html', user=current_user)

@app.route('/history')
@login_required
def history():
    """View prediction history"""
    page = request.args.get('page', 1, type=int)
    predictions = Prediction.query.filter_by(user_id=current_user.id).order_by(
        Prediction.created_at.desc()
    ).paginate(page=page, per_page=10)
    
    return render_template('history.html', predictions=predictions, user=current_user)

@app.route('/analytics')
@login_required
def analytics():
    """View analytics and statistics"""
    predictions = Prediction.query.filter_by(user_id=current_user.id).all()
    
    if predictions:
        powers = [p.predicted_power for p in predictions]
        stats = {
            'total': len(predictions),
            'average': round(sum(powers) / len(powers), 2),
            'max': round(max(powers), 2),
            'min': round(min(powers), 2),
            'last_7_days': len([p for p in predictions if p.created_at > datetime.utcnow() - timedelta(days=7)])
        }
    else:
        stats = {'total': 0, 'average': 0, 'max': 0, 'min': 0, 'last_7_days': 0}
    
    return render_template('analytics.html', stats=stats, user=current_user)

@app.route('/profile')
@login_required
def profile():
    """User profile"""
    return render_template('profile.html', user=current_user)

@app.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    """Update user profile"""
    try:
        full_name = request.form.get('full_name', '').strip()
        company = request.form.get('company', '').strip()
        theme = request.form.get('theme', 'light')
        
        current_user.full_name = full_name
        current_user.company = company
        current_user.theme = theme
        
        db.session.commit()
        log_activity(current_user.id, 'PROFILE_UPDATE', 'User profile updated')
        
        return jsonify({'success': True, 'message': 'Profile updated successfully!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'Profile update failed'}), 500

@app.route('/api/predictions/chart')
@login_required
def predictions_chart_data():
    """Get chart data for predictions"""
    predictions = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.created_at).all()
    
    data = {
        'dates': [p.created_at.strftime('%Y-%m-%d %H:%M') for p in predictions],
        'powers': [p.predicted_power for p in predictions]
    }
    
    return jsonify(data)

@app.route('/api/predictions/delete/<int:prediction_id>', methods=['DELETE'])
@login_required
def delete_prediction(prediction_id):
    """Delete a prediction"""
    prediction = Prediction.query.get(prediction_id)
    
    if not prediction or prediction.user_id != current_user.id:
        return jsonify({'success': False, 'message': 'Prediction not found'}), 404
    
    try:
        db.session.delete(prediction)
        db.session.commit()
        log_activity(current_user.id, 'PREDICTION_DELETE', f'Deleted prediction {prediction_id}')
        
        return jsonify({'success': True, 'message': 'Prediction deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'Failed to delete prediction'}), 500

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """500 error handler"""
    db.session.rollback()
    return render_template('500.html'), 500

# ==================== APPLICATION CONTEXT ====================

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Prediction': Prediction}

# ==================== DATABASE INITIALIZATION ====================

def init_db():
    """Initialize database"""
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")

if __name__ == '__main__':
    # Initialize database on first run
    if not os.path.exists('solar_energy.db'):
        init_db()
    
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
