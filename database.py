import sqlite3

conn = sqlite3.connect("interns.db")

cursor = conn.cursor()

# ==============================
# Intern Table
# ==============================

cursor.execute("""

CREATE TABLE IF NOT EXISTS interns(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    email TEXT NOT NULL UNIQUE,

    domain TEXT NOT NULL

)

""")

# ==============================
# Attendance Table
# ==============================

cursor.execute("""

CREATE TABLE IF NOT EXISTS attendance(

    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    intern_id INTEGER NOT NULL,

    date TEXT NOT NULL,

    status TEXT NOT NULL,

    FOREIGN KEY(intern_id)
    REFERENCES interns(id)

)

""")

# ==============================
# Mentor Table
# ==============================

cursor.execute("""

CREATE TABLE IF NOT EXISTS mentors(

    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    specialization TEXT NOT NULL

)

""")

# ==============================
# Mentor Assignment
# ==============================

cursor.execute("""

CREATE TABLE IF NOT EXISTS mentor_assignment(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    intern_id INTEGER,

    mentor_id INTEGER,

    FOREIGN KEY(intern_id)
    REFERENCES interns(id),

    FOREIGN KEY(mentor_id)
    REFERENCES mentors(mentor_id)

)

""")

conn.commit()

conn.close()

print("Database Created Successfully")