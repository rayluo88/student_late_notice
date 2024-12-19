import sqlite3
import os

def clear_notifications():
    try:
        # Connect to database
        conn = sqlite3.connect('notifications.db')
        cursor = conn.cursor()
        
        # Delete all records but keep table structure
        cursor.execute('DELETE FROM notifications')
        
        # Commit changes
        conn.commit()
        print("Successfully cleared all records!")
        
    except Exception as e:
        print(f"Error: {e}")
        
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