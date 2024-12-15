from flask import jsonify, request
from app import db
from app.models import Lead
from app.api import bp

@bp.route('/leads', methods=['POST'])
def create_lead():
    data = request.get_json()
    
    lead = Lead(
        name=data['name'],
        mobile=data['mobile'],
        email=data.get('email'),
        vehicle_type=data['vehicleType'],
        state=data['state'],
        service_type=data['serviceType'],
        comments=data.get('comments')
    )
    
    db.session.add(lead)
    db.session.commit()
    
    return jsonify(lead.to_dict()), 201

@bp.route('/leads', methods=['GET'])
def get_leads():
    leads = Lead.query.order_by(Lead.created_at.desc()).all()
    return jsonify([lead.to_dict() for lead in leads])