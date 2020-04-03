import bcrypt
from flask import jsonify

from seller.model.seller_dao import SellerDao


class SellerService:

    """
    셀러 서비스
    """
    def create_new_seller(self, request, db_connection):
        """ 신규 셀러 회원가입

        인력된 인자가 신규 셀러로 가입됨

        Args:
            request: 신규 가입 셀러 정보가 담긴 요청
            db_connection: 데이터 베이스 커넥션 객체

        Returns: http 응답 코드
            200: 신규 셀러 계정 저장 완료
            400: key error
            500: server error

        Authors:
            leesh3@brandi.co.kr (이소헌)
            yoonhc@barndi.co.kr (윤희철)보

        History:
            2020-03-25 (leesh3@brandi.co.kr): 초기 생성
            2020-03-30 (yoonhc@barndi.co.kr): db_connection 인자 추
        """
        seller_dao = SellerDao()
        new_seller = request.json
        new_seller_result = seller_dao.insert_seller(new_seller, db_connection)

        return new_seller_result 

    def get_all_sellers(self, request, db_connection):

        """

        Args:
            request: 회원 조회 GET 요청 및 권한 정보 (authorization)
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 가입된 모든 셀러 정보 표

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
        """
        seller_dao = SellerDao()
        get_all_sellers = seller_dao.select_seller_info(db_connection)

        return get_all_sellers

    # noinspection PyMethodMayBeStatic
    def change_password(self, account_info, db_connection):

        """ 계정 비밀번호 변경

        account_info에 담긴 권한 정보를 확인하고,
        마스터 권한일 경우
        -> 비밀번호를 바로 변경해주며,
        셀러 권한일 경우
        -> 데코레이터에서 확인된 account_no 와 파라미터로 받은 account_no 가 일치하는지 확인하고,
        비밀번호 변경

        Args:
            account_info: 엔드포인트에서 전달 받은 account 정보.
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 비밀번호 변경 완료
            400: INVALID_KEY, INVALID_AUTH_TYPE_ID
            401: INVALID_PASSWORD
            500: DB_CURSOR_ERROR, SERVER_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr) : 초기 생성
            2020-04-01 (leejm3@brandi.co.kr) :
            셀러의 경우 decorator account_no 와 parameter account_no이 일치하는 조건 추가

        """

        seller_dao = SellerDao()
        try:
            # Key 가 모두 들어오는지 확인하기 위해 새로운 dict 에 정보를 담음
            new_account_info = {
                'auth_type_id': account_info.get('auth_type_id', None),
                'decorator_account_no': account_info.get('account_no', None),
                'parameter_account_no': account_info.get('parameter_account_no', None),
                'original_password': account_info.get('original_password', None),
                'new_password': account_info.get('new_password', None)
            }

            # 계정이 가진 권한 타입을 가져옴
            account_auth_type_id = new_account_info['auth_type_id']

            # 마스터 권한일 때
            if account_auth_type_id == 1:

                # 인자로 전달 받은 새로운 비밀번호를 암호화 시킨 후 디코드 시켜 'new_password' 로 저장
                crypted_password = bcrypt.hashpw(new_account_info['new_password'].encode('utf-8'), bcrypt.gensalt())
                new_account_info['new_password'] = crypted_password.decode('utf-8')

                # 새로운 비밀번호를 담아서 seller_dao 의 비밀번호 변경 dao 를 호출 및 반환
                changing_password_result = seller_dao.change_password(new_account_info, db_connection)
                return changing_password_result

            # 셀러 권한일 때
            elif account_auth_type_id == 2:

                if new_account_info['decorator_account_no'] == new_account_info['parameter_account_no']:
                    # DB 에서 기존에 저장되어있는 암호화된 비밀번호를 가져옴
                    original_password = seller_dao.get_account_password(new_account_info, db_connection)

                    # DB 에서 가져온 기존 비밀번호와 셀러가 입력한 기존 비밀번호가 일치하는지 확인
                    if bcrypt.checkpw(new_account_info['original_password'].encode('utf-8'),
                                      original_password['password'].encode('utf-8')):
                        # 일치하는지 확인되면 새로운 비밀번호를 암호화해서 new_account_info 에 저장해줌
                        crypted_password = bcrypt.hashpw(new_account_info['new_password'].encode('utf-8'),
                                                         bcrypt.gensalt())
                        new_account_info['new_password'] = crypted_password.decode('utf-8')

                        # 새로운 비밀번호를 담아서 seller_dao 의 비밀번호 변경 dao 를 호출 및 반환
                        changing_password_result = seller_dao.change_password(new_account_info, db_connection)
                        return changing_password_result

                    # 기존 비밀번호와 일치하지 않을 경우
                    return jsonify({'message': 'INVALID_PASSWORD'}), 401

                # decorator_account_no 와 parameter_account_no 가 다를 경우 비밀번호 변경 권한이 없음
                else:
                    return jsonify({'message': 'NO_AUTHORIZATION'}), 403

            # 존재하지 않는 auth_type_id
            else:
                return jsonify({'message': 'INVALID_AUTH_TYPE_ID'}), 400

        # Key 가 잘못 들어올 경우 None TypeError 가 뜨므로 에러 처리
        except TypeError:
            return jsonify({'message': 'INVALID_KEY'}), 400

    # noinspection PyMethodMayBeStatic
    def get_seller_info(self, account_info, db_connection):

        """ 계정 셀러정보 표출

        account_info 에 담긴 권한 정보를 확인하고,
        마스터 권한일 경우
        -> 바로 parameter_account_no 의 셀러 정보를 표출해주며,
        셀러 권한일 경우
        -> 데코레이터에서 확인된 account_no 와 파라미터로 받은 account_no 가 일치하는지 확인하고,
        parameter_account_no 의 셀러정보를 표출해줍니다.

        Args:
            account_info: 엔드포인트에서 전달 받은 account 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 비밀번호 변경 완료
            400: INVALID_KEY
            400: INVALID_AUTH_TYPE_ID
            401: INVALID_PASSWORD
            500: SERVER ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-01 (leejm3@brandi.co.kr) : 초기 생성

        """

        seller_dao = SellerDao()
        try:
            # 계정이 가진 권한 타입을 가져옴
            account_auth_type_id = account_info['auth_type_id']

            # 마스터 권한일 때
            if account_auth_type_id == 1:

                # parameter_account_no 의 셀러정보를 가져옴
                getting_seller_info_result = seller_dao.get_seller_info(account_info, db_connection)
                return getting_seller_info_result

            # 셀러 권한일 때
            elif account_auth_type_id == 2:

                # decorator_account_no 와 parameter_account_no 가 동일한지 확인
                if account_info['decorator_account_no'] == account_info['parameter_account_no']:

                    # parameter_account_no 의 셀러정보를 가져옴
                    getting_seller_info_result = seller_dao.get_seller_info(account_info, db_connection)
                    return getting_seller_info_result

                # decorator_account_no 와 parameter_account_no 가 다를 경우 비밀번호 변경 권한이 없음
                else:
                    return jsonify({'message': 'NO_AUTHORIZATION'}), 403

            # 존재하지 않는 auth_type_id
            else:
                return jsonify({'message': 'INVALID_AUTH_TYPE_ID'}), 400

        except Exception as e:
            print(e)

    def get_seller_list(self, user, db_connection):

        """ Args:
             user: 유저 정보
             db_connection: 데이터베이스 커넥션 객체

         Returns:
             200: 가입된 모든 셀러 정보 리스트

         Authors:
             yoonhc@brandi.co.kr (윤희철)

         History:
             2020-04-03 (yoonhc@brandi.co.kr): 초기 생성

         """

        seller_dao = SellerDao()

        # 유저 정보에서 권한 정보를 확인
        try:
            with db_connection as db_cursor:
                sql_command = '''
                SELECT
                name 
                FROM 
                authorization_types 
                WHERE 
                auth_type_no = %(auth_type_id)s
                '''
                db_cursor.execute(sql_command, {'auth_type_id' : user['auth_type_id']})
                auth_type_name = db_cursor.fetchone()['name']

                # 마스터 유저이면 dao에 db_connection 전달
                if auth_type_name == '마스터':
                    seller_list_result = seller_dao.get_seller_list(db_connection)
                    return seller_list_result

                return jsonify({'message' : 'AUTHORIZATION_REQUIRED'}), 403

        except Exception as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'message' : 'DB_CURSOR_ERROR'})


