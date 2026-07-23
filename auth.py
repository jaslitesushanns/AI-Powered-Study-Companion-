import streamlit as st
import sqlite3
import hashlib
import uuid
from datetime import datetime

DB_NAME = "students.db"


# ======================================
# DATABASE CONNECTION
# ======================================

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# ======================================
# PASSWORD HASHING
# ======================================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ======================================
# CREATE SESSION
# ======================================

def create_session(user_id):

    session_id = str(uuid.uuid4())

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO user_sessions(session_id,user_id,created_at)
    VALUES(?,?,?)
    """,(
        session_id,
        user_id,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()

    return session_id


# ======================================
# CHECK SESSION
# ======================================

def get_session(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM user_sessions
    WHERE session_id=?
    """,(session_id,))

    data = cursor.fetchone()

    conn.close()

    return data


# ======================================
# DELETE SESSION
# ======================================

def delete_session(session_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM user_sessions
    WHERE session_id=?
    """,(session_id,))

    conn.commit()

    conn.close()
  # ======================================
# CREATE SESSION TABLE
# ======================================

def create_session_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_sessions(
        session_id TEXT PRIMARY KEY,
        user_id INTEGER,
        created_at TEXT
    )
    """)

    conn.commit()
# ======================================
# CREATE USER TABLE
# ======================================

def create_user_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()

    conn.close()
    conn.close()
  # ======================================
# USER REGISTRATION
# ======================================

def register_user(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    hashed = hash_password(password)

    try:
        cursor.execute("""
        INSERT INTO users(username,password)
        VALUES(?,?)
        """,(
            username,
            hashed
        ))

        conn.commit()
        conn.close()

        return True

    except sqlite3.IntegrityError:

        conn.close()
        return False



# ======================================
# USER LOGIN
# ======================================

def login_user(username,password):

    conn = get_connection()

    cursor = conn.cursor()

    hashed = hash_password(password)


    cursor.execute("""
    SELECT *
    FROM users
    WHERE username=? AND password=?
    """,(
        username,
        hashed
    ))

    user = cursor.fetchone()

    conn.close()


    if user:
        return user

    return None
  
