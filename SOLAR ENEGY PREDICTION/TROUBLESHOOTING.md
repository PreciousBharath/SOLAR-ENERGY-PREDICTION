# 🆘 TROUBLESHOOTING GUIDE

## Common Issues & Solutions

---

## 1️⃣ Python & Installation Issues

### Issue: "pip: command not found"
**Cause**: Python or pip not installed  
**Solution**:
```bash
# Check if Python is installed
python --version

# If not, download from: https://www.python.org/downloads/
# During installation, make sure to check "Add Python to PATH"
```

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Cause**: Dependencies not installed  
**Solution**:
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Or install each module individually
pip install flask flask-sqlalchemy flask-login flask-wtf
```

### Issue: "Permission denied" error
**Cause**: Virtual environment issue  
**Solution**:
```bash
# Create fresh virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Then reinstall
pip install -r requirements.txt
```

---

## 2️⃣ Database Issues

### Issue: "database is locked"
**Cause**: Database file is in use  
**Solution**:
```bash
# Stop the running app (Ctrl+C)
# Delete database
rm solar_energy.db  # Linux/Mac
del solar_energy.db  # Windows

# Restart and reinitialize
python init_db.py
python run.py
```

### Issue: "table users does not exist"
**Cause**: Database not initialized  
**Solution**:
```bash
python init_db.py
```

### Issue: Cannot create database file
**Cause**: Permission or path issue  
**Solution**:
```bash
# Check current directory
pwd  # Linux/Mac
cd   # Windows

# Ensure you're in the project folder
cd "SOLAR ENEGY PREDICTION\SOLAR ENEGY PREDICTION"

# Then initialize
python init_db.py
```

---

## 3️⃣ Server Issues

### Issue: "Address already in use" (Port 5000)
**Cause**: Another app using port 5000  
**Solution Option 1** - Change port in run.py:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Use 8000 instead
```

**Solution Option 2** - Find and kill process:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :5000
kill -9 <PID>
```

### Issue: "Host is already in use"
**Cause**: Another Flask app running  
**Solution**:
```bash
# Find and kill all Python processes
# Or use a different port (see above)
```

### Issue: Server won't start
**Cause**: Syntax error or import issue  
**Solution**:
```bash
# Check for syntax errors
python -m py_compile app_new.py

# Try running with verbose output
python -u run.py

# Check terminal for error messages
```

---

## 4️⃣ Frontend Issues

### Issue: Website not loading or looks broken
**Cause**: Cache or static files issue  
**Solution**:
```bash
# Hard refresh browser
Ctrl + Shift + R  # Windows/Linux
Cmd + Shift + R   # Mac

# Or clear browser cache entirely
# Chrome: Settings > Privacy > Clear browsing data
```

### Issue: Styles not loading (white page with text)
**Cause**: CSS file not loading  
**Solution**:
```bash
# Check if static folder exists
# Should have: static/css/style.css and static/js/app.js

# Restart server
# Hard refresh browser
```

### Issue: Animations not working
**Cause**: Browser doesn't support CSS animations  
**Solution**:
```bash
# Update browser to latest version
# Or use different browser
# Check browser console (F12) for errors
```

### Issue: Form not submitting
**Cause**: JavaScript error or server issue  
**Solution**:
```bash
# Open browser console (F12)
# Check for JavaScript errors
# Check terminal for server errors
# Try different browser
```

---

## 5️⃣ Login & Authentication Issues

### Issue: Cannot register
**Cause**: Validation error  
**Solution**:
```bash
# Check password requirements:
# - At least 8 characters
# - At least 1 uppercase letter
# - At least 1 digit
# - Username must be unique
# - Email must be valid
```

### Issue: Cannot login
**Cause**: Wrong credentials or account doesn't exist  
**Solution**:
```bash
# Double-check username and password
# Check if account exists
# Try registering new account

# If test user created, try:
# Username: testuser
# Password: TestPass123
```

### Issue: "User not found" after registration
**Cause**: Registration didn't complete  
**Solution**:
```bash
# Check terminal for errors
# Verify database was initialized
# Try registering again

# Or reinitialize database:
python init_db.py
```

---

## 6️⃣ ML Model Issues

### Issue: "Could not load ML model" error
**Cause**: best_model.pkl not found  
**Solution**:
```bash
# Train the model
python model.py

# This creates:
# - best_model.pkl
# - scaler.pkl

# Then restart app
python run.py
```

### Issue: Model training fails
**Cause**: Missing dependencies or data file  
**Solution**:
```bash
# Ensure spg.csv exists in project folder
# Reinstall sklearn dependencies
pip install scikit-learn pandas numpy --upgrade

# Then try again
python model.py
```

### Issue: Predictions not working
**Cause**: Invalid input or model error  
**Solution**:
```bash
# Check input values are numbers
# Check value ranges:
# - Temperature: -50 to 60
# - Wind speed: 0 to 50
# - Sky cover: 0 to 1
# - All values should be numeric

# Check terminal for error messages
```

---

## 7️⃣ File & Path Issues

### Issue: "File not found" error
**Cause**: Wrong working directory  
**Solution**:
```bash
# Ensure you're in correct folder
cd "SOLAR ENEGY PREDICTION\SOLAR ENEGY PREDICTION"

# Check files exist
ls  # Linux/Mac
dir  # Windows

# Should see: app_new.py, model.py, spg.csv, etc.
```

### Issue: "templates" folder not found
**Cause**: Missing templates directory  
**Solution**:
```bash
# Check if templates folder exists
# It should be created automatically
# If not, create it:
mkdir templates

# Ensure all HTML files are there
ls templates/
```

### Issue: "static" folder not found
**Cause**: Missing static assets  
**Solution**:
```bash
# Create folders if missing:
mkdir static
mkdir static/css
mkdir static/js

# Ensure files are there:
ls static/css/
ls static/js/
```

---

## 8️⃣ Browser-Specific Issues

### Chrome Issues
- Clear cache: Settings > Privacy > Clear browsing data
- Disable extensions: Try in incognito mode
- Check console: F12 > Console tab

### Firefox Issues
- Clear cache: Menu > Settings > Privacy > Clear Data
- Disable extensions: Add-ons > Extensions
- Check console: F12 > Inspector tab

### Safari Issues
- Clear cache: Develop > Empty Web Storage
- Check console: Develop > Web Inspector
- Update to latest version

### Edge Issues
- Clear cache: Settings > Privacy > Clear browsing data
- Check console: F12 > Console tab

---

## 9️⃣ Environment Issues

### Issue: "SECRET_KEY not configured"
**Cause**: Development vs production mode  
**Solution**:
```bash
# For development, it's auto-generated
# For production, create .env file:

# Copy template
cp .env.example .env

# Edit .env and set:
SECRET_KEY=your-very-secure-random-key-here
```

### Issue: "Debug mode on in production"
**Cause**: Security risk  
**Solution**:
```bash
# In config.py or run.py, ensure:
# DEBUG = False  (for production)
# DEBUG = True   (only for development)
```

### Issue: Database path issues
**Cause**: Wrong database URI  
**Solution**:
```bash
# Check config.py has:
SQLALCHEMY_DATABASE_URI = 'sqlite:///solar_energy.db'

# Not an absolute path, keep it relative
```

---

## 🔟 Performance Issues

### Issue: App is slow
**Cause**: Debug mode, large dataset, or inefficient queries  
**Solution**:
```bash
# Turn off debug mode (production)
# Add database indexes
# Limit query results
# Use pagination
```

### Issue: Memory usage high
**Cause**: Large predictions loaded in memory  
**Solution**:
```bash
# Implement pagination on history page
# Add query limits
# Use lazy loading

# Check in code and optimize queries
```

### Issue: Page takes long to load
**Cause**: Large dataset or slow server  
**Solution**:
```bash
# Optimize database queries
# Add database indexes
# Use caching
# Reduce animations (for slow devices)
```

---

## 💫 Getting Help

### Check These First:
1. ✅ Read error message carefully
2. ✅ Check terminal output
3. ✅ Look in console (F12)
4. ✅ Review logs if available
5. ✅ Check file paths are correct

### Debugging Steps:
1. Stop the app (Ctrl+C)
2. Check for error messages
3. Verify files exist
4. Check dependencies installed
5. Restart app
6. Try in different browser
7. Clear cache
8. Restart computer (if all else fails)

### Common Commands:

```bash
# Check Python version
python --version

# List installed packages
pip list

# Check if Flask installed
pip show flask

# Update pip
python -m pip install --upgrade pip

# Install all dependencies fresh
pip install -r requirements.txt --force-reinstall

# Check Python syntax
python -m py_compile app_new.py

# Run app with verbose output
python -u run.py
```

---

## 📋 Debug Checklist

- [ ] Python version 3.8+?
- [ ] All dependencies installed?
- [ ] In correct folder?
- [ ] templates/ folder exists?
- [ ] static/ folder exists?
- [ ] Database initialized?
- [ ] ML model trained?
- [ ] Port 5000 available?
- [ ] No syntax errors?
- [ ] Browser cache cleared?

---

## 🎯 Quick Fix Steps

For most issues, try this sequence:

1. **Stop app**: Ctrl+C
2. **Clear cache**: Ctrl+Shift+R
3. **Delete database**: rm solar_energy.db
4. **Reinitialize**: python init_db.py
5. **Restart**: python run.py
6. **Refresh browser**: Ctrl+F5

**This solves 90% of issues!**

---

## ⚠️ If Nothing Works:

1. Copy error message exactly
2. Check folder structure is correct
3. Reinstall Python
4. Delete virtual environment, create new one
5. Reinstall all dependencies
6. Review README.md and QUICKSTART.md again

---

## 📞 Still Stuck?

- Check file paths again
- Verify folder structure
- Read error message word by word
- Try on different browser
- Try on different computer
- Review project documentation

---

**Good Luck! 🚀**

*Most issues are solved by restarting or clearing cache.*
