#!/usr/bin/env python3
"""
Group model
"""

from api.views import db
from uuid import uuid4
from datetime import datetime

class Group(db.Model):
    """
    Defines a group model attributes and properties
    """
    __tablename__ = 'groups'
    id = db.Column(db.String(128), primary_key=True, nullable=False)
    description = db.Column(db.String(100), nullable=True)
    amount = db.Column(db.float, nullable=False)
    vendor_payment_details = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self):
        """
        Class constructor
        """
        self.id = str(uuid4())