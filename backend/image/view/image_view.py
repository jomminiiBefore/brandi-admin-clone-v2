from flask import request, Blueprint
from image.service.image_service import ImageService


class ImageView:
    image_app = Blueprint('image_app', __name__, url_prefix='/image')

    @image_app.route('/resize', methods=['POST'])
    def upload_resized_image():
        image_service = ImageService()
        image_upload_result = image_service.upload_resized_image(request)
        return image_upload_result

    @image_app.route('', methods = ['POST'])
    def upload_image():
        image_service = ImageService()
        image_upload_result = image_service.upload_image(request)
        return image_upload_result
