from flask import jsonify, request
from app import db
from app.models.vehicle import Vehicle
from app.models.document import VehicleDocument
from app.api import bp
from app.utils.auth import login_required, admin_required
from datetime import datetime, timedelta

@bp.route('/vehicles', methods=['POST'])
@login_required
def create_vehicle():
    data = request.get_json()
    vehicle = Vehicle(
        user_id=data['user_id'],
        registration_number=data['registration_number'],
        make=data['make'],
        model=data['model'],
        year=data['year']
    )
    
    db.session.add(vehicle)
    db.session.commit()
    
    return jsonify(vehicle.to_dict()), 201

@bp.route('/vehicles/<int:id>/documents', methods=['POST'])
@login_required
def add_document(id):
    data = request.get_json()
    document = VehicleDocument(
        vehicle_id=id,
        type=data['type'],
        document_number=data['document_number'],
        issued_date=datetime.strptime(data['issued_date'], '%Y-%m-%d').date(),
        expiry_date=datetime.strptime(data['expiry_date'], '%Y-%m-%d').date()
    )
    
    db.session.add(document)
    db.session.commit()
    
    return jsonify(document.to_dict()), 201

@bp.route('/vehicles/expiring', methods=['GET'])
@login_required
def get_expiring_documents():
    # Get documents expiring in the next 30 days
    thirty_days = datetime.now().date() + timedelta(days=30)
    
    documents = VehicleDocument.query.filter(
        VehicleDocument.expiry_date <= thirty_days,
        VehicleDocument.status == 'active'
    ).all()
    
    return jsonify([doc.to_dict() for doc in documents])