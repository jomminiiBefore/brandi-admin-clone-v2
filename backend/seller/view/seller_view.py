from flask import request, Blueprint, jsonify, g

from seller.service.seller_service import SellerService
from connection import DatabaseConnection
from utils import login_required


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

        db_connection = DatabaseConnection()
        if db_connection:
            try:
                seller_service = SellerService()
                new_seller_result = seller_service.create_new_seller(request, db_connection)

                return new_seller_result

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()
                except Exception as e:
                    return jsonify({'message' : f'{e}'}), 400
        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400

    @seller_app.route('', methods=['GET'])
    @login_required
    def get_all_sellers():
        """ 가입된 모든 셀러 표출 엔드포인트

        Returns:
            200: 가입된 모든 셀러 및 셀러 세부 정보 표출

        Authors:
            yoonhc@barndi.co.kr (윤희철)

        History:
            2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
        """

        db_connection = DatabaseConnection()
        if db_connection:
            try:
                seller_service = SellerService()
                sellers = seller_service.get_all_sellers(request, db_connection)

                return sellers

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()
                except Exception as e:
                    return jsonify({'message': f'{e}'}), 400
        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400

    # @login_decorator
    @seller_app.route('/<int:account_no>', methods=['PUT'])
    def change_password(account_no):
        """ 계정 비밀번호 변경 엔드포인트

        계정이 가진 권한에 따라 지정된 인자를 받아 비밀번호를 변경합니다.
        url 에 비밀번호를 바꿔야할 계정 번호를 받습니다.

        Parameters:
            account_no: 비밀번호가 바뀌어야할 계정 번호

        Request.body:
            auth_type_id: 계정의 권한정보
            account_no: 데코레이터에서 확인된 계정번호(데코레이더 생성되면 주석 제외_
            original_password: 기존 비밀번호(마스터는 안보내줌)
            new_password: 새로운 비밀번호

        Returns: http 응답코드
            200: SUCCESS 비밀번호 변경 완료
            400: INVALID_KEY
            400: INVALID_AUTH_TYPE_ID
            401: INVALID_PASSWORD
            500: SERVER ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr): 초기 생성
        """

        db_connection = DatabaseConnection()
        if db_connection:
            try:
                # 데코레이터가 만들어지면, 데코레이터에서 account 정보 받아올 예정
                account_info = request.json
                account_info['parameter_account_no'] = account_no

                seller_service = SellerService()

                changing_password_result = seller_service.change_password(account_info, db_connection)
                return changing_password_result

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()
                except Exception as e:
                    return jsonify({'message': f'{e}'}), 400

        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400
