from flask import Flask
from config import Config
from db import close_db
from routes import notes_bp

app = Flask(__name__)
app.config.from_object(Config)

# Tear down database connection after every request
app.teardown_appcontext(close_db)

# Register blueprints
app.register_blueprint(notes_bp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
