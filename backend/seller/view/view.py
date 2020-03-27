from flask import request, jsonify
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)

        return JSONEncoder.default(self, obj)


class SellerView:
    def create_endpoints(app, services):

        app.json_encoder = CustomJSONEncoder
        seller_service = services.seller_service

        @app.route("/ping", methods=['GET'])
        def ping():
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
            print(new_seller)
            print(new_seller_result)

            return new_seller_result
#            return jsonify({'message': 'SUCCESS'}, 200)
