from flask import send_file, jsonify
import requests
import zipfile
from io import BytesIO

from ...config import config

class download_repository:

    @staticmethod
    def zip(ids):
        try:
            alfresco_url = config['ALFRESCO_BASE_URL']
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
                for document_id in ids:
                    response = requests.get(f"{alfresco_url}/documentos/{document_id}")
                    if response.status_code == 200:
                        document = response.json()
                        zip_file.writestr(document['nombre'], requests.get(document['url']).content)
                    else:
                        return False
            zip_buffer.seek(0)
            return send_file(zip_buffer, as_attachment=True, download_name='archivos.zip')
        except Exception as e:
            return jsonify({'message': str(e)}), 500