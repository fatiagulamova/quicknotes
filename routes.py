from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
import db as database

notes_bp = Blueprint("notes", __name__)


@notes_bp.route("/")
def index():
    notes = database.get_all_notes()
    return render_template("index.html", notes=notes)


@notes_bp.route("/notes/new", methods=["GET", "POST"])
def new_note():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()

        errors = []
        if not title:
            errors.append("Title is required.")
        if not content:
            errors.append("Content is required.")

        if errors:
            for err in errors:
                flash(err, "danger")
            return render_template("note_form.html", title=title, content=content)

        database.create_note(title, content)
        flash("Note created successfully!", "success")
        return redirect(url_for("notes.index"))

    return render_template("note_form.html", title="", content="")


@notes_bp.route("/notes/<int:note_id>")
def view_note(note_id):
    note = database.get_note_by_id(note_id)
    if note is None:
        abort(404)
    return render_template("note_detail.html", note=note)


@notes_bp.route("/notes/<int:note_id>/delete", methods=["POST"])
def delete_note(note_id):
    affected = database.delete_note(note_id)
    if affected == 0:
        abort(404)
    flash("Note deleted.", "info")
    return redirect(url_for("notes.index"))
