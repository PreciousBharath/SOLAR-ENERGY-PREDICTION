"""
Database Initialization Helper Script
Run this once to create the database and schema
"""

from app_new import app, db, User, Prediction, ActivityLog
from datetime import datetime

def init_database():
    """Initialize the database with all tables"""
    with app.app_context():
        print("Creating database schema...")
        db.create_all()
        print("✓ Database schema created successfully!")
        
        # Check if tables exist
        tables = [User, Prediction, ActivityLog]
        for table in tables:
            print(f"✓ {table.__tablename__} table created")
        
        print("\n✓ Database initialization complete!")
        print("\nYou can now:")
        print("1. Run 'python run.py' to start the application")
        print("2. Visit http://localhost:5000/register to create an account")

def create_test_user(username="testuser", email="test@example.com", password="TestPass123"):
    """Create a test user for development"""
    with app.app_context():
        if User.query.filter_by(username=username).first():
            print(f"User {username} already exists!")
            return
        
        user = User(
            username=username,
            email=email,
            full_name="Test User",
            company="Test Company"
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        print(f"✓ Test user created:")
        print(f"  Username: {username}")
        print(f"  Email: {email}")
        print(f"  Password: {password}")

if __name__ == "__main__":
    import sys
    
    print("="*60)
    print("  SOLAR ENERGY PREDICTION SYSTEM - DATABASE SETUP")
    print("="*60 + "\n")
    
    # Initialize database
    init_database()
    
    # Ask if user wants to create test user
    print("\nWould you like to create a test user? (y/n): ", end="")
    response = input().strip().lower()
    
    if response == 'y':
        create_test_user()
        print("\n✓ Test user created! You can now log in with:")
        print("  Username: testuser")
        print("  Password: TestPass123")
    
    print("\n" + "="*60)
    print("  Setup complete! Run 'python run.py' to start")
    print("="*60)
