import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional

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
                response TEXT,
                command TEXT
            )
        ''')
        conn.commit()

def insert_interaction(prompt: str, response: str, command: Optional[str]) -> None:
    now = datetime.now()
    date = now.strftime('%d-%m-%Y')
    time = now.strftime('%H:%M:%S')

    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO interactions (date, time, prompt, response, command)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, time, prompt, response, command))
        conn.commit()

def get_interactions(limit: Optional[int] = None) -> None:
    with connect() as conn:
        cursor = conn.cursor()
        if limit is None:
            cursor.execute('SELECT id, date, time, prompt, response, command FROM interactions ORDER BY id ASC')
        else:
            cursor.execute('SELECT id, date, time, prompt, response, command FROM interactions ORDER BY id DESC LIMIT ?', (limit,))
        interactions = cursor.fetchall()
        interactions = interactions[::-1]

        if interactions:
            print('[P.O.L.A.R.] Interaction history:')
            for (id, date, time, prompt, response, command) in interactions:
                print(f'\nInteraction {id}:')
                print(f'🕒 {date} at {time}')
                print(f'🧠 You: {prompt}')
                print(f'🤖 AI: {response}')
                print(f'📟 Command: {command}')
        else:
            print('[P.O.L.A.R.] No interactions recorded.')

def clear_memory() -> None:
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM interactions')
        conn.commit()
        print('[P.O.L.A.R.] All interaction history has been cleared.')