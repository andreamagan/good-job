from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from project.config import ConfigDB, ConfigFlask

# Create app
app = Flask(__name__)

# Config app requirements (backend, database)
app.config.from_object(ConfigFlask)
app.config.from_object(ConfigDB)

# Create database connection
db = SQLAlchemy(app)

# Persists object as json
ma = Marshmallow(app)

# Establish migration path
migrate_dir = ConfigDB.MIGRATION_PATH
migrate = Migrate(app, db, directory=migrate_dir) if migrate_dir != '' else Migrate(app, db)

# Register blueprints
from project.blueprints.user_blueprint import user_blueprint

app.register_blueprint(user_blueprint)
