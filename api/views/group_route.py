#!/usr/bin/env python3
"""
Module supplies routes to group resources
"""
from . import db
from flask import Blueprint, request, jsonify
from models.user import User
from models.group import Group
from flask_jwt_extended import jwt_required, get_jwt_identity

group_bp = Blueprint('group_bp', __name__)


@group_bp.route('/api/groups', methods=['GET'], strict_slashes=False)
@jwt_required()
def group_details():
    """
    returns all groups
    """
    groups = Group.query.all()
    groups_data = [group.todict() for group in groups]
    return jsonify(groups_data), 200