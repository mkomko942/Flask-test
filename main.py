from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models, routes

if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')
