from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from datetime import datetime
import os
import sqlite3
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key')

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # Fixed for Gmail
SMTP_PORT = 587  # Fixed for Gmail TLS
GMAIL_USER = os.getenv('GMAIL_USER')
GMAIL_APP_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')
RECIPIENT_EMAIL = "huang_lixia@moe.edu.sg"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email.log'),
        logging.StreamHandler()
    ]
)

# Database initialization
def init_db():
    try:
        conn = sqlite3.connect('notifications.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS notifications
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             date TEXT NOT NULL,
             student_name TEXT NOT NULL,
             class TEXT NOT NULL,
             arrival_time TEXT NOT NULL,
             recorder_name TEXT NOT NULL)
        ''')
        conn.commit()
    except Exception as e:
        print(f"Database initialization error: {e}")
        raise
    finally:
        if conn:
            conn.close()

# Initialize database on startup
init_db()

def save_notification(student_name, class_name, arrival_time, recorder_name):
    conn = sqlite3.connect('notifications.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO notifications (date, student_name, class, arrival_time, recorder_name)
        VALUES (?, ?, ?, ?, ?)
    ''', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
          student_name, class_name, arrival_time, recorder_name))
    conn.commit()
    conn.close()

def get_recent_notifications(limit=5):
    conn = sqlite3.connect('notifications.db')
    c = conn.cursor()
    c.execute('''
        SELECT date, student_name, class, arrival_time 
        FROM notifications 
        ORDER BY id DESC 
        LIMIT ?
    ''', (limit,))
    notifications = [
        {
            'date': row[0],
            'student_name': row[1],
            'class': row[2],
            'arrival_time': row[3]
        }
        for row in c.fetchall()
    ]
    conn.close()
    return notifications

def send_email_notification(to_email, subject, message, recorder_name):
    try:
        if not all([GMAIL_USER, GMAIL_APP_PASSWORD]):
            logging.error("Gmail credentials not configured in .env file")
            flash("Email configuration missing. Please check .env file.", "danger")
            return False

        msg = MIMEMultipart()
        msg['From'] = f"{recorder_name} <{GMAIL_USER}>"
        msg['To'] = to_email
        msg['Subject'] = subject

        # Create HTML version of the message
        html = f"""
        <html>
            <body>
                <h2>{subject}</h2>
                <p style="white-space: pre-line">{message}</p>
                <hr>
                <p><small>This is an automated notification from the Student Late Arrival Notification System.</small></p>
            </body>
        </html>
        """
        
        msg.attach(MIMEText(html, 'html'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            try:
                server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
                logging.info(f"Sending notification to {to_email}")
                server.send_message(msg)
                logging.info("Email sent successfully")
                return True
            except smtplib.SMTPAuthenticationError:
                logging.error("Gmail authentication failed. Check App Password")
                flash("Gmail authentication failed. Please verify your App Password.", "danger")
                return False
    except Exception as e:
        logging.error(f"Error sending email: {str(e)}")
        if "please run connect() first" in str(e).lower():
            flash("Network connection error. Please check your internet connection.", "danger")
        elif "authentication failed" in str(e).lower():
            flash("Gmail authentication failed. Please check your credentials.", "danger")
        else:
            flash(f"Error sending email: {str(e)}", "danger")
        return False

@app.route('/', methods=['GET'])
def index():
    recent_notifications = get_recent_notifications()
    return render_template('index.html', 
                         recent_notifications=recent_notifications)

@app.route('/send_notification', methods=['POST'])
def send_notification():
    try:
        recorder_name = request.form.get('recorder_name')
        student_name = request.form.get('student_name')
        class_name = request.form.get('class_name')
        arrival_time = request.form.get('arrival_time')
        
        if not all([recorder_name, student_name, class_name, arrival_time]):
            flash('All fields are required', 'danger')
            return redirect(url_for('index'))

        current_date = datetime.now().strftime('%Y/%m/%d')
        subject = f"Late Notice - {student_name} ({class_name})"
        message = f"""
Dear Ms Huang,

This is to inform you that {student_name} from {class_name} arrived late on {current_date} at {arrival_time}.

Please take necessary action as per school policy.

Best regards,
{recorder_name}
Student Late Arrival Notification System
        """.strip()
        
        if send_email_notification(RECIPIENT_EMAIL, subject, message, recorder_name):
            save_notification(student_name, class_name, arrival_time, recorder_name)
            flash('Notification sent successfully!', 'success')
            logging.info(f"Notification saved and sent for {student_name} by {recorder_name}")
        else:
            save_notification(student_name, class_name, arrival_time, recorder_name)
            flash('Error sending notification. Please check email configuration.', 'danger')
            
    except Exception as e:
        logging.error(f"Error in send_notification: {str(e)}")
        flash(f'An error occurred: {str(e)}', 'danger')
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 