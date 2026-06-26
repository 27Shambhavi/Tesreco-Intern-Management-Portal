import sqlite3

DB_NAME = "interns.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def column_exists(cursor, table_name, column_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    return column_name in [column[1] for column in cursor.fetchall()]


def ensure_database():
    conn = get_connection()
    cursor = conn.cursor()

    # ==============================
    # Intern Table
    # ==============================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interns(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            domain TEXT NOT NULL,
            mentor_id INTEGER,
            FOREIGN KEY(mentor_id) REFERENCES mentors(mentor_id)
        )
    """)

    if not column_exists(cursor, "interns", "mentor_id"):
        cursor.execute("ALTER TABLE interns ADD COLUMN mentor_id INTEGER")

    # ==============================
    # Attendance Table
    # ==============================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance(
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            intern_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY(intern_id) REFERENCES interns(id)
        )
    """)

    # ==============================
    # Mentor Table
    # ==============================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mentors(
            mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            experience INTEGER,
            email TEXT,
            phone TEXT
        )
    """)

    mentor_columns = {
        "experience": "INTEGER",
        "email": "TEXT",
        "phone": "TEXT"
    }

    for column_name, column_type in mentor_columns.items():
        if not column_exists(cursor, "mentors", column_name):
            cursor.execute(
                f"ALTER TABLE mentors ADD COLUMN {column_name} {column_type}"
            )

    # Kept for compatibility with older API data. New mentor assignment uses interns.mentor_id.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mentor_assignment(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            intern_id INTEGER,
            mentor_id INTEGER,
            FOREIGN KEY(intern_id) REFERENCES interns(id),
            FOREIGN KEY(mentor_id) REFERENCES mentors(mentor_id)
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    ensure_database()
    print("Database Created Successfully")
