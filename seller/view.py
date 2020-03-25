from flask              import request, jsonify
from module.db_module   import Database
from flask.json         import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return JSONEncoder.default(self, obj)

class SellerView:
    def create_endpoints(app, services):
        
        app.json_encoder    = CustomJSONEncoder
        seller_service      = services.seller_service

        @app.route("/ping", methods = ['GET'])
        def ping():
            return "pong"

        @app.route("/seller", methods = ['POST'])
        def sign_up():
            new_seller  = request.json
            new_seller  = seller_service.create_seller(new_seller)
            
            # db_class    = Database()

            # # TODO 모델로 이동시켜야 합니다.
            # insert_statement    = (
            #     "INSERT INTO brandi.seller(name)"
            #     "VALUES (%s)"
            # )
            # insert_name         = new_data['name']
            # db_class.cursor.execute(insert_statement, insert_name)
            # db_class.commit()
                        
            return jsonify({'messsage' : 'CREATED'}, 200)