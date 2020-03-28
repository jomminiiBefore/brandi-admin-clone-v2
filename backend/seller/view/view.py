from flask import request
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

        @app.route("/seller", methods=['POST'])
        def sign_up():

            """신규 셀러 회원가입

            입력된 인자가 신규 셀러로 가입됩니다.

            :return:
                200: 신규 셀러 계정 저장 완료
                400: key error
                500: server error

            Authors:
                leesh3@brandi.co.kr (이소헌)

            History:
                2020-03-25 (leesh3@brandi.co.kr): 초기 생성
            """
            new_seller = request.json
            new_seller_result = seller_service.create_new_seller(new_seller)

            return new_seller_result
        
        @app.route('/seller', methods=['GET'])
        def get_all_sellers():

            """가입된 모든 셀러 표출

            :return:
                200: 가입된 모든 셀러 및 셀러 세부 정보 표출

            Authors:
                yoonhc@brandi.co.kr (윤희철)

            History:
                2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
            """
            sellers = seller_service.get_all_sellers()
            return sellers
