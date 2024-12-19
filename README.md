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