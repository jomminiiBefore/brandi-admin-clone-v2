import mysql.connector

from flask import Flask
from flask_cors import CORS
from flask.json import JSONEncoder

from config import DATABASES
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


def get_db_config():

    """
    데이터 베이스 정보
    """
    db_config = {
        'database': DATABASES['database'],
        'user': DATABASES['user'],
        'password': DATABASES['password'],
        'host': DATABASES['host'],
        'port': DATABASES['port'],
    }

    return db_config


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.json_encoder = CustomJSONEncoder

    db_config = get_db_config()
    db_connection = mysql.connector.connect(**db_config)
    CORS(app)

    # Model
    seller_dao = SellerDao(db_connection)

    # Service
    services = Services
    services.seller_service = SellerService(seller_dao)

    # Endpoint
    SellerView.create_endpoints(app, services)

    return app
