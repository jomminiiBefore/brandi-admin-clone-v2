from flask import request, jsonify
from flask.json import JSONEncoder

       
class SellerView:
    def create_endpoints(app, services):
        #app.json_encoder = CustomJSONEncoder
        seller_service = services.seller_service


        @app.errorhandler(400)
        def http_400_bad_request(self, KeyError): 
            response = jsonify({'message' : KeyError.description})
            return response


        @app.route("/ping", methods=['GET'])
        def ping(self):
            return "pong"

        @app.route("/seller", methods=['POST'])
        def sign_up():

            """신규 셀러 회원가입

            입력된 인자가 신규 셀러로 가입됩니다.
            :return:
                신규 셀러 생성

            :authors:
                leesh3@brandi.co.kr (이소헌)

            :history:
                2020-03-25 (leesh3@brandi.co.kr): 초기 생성
            """
            new_seller = request.json
            new_seller_result = seller_service.create_new_seller(new_seller)

            return new_seller_result
        
        @app.route('/seller', methods=['GET'])
        def get_all_sellers():
            data = seller_service.get_all_sellers()
            return data
