# QuickNotes

A lightweight note-taking web application built with **Flask** and **MySQL** — designed as a starting point for a university cloud computing course.

## Project Structure

```
quicknotes/
├── app.py              # Flask application entry point
├── config.py           # Configuration (reads from .env)
├── db.py               # Database connection & query helpers
├── routes.py           # URL routes (Blueprint)
├── requirements.txt    # Python dependencies
├── schema.sql          # Database schema
├── .env.example        # Example environment variables
├── static/
│   └── css/
│       └── style.css   # Custom styles
└── templates/
    ├── base.html       # Base layout (Bootstrap 5)
    ├── index.html      # Notes list
    ├── note_form.html  # Create note form
    └── note_detail.html# Note detail view
```

## Prerequisites

- Python 3.10+
- MySQL 8.0+

## Setup Instructions

### 1. Clone / Download the project

```bash
cd quicknotes
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the database

Log in to MySQL and run the schema script:

```bash
mysql -u root -p < schema.sql
```

Or copy-paste the contents of `schema.sql` into MySQL Workbench / DBeaver.

### 5. Configure environment variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env   # macOS/Linux
copy .env.example .env # Windows
```

Edit `.env`:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=quicknotes
SECRET_KEY=replace-with-a-random-string
```

### 6. Run the application

```bash
python app.py
```

Open your browser and navigate to **http://127.0.0.1:5000**.

## Features

| Feature       | Route                    | Method      |
|---------------|--------------------------|-------------|
| List notes    | `/`                      | GET         |
| Create note   | `/notes/new`             | GET / POST  |
| View note     | `/notes/<id>`            | GET         |
| Delete note   | `/notes/<id>/delete`     | POST        |

## Database Schema

```sql
CREATE TABLE notes (
    id         INT UNSIGNED NOT NULL AUTO_INCREMENT,
    title      VARCHAR(255) NOT NULL,
    content    TEXT         NOT NULL,
    created_at DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
```

## Notes for the Course

This project is intentionally containerisation-free. In later labs you will:

1. Add a `Dockerfile` to containerise the Flask app.
2. Add a `docker-compose.yml` to orchestrate Flask + MySQL together.
3. Write Kubernetes manifests (Deployment, Service, ConfigMap, Secret) to deploy to a cluster.
