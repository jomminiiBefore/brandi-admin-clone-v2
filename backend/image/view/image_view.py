from flask import request, Blueprint
from image.service.image_service import ImageService


class ImageView:
    image_app = Blueprint('image_app', __name__, url_prefix='/image')

    @image_app.route('/product', methods=['POST'])
    def upload_product_image():
        image_service = ImageService()
        image_upload_result = image_service.upload_product_image(request)
        return image_upload_result

    @image_app.route('/seller', methods = ['POST'])
    def upload_seller_image():
        image_service = ImageService()
        image_upload_result = image_service.upload_seller_image(request)
        return image_upload_result

    @image_app.route('/event', methods = ['POST'])
    def upload_event_image():
        image_service = ImageService()
        image_upload_result = image_service.upload_event_image(request)
        return image_upload_result



