from datetime import datetime
from models import db


class Opportunity(db.Model):
    __tablename__ = "opportunities"

    id = db.Column(db.Integer, primary_key=True)

    opportunity_name = db.Column(db.String(255), nullable=False)

    duration = db.Column(db.String(100), nullable=False)

    start_date = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text, nullable=False)

    skills_to_gain = db.Column(db.Text, nullable=False)

    category = db.Column(db.String(100), nullable=False)

    future_opportunities = db.Column(db.Text, nullable=False)

    maximum_applicants = db.Column(db.Integer, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)