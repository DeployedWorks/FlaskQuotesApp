from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/quotesdb"
app.config['DATABASE_URL'] = "postgres://tvlnsrzhhjnnez:8295018134fb2db410293ca005206608b86740f19ca9850187f986c9a10c2f42@ec2-18-211-41-246.compute-1.amazonaws.com:5432/d7vk7o6sm8g87d"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes

if __name__ == '__main__':
    app.run(debug=True)