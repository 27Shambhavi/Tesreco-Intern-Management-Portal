from flask import Flask, render_template, request, jsonify, redirect
import sqlite3

from database import DB_NAME, ensure_database
from models.intern import Intern
from utils.decorator import log_execution
from utils.exception import InvalidEmailError, InvalidDurationError
from utils.logger import logger

try:
    from utils.file_handler import add_record
except ImportError:
    def add_record(*args, **kwargs):
        pass

app = Flask(__name__)
app.secret_key = "tesreco-intern-management"
ensure_database()


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=["GET", "POST"])
@log_execution
def register():

    if request.method == "GET":
        return "Register API is working. Please send a POST request."

    data = request.get_json()

    name = data["name"]
    email = data["email"]
    domain = data["domain"]
    duration = data.get("duration", 6)

    if "@" not in email:
        raise InvalidEmailError("Invalid Email")

    if duration < 1 or duration > 12:
        raise InvalidDurationError("Duration should be between 1 and 12 months")

    intern = Intern(None, name, email, domain, duration)

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO interns(name,email,domain) VALUES(?,?,?)",
        (
            intern.get_name(),
            intern.get_email(),
            intern.get_domain()
        )
    )

    conn.commit()
    intern_id = cursor.lastrowid
    conn.close()

    add_record(
        intern_id,
        intern.get_name(),
        intern.get_email(),
        intern.get_domain(),
        intern.get_duration()
    )

    logger.info(f"Intern Registered: {intern.get_name()}")

    return jsonify({"message": "Intern Registered Successfully"})


@app.route("/interns", methods=["GET"])
@log_execution
def view_interns():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT interns.id, interns.name, interns.email, interns.domain,
               mentors.name AS mentor_name
        FROM interns
        LEFT JOIN mentors ON interns.mentor_id = mentors.mentor_id
        ORDER BY interns.id DESC
        """
    )

    interns = cursor.fetchall()
    conn.close()

    intern_list = []

    for intern in interns:
        intern_list.append({
            "id": intern["id"],
            "name": intern["name"],
            "email": intern["email"],
            "domain": intern["domain"],
            "mentor": intern["mentor_name"] or "Not Assigned Yet"
        })

    return jsonify(intern_list)


@app.route("/intern/<int:id>", methods=["PUT"])
def update_intern(id):

    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE interns
        SET name=?, email=?, domain=?
        WHERE id=?
        """,
        (
            data["name"],
            data["email"],
            data["domain"],
            id
        )
    )

    conn.commit()
    conn.close()

    logger.info(f"Intern Updated: {id}")

    return jsonify({"message": "Intern Updated Successfully"})


@app.route("/intern/<int:id>", methods=["DELETE"])
def delete_intern(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM interns WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    logger.info(f"Intern Deleted: {id}")

    return jsonify({"message": "Intern Deleted Successfully"})


@app.route("/attendance", methods=["POST"])
def mark_attendance():

    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO attendance(intern_id,date,status)
        VALUES(?,?,?)
        """,
        (
            data["intern_id"],
            data["date"],
            data["status"]
        )
    )

    conn.commit()
    conn.close()

    logger.info("Attendance Recorded")

    return jsonify({"message": "Attendance Marked Successfully"})


@app.route("/add-intern", methods=["GET", "POST"])
def add_intern():

    if request.method == "GET":
        return render_template("add_intern.html")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO interns(name,email,domain)
        VALUES(?,?,?)
        """,
        (
            request.form["name"],
            request.form["email"],
            request.form["domain"]
        )
    )

    conn.commit()
    conn.close()

    return redirect("/view-interns")


@app.route("/view-interns")
def view_interns_page():

    conn = get_db_connection()
    cursor = conn.cursor()

    # LEFT JOIN keeps interns visible even when no mentor has been assigned yet.
    cursor.execute(
        """
        SELECT interns.id, interns.name, interns.email, interns.domain,
               mentors.name AS mentor_name
        FROM interns
        LEFT JOIN mentors ON interns.mentor_id = mentors.mentor_id
        ORDER BY interns.id DESC
        """
    )

    interns = cursor.fetchall()
    conn.close()

    return render_template("view_interns.html", interns=interns)


@app.route("/delete-intern/<int:id>")
def delete_intern_page(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM interns WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/view-interns")


@app.route("/edit-intern/<int:id>", methods=["GET", "POST"])
def edit_intern(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "GET":

        cursor.execute(
            "SELECT * FROM interns WHERE id=?",
            (id,)
        )

        intern = cursor.fetchone()
        conn.close()

        return render_template(
            "edit_intern.html",
            intern=intern
        )

    cursor.execute(
        """
        UPDATE interns
        SET name=?, email=?, domain=?
        WHERE id=?
        """,
        (
            request.form["name"],
            request.form["email"],
            request.form["domain"],
            id
        )
    )

    conn.commit()
    conn.close()

    return redirect("/view-interns")


@app.route("/add-mentor", methods=["GET", "POST"])
def add_mentor():

    if request.method == "GET":
        return render_template("add_mentor.html")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO mentors(name,specialization,experience,email,phone)
        VALUES(?,?,?,?,?)
        """,
        (
            request.form["name"],
            request.form["specialization"],
            request.form["experience"],
            request.form["email"],
            request.form["phone"]
        )
    )

    conn.commit()
    conn.close()

    logger.info(f"Mentor Added: {request.form['name']}")

    return redirect("/view-mentors")


@app.route("/view-mentors")
def view_mentors():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT mentor_id, name, specialization, experience, email, phone
        FROM mentors
        ORDER BY mentor_id DESC
        """
    )

    mentors = cursor.fetchall()
    conn.close()

    return render_template("view_mentors.html", mentors=mentors)


@app.route("/edit-mentor/<int:mentor_id>", methods=["GET", "POST"])
def edit_mentor(mentor_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute(
            "SELECT * FROM mentors WHERE mentor_id=?",
            (mentor_id,)
        )

        mentor = cursor.fetchone()
        conn.close()

        return render_template("edit_mentor.html", mentor=mentor)

    cursor.execute(
        """
        UPDATE mentors
        SET name=?, specialization=?, experience=?, email=?, phone=?
        WHERE mentor_id=?
        """,
        (
            request.form["name"],
            request.form["specialization"],
            request.form["experience"],
            request.form["email"],
            request.form["phone"],
            mentor_id
        )
    )

    conn.commit()
    conn.close()

    logger.info(f"Mentor Updated: {mentor_id}")

    return redirect("/view-mentors")


@app.route("/delete-mentor/<int:mentor_id>")
def delete_mentor(mentor_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    # Keep intern records valid before deleting an assigned mentor.
    cursor.execute(
        "UPDATE interns SET mentor_id=NULL WHERE mentor_id=?",
        (mentor_id,)
    )

    cursor.execute(
        "DELETE FROM mentor_assignment WHERE mentor_id=?",
        (mentor_id,)
    )

    cursor.execute(
        "DELETE FROM mentors WHERE mentor_id=?",
        (mentor_id,)
    )

    conn.commit()
    conn.close()

    logger.info(f"Mentor Deleted: {mentor_id}")

    return redirect("/view-mentors")


@app.route("/assign-mentor", methods=["GET", "POST"])
def assign_mentor():

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute("SELECT id, name, domain FROM interns ORDER BY name")
        interns = cursor.fetchall()

        cursor.execute(
            "SELECT mentor_id, name, specialization FROM mentors ORDER BY name"
        )
        mentors = cursor.fetchall()

        conn.close()

        return render_template(
            "assign_mentor.html",
            interns=interns,
            mentors=mentors
        )

    data = request.get_json(silent=True)

    if data:
        intern_id = data["intern_id"]
        mentor_id = data["mentor_id"]
    else:
        intern_id = request.form["intern_id"]
        mentor_id = request.form["mentor_id"]

    cursor.execute(
        """
        UPDATE interns
        SET mentor_id=?
        WHERE id=?
        """,
        (mentor_id, intern_id)
    )

    conn.commit()
    conn.close()

    logger.info("Mentor Assigned")

    if data:
        return jsonify({"message": "Mentor Assigned Successfully"})

    return redirect("/view-interns")


if __name__ == "__main__":
    app.run(debug=True)
