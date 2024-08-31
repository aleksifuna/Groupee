#!/usr/bin/env python3
"""
Module supplies routes to status check resources
"""
from flask import Blueprint, request, jsonify
status_bp = Blueprint('status_bp', __name__)


@status_bp.route('/status', methods=['GET'], strict_slashes=False)
def system_status():
    """
    Check system status
    """
    return jsonify({
        "Status": "Ok"
    }), 200
