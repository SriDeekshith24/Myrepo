from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db
from models.opportunity import Opportunity

opportunity_bp = Blueprint('opportunity', __name__)


def serialize_opportunity(opportunity):
    return {
        'id': opportunity.id,
        'opportunity_name': opportunity.opportunity_name,
        'duration': opportunity.duration,
        'start_date': opportunity.start_date,
        'description': opportunity.description,
        'skills_to_gain': opportunity.skills_to_gain,
        'category': opportunity.category,
        'future_opportunities': opportunity.future_opportunities,
        'maximum_applicants': opportunity.maximum_applicants
    }


# =========================
# GET ALL OPPORTUNITIES
# =========================

@opportunity_bp.route('/', methods=['GET'])
@jwt_required()
def get_opportunities():
    user_id = get_jwt_identity()
    opportunities = Opportunity.query.filter_by(user_id=user_id).all()
    return jsonify([serialize_opportunity(opp) for opp in opportunities]), 200


# =========================
# CREATE OPPORTUNITY
# =========================

@opportunity_bp.route('/', methods=['POST'])
@jwt_required()
def create_opportunity():
    user_id = get_jwt_identity()
    data = request.get_json() or {}

    required_fields = [
        'opportunity_name',
        'duration',
        'start_date',
        'description',
        'skills_to_gain',
        'category',
        'future_opportunities'
    ]

    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'{field} is required'}), 400

    opportunity = Opportunity(
        opportunity_name=data['opportunity_name'],
        duration=data['duration'],
        start_date=data['start_date'],
        description=data['description'],
        skills_to_gain=data['skills_to_gain'],
        category=data['category'],
        future_opportunities=data['future_opportunities'],
        maximum_applicants=data.get('maximum_applicants'),
        user_id=user_id
    )

    db.session.add(opportunity)
    db.session.commit()

    return jsonify({'message': 'Opportunity created successfully'}), 201


# =========================
# GET SINGLE OPPORTUNITY
# =========================

@opportunity_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_single_opportunity(id):
    user_id = get_jwt_identity()
    opportunity = Opportunity.query.filter_by(id=id, user_id=user_id).first()

    if not opportunity:
        return jsonify({'error': 'Opportunity not found'}), 404

    return jsonify(serialize_opportunity(opportunity)), 200


# =========================
# UPDATE OPPORTUNITY
# =========================

@opportunity_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_opportunity(id):
    user_id = get_jwt_identity()
    opportunity = Opportunity.query.filter_by(id=id, user_id=user_id).first()
    if not opportunity:
        return jsonify({'error': 'Opportunity not found'}), 404

    data = request.get_json() or {}
    required_fields = [
        'opportunity_name',
        'duration',
        'start_date',
        'description',
        'skills_to_gain',
        'category',
        'future_opportunities'
    ]

    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'{field} is required'}), 400

    opportunity.opportunity_name = data['opportunity_name']
    opportunity.duration = data['duration']
    opportunity.start_date = data['start_date']
    opportunity.description = data['description']
    opportunity.skills_to_gain = data['skills_to_gain']
    opportunity.category = data['category']
    opportunity.future_opportunities = data['future_opportunities']
    opportunity.maximum_applicants = data.get('maximum_applicants')

    db.session.commit()

    return jsonify({'message': 'Opportunity updated successfully'}), 200


# =========================
# DELETE OPPORTUNITY
# =========================

@opportunity_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_opportunity(id):
    user_id = get_jwt_identity()
    opportunity = Opportunity.query.filter_by(id=id, user_id=user_id).first()
    if not opportunity:
        return jsonify({'error': 'Opportunity not found'}), 404

    db.session.delete(opportunity)
    db.session.commit()

    return jsonify({'message': 'Opportunity deleted successfully'}), 200
