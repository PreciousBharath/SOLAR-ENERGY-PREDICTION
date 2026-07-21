#!/usr/bin/env python
"""
Solar Energy Prediction System - Application Entry Point
Run this file to start the Flask application
"""

import os
import sys
from app_new import app, db, init_db

if __name__ == '__main__':
    with app.app_context():
        # Initialize database if it doesn't exist
        if not os.path.exists('solar_energy.db'):
            print("Creating database...")
            init_db()
        else:
            print("Database already exists.")
        
        # Create tables
        db.create_all()
        print("✓ Database tables created/verified")
        
        # Print startup information
        print("\n" + "="*60)
        print("  SOLAR ENERGY PREDICTION SYSTEM")
        print("="*60)
        print("✓ Server starting...")
        print("✓ Running on: http://localhost:5000")
        print("✓ Debug mode: Enabled")
        print("✓ Database: solar_energy.db")
        print("="*60 + "\n")
        
        # Run the application
        app.run(debug=True, host='0.0.0.0', port=5000)
