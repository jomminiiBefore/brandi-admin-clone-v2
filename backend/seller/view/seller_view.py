from flask import request, Blueprint, jsonify, g

from seller.service.seller_service import SellerService
from connection import DatabaseConnection
from utils import login_required

from flask_request_validator import (
    PATH,
    JSON,
    Param,
    validate_params
)

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

    @seller_app.route('/<int:parameter_account_no>', methods=['PUT'], endpoint='change_password')
    @login_required
    @validate_params(
        Param('parameter_account_no', PATH, int),
        Param('original_password', JSON, str, required=False),
        Param('new_password', JSON, str),
    )
    def change_password(*args):
        """ 계정 비밀번호 변경 엔드포인트

        계정이 가진 권한에 따라 지정된 인자를 받아 비밀번호를 변경합니다.
        url 에 비밀번호를 바꿔야할 계정 번호를 받습니다.
        Args:
            * args:
                parameter_account_no: 비밀번호가 바뀌어야할 계정 번호

        g.account_info: 데코레이터에서 넘겨받은 계정 정보
            auth_type_id: 계정의 권한정보
            account_no: 데코레이터에서 확인된 계정번호

        request.body: request로 전달 받은 정보
            original_password: 기존 비밀번호(마스터는 안보내줌)
            new_password: 새로운 비밀번호

        Returns: http 응답코드
            200: SUCCESS 비밀번호 변경 완료
            400: VALIDATION_ERROR, INVALID_AUTH_TYPE_ID, NO_ORIGINAL_PASSWORD
            401: INVALID_PASSWORD
            500: DB_CURSOR_ERROR, SERVER_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr): 초기 생성
            2020-04-02 (leejm3@brandi.co.kr): 파라미터 validation 추가, 데코레이터 적용
        """

        # validation 확인이 된 data 를 account_info 로 재정의
        account_info = {
            'parameter_account_no': args[0],
            'original_password': args[1],
            'new_password': args[2],
            'auth_type_id': g.account_info['auth_type_id'],
            'account_no': g.account_info['account_no'],

        }

        # 셀러 권한일 때 original_password 가 없으면 에러반환
        if account_info['auth_type_id'] == 2:
            if account_info['original_password'] is None:
                return jsonify({"message": "NO_ORIGINAL_PASSWORD"}), 400

        db_connection = DatabaseConnection()
        if db_connection:
            try:
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

    @seller_app.route('/<int:parameter_account_no>/info', methods=['GET'], endpoint='get_seller_info')
    @login_required
    @validate_params(
        Param('parameter_account_no', PATH, int),
     )
    def get_seller_info(*args):

        """ 계정 셀러정보 표출 엔드포인트

        셀러정보를 표출하는 엔드포인트 입니다.
        url 로 셀러정보를 확인하고 싶은 계정 번호를 받습니다.

        Args:
            * args:
                parameter_account_no: 불러 올 셀러정보의 계정 번호
        
        g.account_info: 데코레이터에서 넘겨받은 계정 정보
            auth_type_id: 계정의 권한정보
            account_no: 데코레이터에서 확인된 계정번호

        Returns: http 응답코드
            # 200: SUCCESS 비밀번호 변경 완료
            # 400: INVALID_KEY
            # 400: VALIDATION_ERROR, INVALID_AUTH_TYPE_ID
            # 401: INVALID_PASSWORD
            # 500: SERVER ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-01 (leejm3@brandi.co.kr): 초기 생성
            2020-04-02 (leejm3@brandi.co.kr): 파라미터 validation 추가, 데코레이터 적용
        """

        # validation 확인이 된 data 를 account_info 로 재정의
        account_info = {
            'parameter_account_no': args[0],
            'auth_type_id': g.account_info['auth_type_id'],
            'decorator_account_no': g.account_info['account_no'],
        }

        db_connection = DatabaseConnection()
        if db_connection:
            try:
                seller_service = SellerService()

                getting_seller_info_result = seller_service.get_seller_info(account_info, db_connection)

                # 셀러정보가 존재하면 리턴
                if getting_seller_info_result:
                    return getting_seller_info_result

                # 셀러정보가 None 으로 들어오면 INVALID_ACCOUNT_NO 리턴
                else:
                    return jsonify({'message': 'INVALID_ACCOUNT_NO'}), 400

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()
                except Exception as e:
                    return jsonify({'message': f'{e}'}), 400

        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400
