from flask import Flask

from flask_cors import CORS
from flask.json import JSONEncoder

from config import S3_CONFIG
from seller.model.seller_dao import SellerDao
from seller.service.seller_service import SellerService
from seller.view.seller_view import SellerView


class CustomJSONEncoder(JSONEncoder):

    """
    set 자료형을 list 자료형으로 변환하여 JSONEencoding을 가능하게 함.
    """
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


class Services:
    pass


def make_config(app):
    app.config['AWS_ACCESS_KEY_ID'] = S3_CONFIG['AWS_ACCESS_KEY_ID']
    app.config['AWS_SECRET_ACCESS_KEY'] = S3_CONFIG['AWS_SECRET_ACCESS_KEY']
    app.config['S3_BUCKET_NAME'] = S3_CONFIG['S3_BUCKET_NAME']
    app.config['DEBUG'] = True
    return




def create_app():
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder
    make_config(app)
    CORS(app)

    # Model
    seller_dao = SellerDao()

    # Service
    services = Services
    services.seller_service = SellerService(seller_dao)

    # Endpoint
    SellerView.create_endpoints(app, services)


    return app


