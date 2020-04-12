import bcrypt
import jwt
from flask import jsonify, g
from datetime import datetime, timedelta
from config import SECRET
from connection import DatabaseConnection, get_s3_connection

from seller.model.seller_dao import SellerDao


class SellerService:

    """ 셀러 서비스

    Authors:
        leesh3@brandi.co.kr (이소헌)
    History:
        2020-03-25 (leesh3@brandi.co.kr): 초기 생성

    """

    # noinspection PyMethodMayBeStatic
    def change_password(self, change_info, db_connection):

        """ 계정 비밀번호 변경

        change_info에 담긴 권한 정보를 확인하고,
        마스터 권한일 경우
        -> 비밀번호를 바로 변경해주며,
        셀러 권한일 경우
        -> 데코레이터에서 확인된 account_no 와 파라미터로 받은 account_no 가 일치하는지 확인하고,
        비밀번호 변경

        Args:
            change_info: 엔드포인트에서 전달 받은 account 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 비밀번호 변경 완료
            400: INVALID_AUTH_TYPE_ID, INVALID_PARAMETER_ACCOUNT_NO
            401: INVALID_PASSWORD
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr) : 초기 생성
            2020-04-01 (leejm3@brandi.co.kr) :
                - 셀러의 경우 decorator account_no 와 parameter account_no이 일치하는 조건 추가
            2020-04-12 (leejm3@brandi.co.kr):
                - 'INVALID_PARAMETER_ACCOUNT_NO' 에러 추가
                - 받는 인자 명칭을 명확히 하기 위해 변경(account_info -> change_info)
                - parameter validator 를 사용하기 전에 들어온 값을 확인하기 위해 만들었던 new_change_info 를 제거
        """

        seller_dao = SellerDao()
        try:
            # 계정이 가진 권한 타입을 가져옴
            account_auth_type_id = change_info['auth_type_id']

            # 마스터 권한일 때
            if account_auth_type_id == 1:

                # 인자로 전달 받은 새로운 비밀번호를 암호화 시킨 후 디코드 시켜 'password' 로 저장
                crypted_password = bcrypt.hashpw(change_info['new_password'].encode('utf-8'), bcrypt.gensalt())
                change_info['password'] = crypted_password.decode('utf-8')

                # 새로운 비밀번호를 담아서 seller_dao 의 비밀번호 변경 dao 를 호출 및 반환
                changing_password_result = seller_dao.change_password(change_info, db_connection)
                return changing_password_result

            # 셀러 권한일 때
            elif account_auth_type_id == 2:

                if change_info['decorator_account_no'] == change_info['parameter_account_no']:
                    # DB 에서 기존에 저장되어있는 암호화된 비밀번호를 가져옴
                    original_password = seller_dao.get_account_password(change_info, db_connection)

                    # DB 에서 가져온 기존 비밀번호와 셀러가 입력한 기존 비밀번호가 일치하는지 확인
                    if bcrypt.checkpw(change_info['original_password'].encode('utf-8'),
                                      original_password['password'].encode('utf-8')):

                        # 일치하는지 확인되면 새로운 비밀번호를 암호화해서 change_info 에 저장해줌
                        crypted_password = bcrypt.hashpw(change_info['new_password'].encode('utf-8'), bcrypt.gensalt())
                        change_info['password'] = crypted_password.decode('utf-8')

                        # 새로운 비밀번호를 담아서 seller_dao 의 비밀번호 변경 dao 를 호출 및 반환
                        changing_password_result = seller_dao.change_password(change_info, db_connection)
                        return changing_password_result

                    # 기존 비밀번호와 일치하지 않을 경우
                    return jsonify({'message': 'INVALID_PASSWORD'}), 401

                # decorator_account_no 와 parameter_account_no 가 다를 경우 비밀번호 변경 권한이 없음
                else:
                    return jsonify({'message': 'NO_AUTHORIZATION'}), 403

            # 존재하지 않는 auth_type_id
            else:
                return jsonify({'message': 'INVALID_AUTH_TYPE_ID'}), 400

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

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
            200: SUCCESS 셀러정보
            400: INVALID_AUTH_TYPE_ID
            403: NO_AUTHORIZATION
            500: DB_CURSOR_ERROR, INVALID_KEY

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

                # decorator_account_no 와 parameter_account_no 가 다를 경우 셀러정보 열람 권한이 없음
                else:
                    return jsonify({'message': 'NO_AUTHORIZATION'}), 403

            # 존재하지 않는 auth_type_id
            else:
                return jsonify({'message': 'INVALID_AUTH_TYPE_ID'}), 400

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

    # noinspection PyMethodMayBeStatic
    def change_seller_info(self, account_info, db_connection):

        """ 계정 셀러정보 수정 로직(새로운 셀러정보 이력 생성)

        account_info 에 담긴 권한 정보를 확인하고,
        마스터 권한일 경우
        -> 바로 parameter_account_no 의 셀러 정보를 수정해주며,
        셀러 권한일 경우
        -> 데코레이터에서 확인된 수정 진행자의 account_no 와 파라미터로 받은 수정될 셀러의 account_no 가 일치하는지 확인하고,
        parameter_account_no 의 셀러정보를 수정해줍니다.

        Args:
            account_info: 엔드포인트에서 전달 받은 account 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 셀러정보 수정(새로운 이력 생성) 완료
            400: INVALID_APP_ID (존재하지 않는 브랜디 앱 아이디 입력)
            400: INVALID_AUTH_TYPE_ID
            403: NO_AUTHORIZATION
            500: INVALID_KEY, DB_CURSOR_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-03 (leejm3@brandi.co.kr) : 초기 생성

        """

        seller_dao = SellerDao()
        try:
            # 계정이 가진 권한 타입을 가져옴
            account_auth_type_id = account_info['auth_type_id']

            # 마스터 권한일 때
            if account_auth_type_id == 1:

                # parameter_account_no 의 셀러정보를 수정함(새로운 이력 생성)
                changing_seller_info_result = seller_dao.change_seller_info(account_info, db_connection)
                return changing_seller_info_result

            # 셀러 권한일 때
            elif account_auth_type_id == 2:

                # decorator_account_no 와 parameter_account_no 가 동일한지 확인
                if account_info['decorator_account_no'] == account_info['parameter_account_no']:

                    # parameter_account_no 의 셀러정보를 수정함(새로운 이력 생성)
                    changing_seller_info_result = seller_dao.change_seller_info(account_info, db_connection)
                    return changing_seller_info_result

                # decorator_account_no 와 parameter_account_no 가 다를 경우 셀러정보 수정 권한이 없음
                else:
                    return jsonify({'message': 'NO_AUTHORIZATION'}), 403

            # 존재하지 않는 auth_type_id
            else:
                return jsonify({'message': 'INVALID_AUTH_TYPE_ID'}), 400

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

    # noinspection PyMethodMayBeStatic
    def get_seller_list(self, request, user, db_connection):

        """ 가입된 모든 셀러 정보 리스트 표출
        Args:
            request: 클라이언트에서 온 요청
            user: 유저 정보
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            seller_list_result: 셀러 정보 리스트
            403: auth_type_id가 1(마스터)이 아니면 열람 권한 없음

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-03 (yoonhc@brandi.co.kr): 초기 생성

        """

        seller_dao = SellerDao()
        auth_type_id = user.get('auth_type_id', None)

        # 마스터 유저이면 dao에 db_connection 전달
        if auth_type_id == 1:
            seller_list_result = seller_dao.get_seller_list(request, db_connection)
            return seller_list_result

        return jsonify({'message': 'AUTHORIZATION_REQUIRED'}), 403

    def change_seller_status(self, valid_param, user, db_connection):

        """ 마스터 권한 셀러 상태 변경
            Args:
                valid_param: 유효성검사를 통과한 parameter
                user: 유저 정보
                db_connection: 데이터베이스 커넥션 객체

            Returns:
                200: 수정 성공
                400: value값이 정확하게 안들어 온 경우
                403: 마스터 권한이 아닌 경우 수정 권한 없음

            Authors:
                yoonhc@brandi.co.kr (윤희철)

            History:
                2020-04-03 (yoonhc@brandi.co.kr): 초기 생성
                2020-04-05 (yoonhc@brandi.co.kr): 마스터권한 확인 방식 변경

        """
        seller_dao = SellerDao()
        auth_type_id = user.get('auth_type_id', None)

        # 마스터 유저이면 dao에 db_connection 전달
        if auth_type_id == 1:
            seller_status_id = valid_param.get('seller_status_id', None)
            seller_account_id = valid_param.get('seller_account_id', None)

            # 셀러 상태 번호와 셀러 계정 번호가 둘다 들어오지 않으면 400 리턴
            if not seller_status_id or not seller_account_id:
                return jsonify({'message': 'INVALID_VALUE'}), 400

            seller_list_result = seller_dao.change_seller_status(seller_status_id, seller_account_id, db_connection)
            return seller_list_result

        return jsonify({'message': 'AUTHORIZATION_REQUIRED'}), 403

    # noinspection PyMethodMayBeStatic
    def get_seller_name_list(self, keyword, db_connection):

        """ 마스터 권한으로 상품 등록시 셀러를 검색

        마스터 권한으로 접속하여 상품을 등록할 경우,
        셀러를 한글 이름으로 검색하여 선택할 수 있음

        Args:
            keyword(string): 한글 이름 검색어
            db_connection(DatabaseConnection): 데이터베이스 커넥션 객체

        Returns:
            200: 검색된 셀러 10개
            403: 마스터 권한이 없음

         Authors:

            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-04 (leesh3@brandi.co.kr): 초기 생성

        """
        seller_dao = SellerDao()

        if g.account_info['auth_type_id'] == 1:
            seller_name_list_result = seller_dao.get_seller_name_list(keyword, db_connection)
            return seller_name_list_result

        return jsonify({'message': 'AUTHORIZATION_REQUIRED'}), 403

    # noinspection PyMethodMayBeStatic
    def login(self, account_info, db_connection):

        """ 로그인 로직 처리

        유효성 검사를 통과한 로그인 정보를 view 에서 받아와 DAO 에 전달하고
        DAO 에서 받은 return 값에 따라 로직을 처리
        - true: password 가 맞는지 확인 및 jwt 로 토큰 발급
        - false: return invalid login id

        Args:
            account_info: 유효성 검사를 통과한 account 정보 (login_id, password)
            db_connection: 연결된 database connection 객체

        Returns:
            200: SUCCESS 로그인 성공
            400: INVALID_LOGIN_ID
            401: INVALID_PASSWORD

        Authors:
            choiyj@brandi.co.kr (최예지)

        History:
            2020-04-05 (choiyj@brandi.co.kr): 초기 생성
            2020-04-05 (choiyj@brandi.co.kr): 로그인 로직을 처리하는 함수 작성, login_id 존재여부에 따라 token 발행 함수 구현
        """

        # SellerDao 에서 가져온 정보를 담는 seller_dao 인스턴스 생성
        seller_dao = SellerDao()
        try:
            # seller_dao 에 있는 get_account_info 함수로 account_info 와 db_connection 을 인자로 넘겨줌
            account_info_result = seller_dao.get_account_info(account_info, db_connection)

            # 만약 DB 에 login_id 가 존재하면
            if account_info_result:

                # bcrypt.checkpw 를 통해 암호화 된 password 와 인자로 받아 온 password 를 비교
                if bcrypt.checkpw(account_info['password'].encode('utf-8'),
                                  account_info_result['password'].encode('utf-8')):

                    # 두 password 가 일치하면 token 을 발급하는데 현재시간 + 3일 만큼 유효하도록 지정해 줌
                    token = jwt.encode({'account_no': account_info_result['account_no'],
                                        'exp': datetime.utcnow() + timedelta(days=3)},
                                       SECRET['secret_key'], algorithm=SECRET['algorithm'])

                    # 발급 된 token 을 return
                    return jsonify({'token': token}), 200

                else:
                    # 만약 두 password 가 불일치하면 에러 메세지 return
                    return jsonify({'message': 'INVALID_PASSWORD'}), 401

            else:
                # DB에 login_id 가 존재하지 않으면 에러 메세지 return
                return jsonify({'message': 'INVALID_LOGIN_ID'}), 400

        # 명시하지 않은 모든 에러를 잡아서 return
        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

    # noinspection PyMethodMayBeStatic
    def sign_up(self, account_info, db_connection):
        """ 회원가입 로직 처리

        유효성 검사를 통과한 입력 정보를 account_info 로 받고,
        login_id, name_kr, name_en 에 대한 중복 체크 진행

        중복 체크를 통과하면 bcrypt로 암호화된 비밀번호를 생성하고,
        생성된 비밀번호를 account_info 에 넣어 회원가입 dao 를 실행

        Args:
            account_info: 유효성 검사를 통과한 account 정보 (login_id, password)
                login_id 로그인 아이디
                password 비밀번호
                contact_number 담당자 번호
                seller_type_id 셀러 속성 아이디
                name_kr 셀러명
                name_en 셀러 영문명
                center_number 고객센터 번호
                site_url 사이트 URL
                kakao_id 카카오 아이디
                insta_id 인스타 아이디
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 셀러 회원가입 완료
            400: EXISTING_LOGIN_ID, EXISTING_NAME_KR,
                 EXISTING_NAME_EN, INVALID_KEY
            500: NO_DATABASE_CONNECTION

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-06 (leejm3@brandi.co.kr): 초기 생성

        """

        seller_dao = SellerDao()
        try:
            # login_id 중복 체크
            check_overlap_login_id_result = seller_dao. \
                check_overlap_login_id(account_info['login_id'], db_connection)

            if check_overlap_login_id_result:
                return jsonify({'message': 'EXISTING_LOGIN_ID'}), 400

            # name_kr 중복 체크
            check_overlap_name_kr_result = seller_dao. \
                check_overlap_name_kr(account_info['name_kr'], db_connection)

            if check_overlap_name_kr_result:
                return jsonify({'message': 'EXISTING_NAME_KR'}), 400

            # name_en 중복 체크
            check_overlap_name_en_result = seller_dao. \
                check_overlap_name_en(account_info['name_en'], db_connection)

            if check_overlap_name_en_result:
                return jsonify({'message': 'EXISTING_NAME_EN'}), 400

            # 중복체크까지 모두 끝나면 암호화된 비밀번호 생성
            bcrypted_password = bcrypt.hashpw(account_info['password'].encode('utf-8'), bcrypt.gensalt())
            account_info['password'] = bcrypted_password

            # 회원가입 절차 진행
            sign_up_result = seller_dao.sign_up(account_info, db_connection)
            return sign_up_result

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

    # noinspection PyMethodMayBeStatic
    def get_my_page(self, account_info, db_connection):

        """ 계정 셀러정보 표출(my_page)

        데코레이터의 계정번호에 맞는 셀러정보를 표출해줍니다.

        Args:
            account_info: 엔드포인트에서 전달 받은 account 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 셀러정보
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-08 (leejm3@brandi.co.kr) : 초기 생성

        """

        seller_dao = SellerDao()
        try:
            getting_seller_info_result = seller_dao.get_seller_info(account_info, db_connection)
            return getting_seller_info_result

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400
