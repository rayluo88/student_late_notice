import sqlite3
import os
import shutil
from datetime import datetime

def backup_database():
    try:
        # Create backup filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f'notifications_backup_{timestamp}.db'
        
        # Create backups directory if it doesn't exist
        if not os.path.exists('backups'):
            os.makedirs('backups')
        
        # Full path for backup file
        backup_path = os.path.join('backups', backup_file)
        
        # Copy database file
        shutil.copy2('notifications.db', backup_path)
        
        print(f"Database backed up successfully to: {backup_path}")
        return True
        
    except Exception as e:
        print(f"Backup failed: {e}")
        return False

def clear_notifications():
    try:
        # Perform backup first
        if not backup_database():
            print("Aborting clear operation due to backup failure")
            return
        
        # Connect to database
        conn = sqlite3.connect('notifications.db')
        cursor = conn.cursor()
        
        # Get current record count
        cursor.execute('SELECT COUNT(*) FROM notifications')
        record_count = cursor.fetchone()[0]
        
        # Delete all records but keep table structure
        cursor.execute('DELETE FROM notifications')
        
        # Commit changes
        conn.commit()
        print(f"Successfully cleared {record_count} records!")
        
    except Exception as e:
        print(f"Error during clear operation: {e}")
        
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # Ask for confirmation
    confirm = input("Are you sure you want to clear all records? (yes/no): ")
    if confirm.lower() == 'yes':
        clear_notifications()
    else:
        print("Operation cancelled.") 