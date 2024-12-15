from app import db
from datetime import datetime

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    registration_number = db.Column(db.String(20), unique=True, nullable=False)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    user = db.relationship('User', backref='vehicles')
    documents = db.relationship('VehicleDocument', backref='vehicle', lazy='dynamic')
    
    def to_dict(self):
        return {
            'id': self.id,
            'registration_number': self.registration_number,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'user': self.user.to_dict(),
            'documents': [doc.to_dict() for doc in self.documents],
            'created_at': self.created_at.isoformat()
        }