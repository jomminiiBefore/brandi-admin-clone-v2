from flask import request, Blueprint, jsonify
from connection import get_db_connection
from seller.service.seller_service import SellerService


class SellerView:
    """
    셀러 뷰
    """

    seller_app = Blueprint('seller_app', __name__, url_prefix='/seller')

    @seller_app.route("", methods=["POST"])
    def sign_up():

            """ 신규 셀러 회원가입 엔드포인드

            입력된 인자가 신규 셀러로 가입됩니다.

            Returns: http 응답코드
                200: 신규 셀러 계정 저장 완료
                400: key error
                500: server error

            Authors:
                leesh3@brandi.co.kr (이소헌)
                yoonhc@barndi.co.kr (윤희철)

            History:
                2020-03-25 (leesh3@brandi.co.kr): 초기 생성
                2020-03-30 (yoonhc@barndi.co.kr): database connection open & close 추가
            """
            try:
                db_connection = get_db_connection()

                seller_service = SellerService()
                new_seller_result = seller_service.create_new_seller(request, db_connection)
                return new_seller_result

            except Exception as e:
                return jsonify({'message' : f'{e}'}), 400

            finally:
                if db_connection:
                    try:
                        db_connection.close()
                    except Exception as e2:
                        return jsonify({'message' : f'{e2}'}), 400


    @seller_app.route('', methods=['GET'])
    def get_all_sellers():
        """ 가입된 모든 셀러 표출 엔드포인트

        Returns:
            200: 가입된 모든 셀러 및 셀러 세부 정보 표출

        Authors:
            yoonhc@barndi.co.kr (윤희철)

        History:
            2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
        """

        db_connection = get_db_connection()
        if db_connection:
            try:
                seller_service = SellerService()
                sellers = seller_service.get_all_sellers(request, db_connection)

                return sellers

            except Exception as e:
                return jsonify({'message222': f'{e}'}), 400

            finally:
                if db_connection:
                    try:
                        db_connection.close()
                    except Exception as e:
                        return jsonify({'message111': f'{e}'}), 400
        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400
