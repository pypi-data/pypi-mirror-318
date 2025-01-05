from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Wallet Model
class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(64), unique=True, nullable=False)
    private_key = db.Column(db.Text, nullable=False)
    public_key = db.Column(db.Text, nullable=False)
    balance = db.Column(db.Float, default=0.0)
