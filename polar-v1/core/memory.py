import sqlite3
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'polar.db'
DB_FILE = ROOT_DIR / DB_NAME

def connect() -> sqlite3.Connection:
    return sqlite3.connect(DB_FILE)

def table() -> None:
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                prompt TEXT NOT NULL,
                response TEXT NOT NULL
            )
        ''')
        conn.commit()

def insert_interaction(prompt: str, response: str) -> None:
    now = datetime.now()
    date = now.strftime('%d-%m-%Y')
    time = now.strftime('%H:%M:%S')

    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO interactions (date, time, prompt, response)
            VALUES (?, ?, ?, ?)
        ''', (date, time, prompt, response))
        conn.commit()

def get_all_interactions() -> None:
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT date, time, prompt, response FROM interactions ORDER BY id ASC')
        interactions = cursor.fetchall()

        if interactions:
            print('[P.O.L.A.R.] Interaction history:')
            for i, (date, time, prompt, response) in enumerate(interactions, 1):
                print(f'\nInteraction {i}:')
                print(f'🕒 {date} at {time}')
                print(f'🧠 You: {prompt}')
                print(f'🤖 AI: {response}')
        else:
            print('[P.O.L.A.R.] No interactions recorded.')

def clear_memory() -> None:
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM interactions')
        conn.commit()
        print('[P.O.L.A.R.] All interaction history has been cleared.')