from flask import request
from connection import DatabaseConnection


class ImageView:

    def create_endpoint(app, services):

        @app.route('/image', methods=['POST'])
        def upload_image():
            db_connection = DatabaseConnection()
            image_upload_result = services.upload_image(request, db_connection)
            return image_upload_result