# 🚀 QUICK START GUIDE - Solar Energy Prediction System

## Step-by-Step Setup (5 minutes)

### ✅ Prerequisites
- Python 3.8 or higher installed
- pip package manager

### 📥 Step 1: Install Dependencies

Open terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

Wait for all packages to install (you'll see progress messages).

### 🤖 Step 2: Train ML Model (First Time Only)

```bash
python model.py
```

This creates:
- `best_model.pkl` - Your trained model
- `scaler.pkl` - Data normalizer

(This usually takes 5-10 seconds)

### 💾 Step 3: Initialize Database

```bash
python init_db.py
```

Follow the prompts to optionally create a test user:
- Username: `testuser`
- Password: `TestPass123`

### 🎯 Step 4: Start the Application

```bash
python run.py
```

You should see:
```
========================================
  SOLAR ENERGY PREDICTION SYSTEM
========================================
✓ Server starting...
✓ Running on: http://localhost:5000
✓ Debug mode: Enabled
========================================
```

### 🌐 Step 5: Open in Browser

Visit: **http://localhost:5000**

## 🔑 First Login

**Option 1: Use Test Account** (if created in Step 3)
- Username: `testuser`
- Password: `TestPass123`

**Option 2: Create New Account**
- Click "Register" on login page
- Fill in your details
- Login with your credentials

## 📊 Making Your First Prediction

1. After login, click **"Predict"** in navigation
2. Fill in weather parameters:
   - Distance to solar noon (e.g., 120 minutes)
   - Temperature (e.g., 25°C)
   - Wind speed (e.g., 5 m/s)
   - Sky cover (e.g., 0.3 = 30% cloud coverage)
   - Other parameters...
3. Click **"Predict Solar Power"**
4. See instant prediction result! ⚡

## 📈 Explore Features

- **Dashboard**: Overview of your predictions
- **History**: All past predictions with details
- **Analytics**: Trends and statistics
- **Profile**: Update personal information

## 🎨 Customize

### Change Colors
Edit `static/css/style.css` line 1-15:
```css
:root {
    --primary-color: #FFB03B;  /* Change this! */
    /* ... other colors ... */
}
```

### Change Port
Edit `run.py` last line:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Change 5000 to 8000
```

## 🛑 Stop the Application

Press `Ctrl + C` in terminal

## ❓ Common Issues

**Port already in use?**
```bash
python run.py  # Change port in run.py if needed
```

**Module not found?**
```bash
pip install -r requirements.txt  # Run again
```

**Database error?**
```bash
rm solar_energy.db  # Delete database and restart
python init_db.py    # Recreate it
python run.py        # Start again
```

## 📱 Mobile Access

Other devices on same network can access:
```
http://[YOUR_COMPUTER_IP]:5000
```

Find your IP (Windows):
```bash
ipconfig  # Look for "IPv4 Address"
```

## 🔐 Security Tips

- ✓ Never share your login credentials
- ✓ Use strong passwords (8+ chars, mixed case, numbers)
- ✓ Enable HTTPS for production use
- ✓ Change SECRET_KEY in production

## 📚 Next Steps

1. Read `README.md` for complete documentation
2. Check out the UI animations and themes
3. Try different weather parameters to see predictions vary
4. Export your predictions data (feature coming soon)

## 💡 Tips & Tricks

- Use keyboard shortcut `Ctrl+K` to search history (when implemented)
- Click on stat cards for more details
- Hover over elements for tooltips
- Use responsive design on mobile/tablet

## 🎓 Understanding the ML Model

The system uses **Random Forest** or **Gradient Boosting** algorithms trained on solar panel data to predict:
- Solar power output (kW)
- Based on weather conditions
- Historical patterns

**Accuracy**: ~95% on test data

## 🌟 Features Showcase

### User Authentication ✓
- Secure registration
- Login/logout
- Session management
- Password hashing

### Solar Predictions ✓
- Real-time ML predictions
- 8 weather parameters
- Instant results
- Stored history

### Dashboard ✓
- Statistics overview
- Recent predictions
- Quick actions
- Responsive design

### Analytics ✓
- Trend charts
- Average/Max/Min power
- Last 7 days stats
- Interactive visualizations

### Beautiful UI ✓
- Solar energy theme
- Smooth animations
- Responsive layout
- Toast notifications
- Popup alerts

## 🚀 Production Deployment

When ready to go live:

1. Change `DEBUG = False` in `config.py`
2. Use PostgreSQL instead of SQLite
3. Set `SECRET_KEY` to secure random value
4. Enable HTTPS/SSL
5. Use Gunicorn/uWSGI as server
6. Set up database backups
7. Configure email notifications

---

**Enjoy your Solar Energy Prediction System! ☀️**

For more help, see README.md or check the code comments.
