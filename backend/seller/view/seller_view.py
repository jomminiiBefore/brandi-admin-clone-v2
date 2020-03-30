from flask import request, jsonify
from connection import get_connection


class SellerView:

    """
    셀러 뷰
    """


    def create_endpoints(app, services):
        seller_service = services.seller_service

        @app.route("/seller", methods=['POST'])
        def sign_up():
            try:
                db_connection = get_connection()

                """ 신규 셀러 회원가입 엔드포인드

                입력된 인자가 신규 셀러로 가입됩니다.

                Returns: http 응답코드
                    200: 신규 셀러 계정 저장 완료
                    400: key error
                    500: server error

                Authors:
                    leesh3@brandi.co.kr (이소헌)

                History:
                    2020-03-25 (leesh3@brandi.co.kr): 초기 생성
                """

                new_seller_result = seller_service.create_new_seller(request, db_connection)
                return new_seller_result

            except Exception as e:
                return jsonify({'message' : f'{e}'}), 400

            finally:
                if db_connection:
                    try:
                        db_connection.close()
                    except Exception as e2:
                        # 프린트 스택트레이스 찍어보기. call stack, 함수가 어떻게 요청되었는지.
                        return jsonify({'message' : f'{e2}'}), 400

        @app.route('/seller', methods=['GET'])
        def get_all_sellers():

            try:
                db_connection = get_connection()

                """ 가입된 모든 셀러 표출

                Return:
                    200: 가입된 모든 셀러 및 셀러 세부 정보 표출

                Authors:
                    yoonhc@brandi.co.kr (윤희철)

                History:
                    2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
                """
                sellers = seller_service.get_all_sellers(request, db_connection)
                return sellers

            except Exception as e:
                return jsonify({'message' : f'{e}'}), 400

            finally:
                if db_connection:

                    try:
                        db_connection.close()
                    except Exception as e2:
                        return jsonify({'message' : f'{e2}'}), 400