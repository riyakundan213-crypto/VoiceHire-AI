# db.py
import sqlite3
DB = "voicehire.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            field TEXT,
            question TEXT,
            transcript TEXT,
            score REAL,
            breakdown TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_interview(name, field, question, transcript, score, breakdown):
    import json
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO interviews (name, field, question, transcript, score, breakdown)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, field, question, transcript, score, json.dumps(breakdown)))
    conn.commit()
    conn.close()

