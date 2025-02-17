#!/usr/bin/python3
"""
Index view for the API
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Returns the status of the API
    Returns:
        A JSON response with the status
    """
    return jsonify({"status": "OK"})
