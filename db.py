import mysql.connector
from flask import g
from config import Config


def get_db():
    """Open a database connection for the current request context."""
    if "db" not in g:
        g.db = mysql.connector.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
        )
    return g.db


def close_db(e=None):
    """Close the database connection at the end of the request."""
    db = g.pop("db", None)
    if db is not None and db.is_connected():
        db.close()


# ---------------------------------------------------------------------------
# Note queries
# ---------------------------------------------------------------------------

def get_all_notes():
    cursor = get_db().cursor(dictionary=True)
    cursor.execute("SELECT id, title, content, created_at FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()
    cursor.close()
    return notes


def get_note_by_id(note_id: int):
    cursor = get_db().cursor(dictionary=True)
    cursor.execute(
        "SELECT id, title, content, created_at FROM notes WHERE id = %s",
        (note_id,),
    )
    note = cursor.fetchone()
    cursor.close()
    return note


def create_note(title: str, content: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO notes (title, content) VALUES (%s, %s)",
        (title, content),
    )
    db.commit()
    note_id = cursor.lastrowid
    cursor.close()
    return note_id


def delete_note(note_id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    db.commit()
    affected = cursor.rowcount
    cursor.close()
    return affected
