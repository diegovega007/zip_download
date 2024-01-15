from flask import jsonify

from ..repository.download_repository import download_repository

class zip_domain:
    def __init__(self):
        self.download_repository = download_repository

    def zip(self, ids):
        zip_file = self.download_repository.zip(ids)
        if not zip_file:
            return jsonify({'message': 'No files found'}), 404
        return zip_file
        