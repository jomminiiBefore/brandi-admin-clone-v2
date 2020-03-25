import pymysql

from flask              import Flask
from flask_cors         import CORS

from seller.model       import SellerDao
from seller.service     import SellerService
from seller.view        import SellerView
from module.db_module   import Database

class Services:
    pass

def create_app():
    app = Flask(__name__)

    CORS(app)

    ## Model
    seller_dao  = SellerDao(Database)
    
    ## Service
    services = Services
    services.seller_service = SellerService(SellerDao)

    ## Create endpoints
    SellerView.create_endpoints(app, services)

    return app