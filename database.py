import mysql.connector
from config import DATABASE_CONFIG

def connect_db():
    return mysql.connector.connect(**DATABASE_CONFIG)

def create_table():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email_text TEXT,
        is_phishing BOOLEAN,
        prediction BOOLEAN
    )
    """)
    db.commit()
    db.close()

def insert_email(email_text, is_phishing, prediction):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
    INSERT INTO emails (email_text, is_phishing, prediction)
    VALUES (%s, %s, %s)
    """, (email_text, is_phishing, prediction))
    db.commit()
    db.close()
