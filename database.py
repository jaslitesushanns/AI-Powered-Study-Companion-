import sqlite3
from datetime import datetime

DB_NAME = "students.db"


def get_connection():
    """Create database connection"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_database():
    """Create all required tables"""

    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # USERS TABLE
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        class_name TEXT,
        board TEXT,
        school TEXT,
        created_at TEXT
    )
    """)

    # ==========================
    # STUDENT PROFILE
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_profile(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        goal TEXT,
        study_hours INTEGER,
        preferred_time TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ==========================
    # SUBJECTS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject_name TEXT,
        weak_subject INTEGER DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()
      # ==========================
    # EXAM PORTIONS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exam_portions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject TEXT,
        chapters TEXT,
        exam_date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ==========================
    # STUDY PLANS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_plans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject TEXT,
        planner TEXT,
        created_at TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ==========================
    # QUIZ HISTORY
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quiz_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject TEXT,
        topic TEXT,
        score INTEGER,
        percentage REAL,
        difficulty TEXT,
        attempted_on TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ==========================
    # FLASHCARDS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcards(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        subject TEXT,
        topic TEXT,
        question TEXT,
        answer TEXT,
        created_at TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)
      # ==========================
    # AI CHAT HISTORY
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question TEXT,
        answer TEXT,
        asked_on TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ==========================
    # LEARNING JOURNEY
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS learning_journey(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        current_stage TEXT DEFAULT 'Beginner',
        progress INTEGER DEFAULT 0,
        study_streak INTEGER DEFAULT 0,
        last_updated TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ==========================
    # NOTIFICATIONS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        message TEXT,
        is_read INTEGER DEFAULT 0,
        created_at TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ==========================
    # LOGIN SESSIONS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_sessions(
        session_id TEXT PRIMARY KEY,
        user_id INTEGER,
        created_at TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    # ==========================
    # USER SETTINGS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_settings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        theme TEXT DEFAULT 'Light',
        notifications INTEGER DEFAULT 1,
        music INTEGER DEFAULT 1,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()
  
