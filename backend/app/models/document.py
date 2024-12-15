from app import db
from datetime import datetime

class VehicleDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # fitness, ais140, insurance
    document_number = db.Column(db.String(50))
    issued_date = db.Column(db.Date, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'document_number': self.document_number,
            'issued_date': self.issued_date.isoformat(),
            'expiry_date': self.expiry_date.isoformat(),
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }