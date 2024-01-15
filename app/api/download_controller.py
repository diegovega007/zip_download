from flask import Blueprint, request, jsonify

from ..domain.download_domain import zip_domain

zip_controller = Blueprint('zip_controller', __name__)
domain = zip_domain

@zip_controller.route('/zip', methods=['POST'])
def zip():
    data = request.get_json()
    ids = data.get('ids', [])
    if not ids:
        return jsonify({'message': 'No ids provided'}), 400
    try:
        zip_file = domain.zip(ids)
        return zip_file
    except Exception as e:
        return jsonify({'message': str(e)}), 500


