# Student Late Arrival Notification System

A web application to notify teachers about student late arrivals.

## Features and Implementation Status

### Core Features
- [x] Web-based interface for recording late arrivals
- [x] Automatic email notifications to designated recipient
- [x] Notification history tracking
- [x] Real-time form validation

### Detailed Implementation Status

#### Data Management
- [x] SQLite database for notification history
- [x] Recorder name tracking
- [x] Form class recording

#### User Interface
- [x] Clean, responsive Bootstrap design
- [x] Real-time form validation
- [x] Recent notifications display

#### Notification System
- [x] Gmail integration
- [x] HTML formatted emails
- [x] Error handling and logging

## Technical Stack

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: 
  - HTML5
  - Bootstrap 5
  - JavaScript
- **Email**: Gmail SMTP

## Setup Requirements

1. Python Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Gmail Configuration:
   a. Enable 2-Step Verification:
      - Go to Google Account settings
      - Navigate to Security
      - Enable 2-Step Verification

   b. Generate App Password:
      - Go to Google Account settings
      - Navigate to Security
      - Under "2-Step Verification", click on "App passwords"
      - Select "Mail" and your device
      - Copy the generated 16-character password

3. Environment Configuration:
   Create a `.env` file with:
   ```
   SECRET_KEY=your-secret-key-here
   GMAIL_USER=your-gmail@gmail.com
   GMAIL_APP_PASSWORD=your-16-char-app-password
   ```

## Running the Application

1. Run the application:
   ```bash
   python app.py
   ```

2. Access the web interface at `http://localhost:5000`

## Usage Guide

1. Enter your name in the "Recorded by" field
2. Enter student name
3. Enter student's form class
4. Select arrival time
5. Click Send Notification

## Data Privacy and Security
- Local data storage only
- Gmail App Password for secure email sending
- Sensitive data stored in environment variables

## Support and Maintenance
- Regular database backups recommended
- Monitor email logs in email.log
- Check notification logs for any failures

## Important Notes
- Never use regular Gmail password
- Keep App Password secure
- Don't commit .env file to version control
- Regularly check email.log for any issues

## Deployment to PythonAnywhere

### 1. Account Setup
1. Create a free account at PythonAnywhere.com
2. Log in to your dashboard

### 2. Code Deployment
```bash
# Open a Bash console in PythonAnywhere and run:
git clone <your-repository-url>
# OR upload files manually via Files tab
```

### 3. Virtual Environment Setup
```bash
# Create and activate virtual environment
mkvirtualenv --python=/usr/bin/python3.8 myenv
workon myenv

# Install dependencies
cd <your-project-directory>
pip install -r requirements.txt
```

### 4. Web App Configuration
1. Go to Web tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10
5. Set Source code and Working directory:
   ```
   Source code: /home/your_username/your_project_name
   Working directory: /home/your_username/your_project_name
   ```

### 5. Virtual Environment Configuration
In Web tab, under Virtualenv:
```
/home/your_username/.virtualenvs/myenv
```

### 6. WSGI Configuration
Create/edit: `/var/www/username_pythonanywhere_com_wsgi.py`
```python
import sys
import os
from dotenv import load_dotenv

# Add your project directory to the sys.path
path = '/home/your_username/your_project_name'
if path not in sys.path:
    sys.path.append(path)

# Load environment variables
load_dotenv(os.path.join(path, '.env'))

# Import your app
from app import app as application
application.debug = False  # Ensure debug mode is off in production
```

### 7. Environment Variables
Create .env file in your project directory:
```bash
# In PythonAnywhere console
cd ~/your_project_name
nano .env
```

Add to .env:
```
SECRET_KEY=your-secret-key-here
GMAIL_USER=your-gmail@gmail.com
GMAIL_APP_PASSWORD=your-16-char-app-password
```

Set file permissions:
```bash
chmod 600 .env
```

### 8. Static Files Configuration
In Web tab, add:
```
URL: /static/
Directory: /home/your_username/your_project_name/static
```

### 9. Database Setup
```bash
# In PythonAnywhere console
cd ~/your_project_name
python
>>> from app import init_db
>>> init_db()
>>> exit()
```

### 10. Final Steps
1. Click "Reload" in Web tab
2. Visit your app: `https://your_username.pythonanywhere.com`

### Troubleshooting

#### Common Issues
1. **Application Error**:
   - Check error logs in Web tab
   - Verify WSGI file configuration
   - Ensure all paths are correct

2. **Static Files Not Loading**:
   - Verify static files configuration
   - Check file permissions
   - Clear browser cache

3. **Email Issues**:
   - Verify environment variables
   - Check email.log
   - Ensure Gmail App Password is correct

#### Viewing Logs
```bash
# Application errors
tail -f /var/log/username.pythonanywhere.com.error.log

# Access logs
tail -f /var/log/username.pythonanywhere.com.access.log

# Email logs
tail -f /home/username/your_project_name/email.log
```