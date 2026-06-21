from flask import Flask, render_template, request, jsonify, redirect
import sqlite3

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

    conn = sqlite3.connect("interns.db")
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

    conn = sqlite3.connect("interns.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interns")

    interns = cursor.fetchall()

    conn.close()

    intern_list = []

    for intern in interns:

        intern_list.append({
            "id": intern[0],
            "name": intern[1],
            "email": intern[2],
            "domain": intern[3]
        })

    return jsonify(intern_list)


@app.route("/intern/<int:id>", methods=["PUT"])
def update_intern(id):

    data = request.get_json()

    conn = sqlite3.connect("interns.db")
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

    conn = sqlite3.connect("interns.db")
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

    conn = sqlite3.connect("interns.db")
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


@app.route("/assign-mentor", methods=["POST"])
def assign_mentor():

    data = request.get_json()

    conn = sqlite3.connect("interns.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO mentors(name,specialization)
        VALUES(?,?)
        """,
        (
            data["mentor_name"],
            data["specialization"]
        )
    )

    mentor_id = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO mentor_assignment(intern_id,mentor_id)
        VALUES(?,?)
        """,
        (
            data["intern_id"],
            mentor_id
        )
    )

    conn.commit()
    conn.close()

    logger.info("Mentor Assigned")

    return jsonify({"message": "Mentor Assigned Successfully"})


@app.route("/add-intern", methods=["GET", "POST"])
def add_intern():

    if request.method == "GET":
        return render_template("add_intern.html")

    conn = sqlite3.connect("interns.db")
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

    conn = sqlite3.connect("interns.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interns")

    interns = cursor.fetchall()

    conn.close()

    return render_template("view_interns.html", interns=interns)


@app.route("/delete-intern/<int:id>")
def delete_intern_page(id):

    conn = sqlite3.connect("interns.db")
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

    conn = sqlite3.connect("interns.db")
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


if __name__ == "__main__":
    app.run(debug=True)
