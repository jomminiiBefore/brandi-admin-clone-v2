from flask import Flask, request

from flask_cors import CORS
from flask.json import JSONEncoder

from config import S3_CONFIG
from seller.view.seller_view import SellerView
# from image.view.image_view import ImageView


class CustomJSONEncoder(JSONEncoder):

    """
    set 자료형을 list 자료형으로 변환하여 JSONEencoding을 가능하게 함.
    """
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


def make_config(app):
    app.config['AWS_ACCESS_KEY_ID'] = S3_CONFIG['AWS_ACCESS_KEY_ID']
    app.config['AWS_SECRET_ACCESS_KEY'] = S3_CONFIG['AWS_SECRET_ACCESS_KEY']
    app.config['S3_BUCKET_NAME'] = S3_CONFIG['S3_BUCKET_NAME']
    app.config['DEBUG'] = True
    return


def create_app():
    # set flask object
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder
    make_config(app)
    CORS(app)
    app.register_blueprint(SellerView.seller_app)

    return app


