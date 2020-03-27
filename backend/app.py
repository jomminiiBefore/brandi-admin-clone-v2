import mysql.connector

from flask import Flask
from flask_cors import CORS

from config import DATABASES
from seller.model import SellerDao
from seller.service import SellerService
from seller.view import SellerView


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
    app.config["DEBUG"] = True

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
