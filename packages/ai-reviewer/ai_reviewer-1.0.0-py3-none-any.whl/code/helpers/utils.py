import subprocess
import sqlite3
import pickle
import time
import logging

CACHE_DB = 'cache.db'

def init_cache_db():
    """Initialize the SQLite database for caching."""
    with sqlite3.connect(CACHE_DB) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS cache (
                key TEXT PRIMARY KEY,
                data BLOB,
                timestamp REAL
            )
        ''')

def cache_data(key, data):
    """Cache data in SQLite."""
    with sqlite3.connect(CACHE_DB) as conn:
        conn.execute('REPLACE INTO cache (key, data, timestamp) VALUES (?, ?, ?)', 
                     (key, pickle.dumps(data), time.time()))

def fetch_from_cache(key):
    """Retrieve data from the cache."""
    with sqlite3.connect(CACHE_DB) as conn:
        result = conn.execute('SELECT data, timestamp FROM cache WHERE key = ?', (key,)).fetchone()
    return result

def fetch_github_data(command):
    """Fetch data using Git command and log the action."""
    logging.info(f"Executing command: {' '.join(command)}")
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        logging.error(f"Git Command Error: {result.stderr}")
        raise Exception(f"Git Command Error: {result.stderr}")
    return result.stdout
