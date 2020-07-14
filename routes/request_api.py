import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint

from validate_email import validate_email
REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API





@REQUEST_API.route('/send_file', methods=['POST'])
def send_metadata():
    """Return file metadata
    """

    # if not request.get_json():
    #     abort(400)

    workflow_file = request.files['file']
    data = request.get_json(force=True)
    return jsonify(data), 200

