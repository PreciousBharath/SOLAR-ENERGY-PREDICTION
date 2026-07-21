# Solar Energy Prediction System ☀️

A modern, full-stack web application for predicting solar energy yield using machine learning. Features user authentication, interactive dashboards, and an attractive solar-themed UI with animations.

## 🚀 Features

### User Authentication
- **User Registration**: Secure account creation with password validation
- **User Login**: Remember me functionality and session management
- **Profile Management**: Update personal information and preferences
- **Activity Logging**: Track user actions for security

### Solar Energy Prediction
- **ML-Based Predictions**: Uses trained Random Forest/Gradient Boosting models
- **Weather Input**: Temperature, humidity, wind speed, visibility, pressure, etc.
- **Real-time Results**: Instant solar power yield predictions
- **Prediction History**: Store and retrieve all predictions
- **Analytics Dashboard**: View trends and statistics

### User Interface
- **Solar Energy Theme**: Attractive orange/gold color scheme with animations
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Smooth Animations**: Fade-in, slide-up, and scaling animations
- **Popup Notifications**: Toast-style alerts for user feedback
- **Interactive Charts**: Chart.js integration for data visualization
- **Dark/Light Theme**: User preference settings (ready to implement)

## 📋 Requirements

- Python 3.8+
- Flask 2.3.3
- SQLAlchemy (ORM for database)
- Flask-Login (authentication)
- scikit-learn (ML models)
- pandas (data processing)
- numpy (numerical operations)

## 🔧 Installation

### 1. Clone/Download the Project
```bash
cd "SOLAR ENEGY PREDICTION\SOLAR ENEGY PREDICTION"
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train ML Model (First time only)
```bash
python model.py
```
This generates:
- `best_model.pkl` - Trained ML model
- `scaler.pkl` - Data scaler for normalization

### 5. Run the Application
```bash
python run.py
```

The application will start at: **http://localhost:5000**

## 📊 File Structure

```
SOLAR ENEGY PREDICTION/
├── app_new.py                 # Main Flask application
├── models.py                  # Database models (User, Prediction, ActivityLog)
├── config.py                  # Configuration settings
├── model.py                   # ML model training script
├── run.py                     # Application entry point
├── requirements.txt           # Python dependencies
├── best_model.pkl            # Trained ML model
├── scaler.pkl                # Data scaler
├── spg.csv                   # Training dataset
│
├── templates/                 # HTML templates
│   ├── base.html            # Base template with navbar
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   ├── dashboard.html       # User dashboard
│   ├── predict.html         # Prediction form
│   ├── history.html         # Prediction history
│   ├── analytics.html       # Analytics dashboard
│   ├── profile.html         # User profile
│   ├── 404.html            # 404 error page
│   └── 500.html            # 500 error page
│
├── static/
│   ├── css/
│   │   └── style.css       # Complete styling with animations
│   └── js/
│       └── app.js          # JavaScript utilities and interactions
│
└── solar_energy.db          # SQLite database (auto-created)
```

## 🔐 Default User (Optional)

After first run, you can create test users or access the registration page at:
**http://localhost:5000/register**

## 🎯 Usage

### 1. Register Account
- Go to http://localhost:5000/register
- Fill in username, email, password (min 8 chars, 1 uppercase, 1 digit)
- Click "Create Account"

### 2. Make Predictions
- Log in to your account
- Click "Predict" from navigation
- Input weather parameters:
  - Distance to solar noon (minutes)
  - Temperature (°C)
  - Wind speed (m/s)
  - Sky cover (0-1)
  - Visibility (km)
  - Humidity (%)
  - Wind direction (degrees)
  - Pressure (hPa)
- View instant solar power prediction

### 3. View History
- Click "History" to see all your predictions
- Search predictions by date or power value
- Delete predictions individually
- View weather parameters for each prediction

### 4. Analytics
- Click "Analytics" for statistics
- View average, max, min predictions
- See predictions from last 7 days
- Interactive trend chart with Chart.js

### 5. Manage Profile
- Click profile icon → "Profile"
- Update full name and company
- View account information
- Change theme preferences (future feature)

## 🎨 Customization

### Change Colors
Edit the CSS variables in `static/css/style.css`:
```css
:root {
    --primary-color: #FFB03B;      /* Solar orange */
    --secondary-color: #1A237E;    /* Dark blue */
    --accent-color: #00BCD4;       /* Cyan */
    /* ... more colors ... */
}
```

### Modify Solar Background Animation
Edit the animation in `static/css/style.css`:
- `.sun` - Pulsing sun effect
- `.solar-ray` - Rotating rays animation
- Adjust timing and colors as needed

### Add New ML Models
Edit `model.py` to test different algorithms:
```python
from sklearn.svm import SVR
# Add SVR to models dictionary
models["Support Vector Regression"] = SVR()
```

## 🚨 Troubleshooting

### Issue: "Module not found"
**Solution**: Make sure virtual environment is activated and all packages installed
```bash
pip install -r requirements.txt
```

### Issue: Database locked error
**Solution**: Delete `solar_energy.db` and restart the app (existing data will be lost)
```bash
rm solar_energy.db  # or del solar_energy.db on Windows
python run.py
```

### Issue: Port 5000 already in use
**Solution**: Change the port in `run.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Use port 8000
```

### Issue: ML model not loading
**Solution**: Re-train the model
```bash
python model.py
```

## 📈 Performance Tips

1. **Database Optimization**: Add indexes to frequently queried columns
2. **Caching**: Use Flask-Caching for expensive operations
3. **Async Tasks**: Use Celery for background prediction jobs
4. **API Rate Limiting**: Implement rate limiting for API endpoints

## 🔒 Security Notes

- ✓ Passwords are hashed with bcrypt
- ✓ CSRF protection enabled
- ✓ SQL injection prevention via SQLAlchemy ORM
- ✓ Session management with Flask-Login
- ✓ Form validation on both client and server

### For Production:
1. Set `SECRET_KEY` to a secure random value
2. Set `DEBUG = False`
3. Use a production database (PostgreSQL recommended)
4. Enable HTTPS
5. Set secure cookie settings
6. Use environment variables for sensitive data

## 📚 Technologies Used

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite (development), PostgreSQL recommended for production
- **Machine Learning**: scikit-learn, pandas, numpy
- **Charts**: Chart.js
- **Icons**: Font Awesome 6

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Submit pull requests

## 📝 License

This project is open source and available for educational and commercial use.

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the file structure
3. Check console logs for errors

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [scikit-learn](https://scikit-learn.org/)
- [Chart.js](https://www.chartjs.org/)

---

**Happy Predicting! ☀️🔋**
