import uuid
from flask import jsonify, abort, request, Blueprint
import os
from cwlparser import CwlParser
REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API





@REQUEST_API.route('/send_file', methods=['POST'])
def send_metadata():
    """Return file metadata
    """

    if not request.files['file']:
        abort(400)

    cwl_file = request.files['file']
    # save the cwl file
    currentdir = os.getcwd()
    file_loc = os.path.join(currentdir, "temp_inputs", cwl_file.filename)
    cwl_file.save(file_loc)

    # parse the file
    parser = CwlParser(file_loc)

    # set output
    metadata = {'tasks': parser.tasks, 'dependencies': parser.dependencies}

    # clear input
    os.remove(file_loc)

    # TODO: handle error codes
    return jsonify(metadata), 200

