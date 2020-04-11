import pandas as pd, uuid, os
from flask import jsonify
from datetime import datetime
from mysql.connector.errors import Error

from connection import DatabaseConnection, get_s3_connection


class SellerDao:
    """ 셀러 모델

    Authors:
        leesh3@brandi.co.kr (이소헌)
    History:
        2020-03-25 (leesh3@brandi.co.kr): 초기 생성

    """
    def gen_random_name(self):

        """ 랜덤한 이름 생성

        Args:
            self: 클래스에서 전역으로 쓰임.

        Returns: http 응답코드
            random_name: 랜덤한 이름 리

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-07 (yoonhc@brandi.co.kr): 초기 생성
        """
        random_name = str(uuid.uuid4())
        return random_name

    # noinspection PyMethodMayBeStatic
    def get_account_password(self, account_info, db_connection):

        """ 계정의 암호화된 비밀번호 표출

        비밀번호 변경 시 기존 비밀번호를 제대로 입력했는지 확인하기 위해,
        인자로 받아온 account_info['parameter_account_no'] 의 password 를 표출합니다.

        Args:
            account_info: account 정보
            (parameter_account_no: 비밀번호를 확인할 account_no)
            db_connection: 연결된 database connection 객체

        Returns:
            200: 요청된 계정의 계정번호 및 암호화된 비밀번호
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr): 초기 생성
        """

        try:
            with db_connection.cursor() as db_cursor:

                # SELECT 문에서 확인할 데이터
                account_info_data = {
                    'account_no': account_info['parameter_account_no']
                }

                # accounts 테이블 SELECT
                select_account_password_statement = """
                    SELECT account_no, password 
                    FROM accounts 
                    WHERE account_no = %(account_no)s
                """

                # SELECT 문 실행
                db_cursor.execute(select_account_password_statement, account_info_data)

                # 쿼리로 나온 기존 비밀번호를 가져옴
                original_password = db_cursor.fetchone()
                return original_password

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def change_password(self, account_info, db_connection):

        """ UPDATE 계정 비밀번호 DB

        Args:
            account_info: account 정보
            (parameter_account_no: 비밀번호를 확인할 account_no
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 비밀번호 변경 완료
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr): 초기 생성
        """

        try:
            with db_connection.cursor() as db_cursor:

                # SELECT 문에서 확인할 데이터
                account_info_data = {
                    'account_no': account_info['parameter_account_no'],
                    'password': account_info['new_password'],
                }

                # accounts 테이블 UPDATE
                update_password_statement = """
                    UPDATE 
                    accounts 
                    SET
                    password = %(password)s
                    WHERE
                    account_no = %(account_no)s
                """

                # UPDATE 문 실행
                db_cursor.execute(update_password_statement, account_info_data)

                # 실행 결과 반영
                db_connection.commit()
                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError:
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_seller_info(self, account_info, db_connection):

        """ 계정의 셀러정보 표출

        인자로 받아온 account_info['parameter_account_no'] 의 셀러정보를 표출합니다.

        Args:
            account_info: account 정보
            (parameter_account_no: 셀러정보를 확인할 account_no)
            db_connection: 연결된 database connection 객체

        Returns:
            200: 요청된 계정의 셀러정보
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr): 초기 생성
            2020-04-01 (leejm3@brandi.co.kr): seller_info 기본 정보 표출
            2020-04-02 (leejm3@brandi.co.kr): 외래키 관련 정보 표출
            2020-04-03 (leejm3@brandi.co.kr): 표출 정보에 외래키 id 값 추가
        """
        try:
            with db_connection.cursor() as db_cursor:

                # 셀러 기본 정보(외래키 제외)
                # SELECT 문 조건 데이터
                account_info_data = {
                    'account_no': account_info['parameter_account_no']
                }

                # seller_info 테이블 SELECT (get 기본 정보)
                select_seller_info_statement = """
                    SELECT 
                    seller_info_no,
                    seller_account_id,
                    profile_image_url,
                    c.status_no as seller_status_no,
                    c.name as seller_status_name,
                    d.seller_type_no as seller_type_no,
                    d.name as seller_type_name,
                    e.account_no as account_no,
                    e.login_id as account_login_id,
                    f.app_user_no as brandi_app_user_no,
                    f.app_id as brandi_app_user_app_id,
                    name_kr,
                    name_en,
                    brandi_app_user_id,
                    ceo_name,
                    company_name,
                    business_number,
                    certificate_image_url,
                    online_business_number,
                    online_business_image_url,
                    background_image_url,
                    short_description,
                    long_description,
                    site_url,
                    insta_id,
                    center_number,
                    kakao_id,
                    yellow_id,
                    zip_code,
                    address,
                    detail_address,
                    weekday_start_time,
                    weekday_end_time,
                    weekend_start_time,
                    weekend_end_time,
                    bank_name,
                    bank_holder_name,
                    account_number
                    
                    FROM seller_accounts AS a
                    
                    -- seller_info 기본 정보
                    INNER JOIN seller_infos AS b
                    ON a.seller_account_no = b.seller_account_id
                    
                    -- 셀러 상태명
                    INNER JOIN seller_statuses as c
                    ON b.seller_status_id = c.status_no

                    -- 셀러 속성명
                    INNER JOIN seller_types as d
                    ON b.seller_type_id = d.seller_type_no

                    -- 셀러계정 로그인 아이디
                    LEFT JOIN accounts as e
                    ON e.account_no = a.account_id
                    AND e.is_deleted =0

                    -- 브랜디 앱 아이디
                    LEFT JOIN brandi_app_users as f
                    ON b.brandi_app_user_id = f.app_user_no
                    AND f.is_deleted = 0
                    WHERE a.account_id = %(account_no)s
                    AND a.is_deleted = 0
                    AND b.close_time = '2037-12-31 23:59:59'
                """

                # SELECT 문 실행
                db_cursor.execute(select_seller_info_statement, account_info_data)

                # seller_info_result 에 쿼리 결과 저장
                seller_info_result = db_cursor.fetchone()

                # 담당자 정보
                # SELECT 문 조건 데이터
                seller_info_no_data = {
                    'seller_info_no': seller_info_result['seller_info_no']
                }
                # manager_infos 테이블 SELECT(get *)
                select_manager_infos_statement = """
                                SELECT
                                b.name,
                                b.contact_number,
                                b.email,
                                b.ranking
                                FROM seller_infos AS a
                                INNER JOIN manager_infos AS b
                                ON a.seller_info_no = b.seller_info_id
                                WHERE seller_info_no = %(seller_info_no)s
                                AND b.is_deleted = 0
                                LIMIT 3
                            """

                # SELECT 문 실행
                db_cursor.execute(select_manager_infos_statement, seller_info_no_data)

                # manager_infos 출력 결과 저장
                manager_infos = db_cursor.fetchall()

                # seller_info_result 에 manager_info 저장
                seller_info_result['manager_infos'] = [info for info in manager_infos]

                # 셀러 상태 변경 기록
                # SELECT 문 조건 데이터
                account_info_data = {
                    'seller_account_id': seller_info_result['seller_account_id']
                }

                # seller_status_change_histories 테이블 SELECT
                select_status_history_statement = """
                                SELECT
                                changed_time,
                                c.name as seller_status_name,
                                d.login_id as modifier
                                FROM
                                seller_accounts as a

                                -- 셀러상태이력 기본정보
                                INNER JOIN
                                seller_status_change_histories as b
                                ON a.seller_account_no = b.seller_account_id

                                -- 셀러 상태명
                                INNER JOIN
                                seller_statuses as c
                                ON b.seller_status_id = c.status_no

                                -- 수정자 로그인아이디
                                LEFT JOIN
                                accounts as d
                                ON d.account_no = a.account_id

                                WHERE a.seller_account_no = %(seller_account_id)s
                                AND d.is_deleted = 0
                                ORDER BY changed_time
                            """

                # SELECT 문 실행
                db_cursor.execute(select_status_history_statement, account_info_data)

                # seller_status_change_histories 출력 결과 저장
                status_histories = db_cursor.fetchall()

                # seller_info_result 에 seller_status_change_histories 저장
                seller_info_result['seller_status_change_histories'] = [history for history in status_histories]

                # 셀러 속성 리스트(마스터가 셀러의 속성 변경하는 옵션 제공용)
                # SELECT 문 조건 데이터
                account_info_data = {
                    'seller_info_no': seller_info_result['seller_info_no']
                }

                # seller_types 테이블 SELECT
                select_seller_types_statement = """
                                SELECT
                                c.seller_type_no as seller_type_no,
                                c.name as seller_type_name
                                FROM 
                                product_sorts as a
                                
                                -- 셀러정보
                                INNER JOIN
                                seller_infos as b
                                ON a.product_sort_no = b.product_sort_id
                               
                                -- 상품속성
                                INNER JOIN
                                seller_types as c
                                ON a.product_sort_no = c.product_sort_id

                                WHERE b.seller_info_no = %(seller_info_no)s
                            """

                # SELECT 문 실행
                db_cursor.execute(select_seller_types_statement, account_info_data)

                # seller_types 출력 결과 저장
                seller_types = db_cursor.fetchall()

                # seller_info_result 에 seller_types 저장
                seller_info_result['seller_types'] = seller_types

                # seller_info_result 에 auth_type_id 저장

                seller_info_result['auth_type_id'] = account_info['auth_type_id']
                print(seller_info_result)
                return seller_info_result

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_seller_list(self, request, db_connection):

        """ GET 셀러 리스트를 표출하고, 검색 키워드가 오면 키워드 별 검색 가능.
        페이지네이션 기능: offset과 limit값을 받아서 페이지네이션 구현.
        검색기능: 키워드를 받아서 검색기능 구현. 키워드가 추가 될 때 마다 검색어가 필터에 추가됨.
        엑셀다운로드 기능: excel=1을 쿼리파라미터로 받으면 데이터베이스의 값을
                        엑셀파일로 만들어 s3에 업로드하고 다운로드 링크를 리턴

        Args:
            db_connection: 연결된 database connection 객체
            request: 쿼리파라미터를 가져옴

        Returns: http 응답코드
            200: 키워드로 excel=1이 들어온 경우 s3에 올라간 엑셀파일 다운로드url
            200: 셀러 리스트 표출(검색기능 포함), 키워드에 맞는 셀러 숫자
            500: SERVER ERROR

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-03(yoonhc@brandi.co.kr): 초기 생성
            2020-04-07(yoonhc@brandi.co.kr): 엑셀 다운로드 기능 추가
            2020-04-10(yoonhc@brandi.co.kr): 필터링 키워드가 들어오면 필터된 셀러를 count하고 결과값에 추가하는 기능 작성
        """

        # offset과 limit에 음수가 들어오면  default값 지정
        offset = 0 if int(request.args.get('offset', 0)) < 0 else int(request.args.get('offset', 0))
        limit = 10 if int(request.args.get('limit', 10)) < 0 else int(request.args.get('limit', 10))

        # sql에서 where 조건문에 들어갈 필터 문자열
        filter_query = ''

        # request안의 유효성검사에 딕셔너리인 valid_param에서 value가 None이 아니면 filter_query에 조건 쿼리문을 추가해줌.
        seller_account_no = request.valid_param['seller_account_no']
        if seller_account_no:
            filter_query += f" AND seller_accounts.seller_account_no = {seller_account_no}"

        login_id = request.valid_param['login_id']
        if login_id:
            filter_query += f" AND accounts.login_id = '{login_id}'"

        name_kr = request.valid_param['name_kr']
        if name_kr:
            filter_query += f" AND name_kr = '{name_kr}'"

        name_en = request.valid_param['name_en']
        if name_en:
            filter_query += f" AND name_en = '{name_en}'"

        brandi_app_user_id = request.valid_param['brandi_app_user_id']
        if brandi_app_user_id:
            filter_query += f" AND brandi_app_user_id = {brandi_app_user_id}"

        manager_name = request.valid_param['manager_name']
        if manager_name:
            filter_query += f" AND manager_infos.name = '{manager_name}'"

        seller_status = request.valid_param['seller_status']
        if seller_status:
            filter_query += f" AND seller_statuses.name = '{seller_status}'"

        manager_contact_number = request.valid_param['manager_contact_number']
        if manager_contact_number:
            filter_query += f" AND manager_infos.contact_number LIKE '%{manager_contact_number}%'"

        manager_email = request.valid_param['manager_email']
        if manager_email:
            filter_query += f" AND manager_infos.email = '{manager_email}'"

        seller_type_name = request.valid_param['seller_type_name']
        if seller_type_name:
            filter_query += f" AND seller_types.name = '{seller_type_name}'"

        start_date = request.valid_param['start_time']
        end_date = request.valid_param['close_time']
        if start_date and end_date:
            start_date = str(request.args.get('start_time', None)) + ' 00:00:00'
            end_date = str(request.args.get('close_time', None)) + ' 23:59:59'
            filter_query += f" AND seller_accounts.created_at > '{start_date}' AND seller_accounts.created_at < '{end_date}'"

        try:
            with db_connection as db_cursor:

                # 셀러 리스트를 가져오는 sql 명령문, 쿼리가 들어오면 쿼리문을 포메팅해서 검색 실행
                select_seller_list_statement = f'''
                    SELECT 
                    seller_account_id, 
                    accounts.login_id,
                    name_en,
                    name_kr,
                    brandi_app_user_id,
                    seller_statuses.name as seller_status,
                    seller_status_id,
                    seller_types.name as seller_type_name,
                    site_url,
                    (
                        SELECT COUNT(0) 
                        FROM product_infos 
                        WHERE product_infos.seller_id  = seller_infos.seller_account_id 
                        AND product_infos.close_time = '2037-12-31 23:59:59' 
                    ) as product_count,
                    seller_accounts.created_at,
                    manager_infos.name as manager_name,
                    manager_infos.contact_number as manager_contact_number,
                    manager_infos.email as manager_email
                    FROM seller_infos
                    right JOIN seller_accounts ON seller_accounts.seller_account_no = seller_infos.seller_account_id
                    LEFT JOIN accounts ON seller_accounts.account_id = accounts.account_no
                    LEFT JOIN seller_statuses ON seller_infos.seller_status_id = seller_statuses.status_no
                    LEFT JOIN seller_types ON seller_infos.seller_type_id = seller_types.seller_type_no
                    LEFT JOIN manager_infos on manager_infos.seller_info_id = seller_infos.seller_info_no 
                    WHERE seller_infos.close_time = '2037-12-31 23:59:59.0' 
                    AND manager_infos.ranking = 1{filter_query}
                    LIMIT %(limit)s OFFSET %(offset)s                   
                '''
                parameter = {
                    'limit': limit,
                    'offset': offset,
                }

                # sql 쿼리와 pagination 데이터 바인딩
                db_cursor.execute(select_seller_list_statement, parameter)
                seller_info = db_cursor.fetchall()

                # 쿼리파라미터에 excel키가 1로 들어오면 엑셀파일을 만듦.
                if request.valid_param['excel'] == 1:
                    s3 = get_s3_connection()

                    # pandas 데이터 프레임을 만들기 위한 column과 value 정리
                    seller_list_dict = {
                        '셀러번호': [seller['seller_account_id'] for seller in seller_info],
                        '관리자계정ID': [seller['login_id'] for seller in seller_info],
                        '셀러영문명': [seller['name_en'] for seller in seller_info],
                        '셀러한글명': [seller['name_kr'] for seller in seller_info],
                        '브랜디회원번호': [seller['brandi_app_user_id'] for seller in seller_info],
                        '담당자명': [seller['manager_name'] for seller in seller_info],
                        '담당자전화번호': [seller['manager_contact_number'] for seller in seller_info],
                        '판매구분': [seller['seller_type_name'] for seller in seller_info],
                        '상품개수': [seller['product_count'] for seller in seller_info],
                        '셀러URL': [seller['site_url'] for seller in seller_info],
                        '셀러등록일': [seller['created_at'] for seller in seller_info],
                        '승인여부': [seller['seller_status'] for seller in seller_info]
                    }

                    # 데이터베이스의 데이터를 기반으로 한 딕셔너리를 판다스 데이터 프레임으로 만들어줌.
                    df = pd.DataFrame(data=seller_list_dict)

                    # 파일이름과 파일경로를 정의해줌.
                    file_name = f'{self.gen_random_name()}.xlsx'
                    file = f'../{file_name}'

                    # 파일을 엑셀파일로 변환해서 로컬에 저장
                    df.to_excel(file, encoding='utf8')

                    # 로컬에 저장된 파일을 s3에 업로드
                    s3.upload_file(file, "brandi-intern", file_name)

                    # s3에 올라간 파일을 다운받는 url
                    file_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{file_name}'

                    # s3에 올라간 후에 로컬에 있는 파일 삭제
                    os.remove(file)

                    return jsonify({'file_url': file_url}), 200

                # 셀러 상태를 확인하여 해당 상태에서 취할 수 있는 action을 기존의 seller_info에 넣어줌.
                for seller in seller_info:
                    if seller['seller_status'] == '입점':
                        seller['action'] = ['휴점 신청', '퇴점 신청 처리']
                    elif seller['seller_status'] == '입점대기':
                        seller['action'] = ['입점 승인', '입점 거절']
                    elif seller['seller_status'] == '휴점':
                        seller['action'] = ['휴점 해제', '퇴점 신청 처리']
                    elif seller['seller_status'] == '퇴점대기':
                        seller['action'] = ['휴점 신청', '퇴점 확정 처리', '퇴점 철회 처리']

                # pagination을 위해서 전체 셀러가 몇명인지 count해서 기존의 seller_info에 넣어줌.
                seller_count_statement = '''
                    SELECT 
                    COUNT(seller_account_id) as total_seller_count
                    FROM seller_infos
                    LEFT JOIN seller_accounts ON seller_infos.seller_account_id = seller_accounts.seller_account_no 
                    LEFT JOIN accounts ON seller_accounts.account_id = accounts.account_no 
                    WHERE close_time = '2037-12-31 23:59:59.0' AND accounts.is_deleted = 0
                '''
                db_cursor.execute(seller_count_statement)
                seller_count = db_cursor.fetchone()

                # 쿼리파라미터가 들어오면 필터된 셀러를 카운트하고 리턴 값에 포함시킴.
                if len(filter_query) > 0:
                    filter_query_values_count_statement = f'''
                        SELECT COUNT(0) as filtered_seller_count
                        FROM seller_infos
                        right JOIN seller_accounts ON seller_accounts.seller_account_no = seller_infos.seller_account_id
                        LEFT JOIN accounts ON seller_accounts.account_id = accounts.account_no
                        LEFT JOIN seller_statuses ON seller_infos.seller_status_id = seller_statuses.status_no
                        LEFT JOIN seller_types ON seller_infos.seller_type_id = seller_types.seller_type_no
                        LEFT JOIN manager_infos on manager_infos.seller_info_id = seller_infos.seller_info_no 
                        WHERE seller_infos.close_time = '2037-12-31 23:59:59.0' 
                        AND manager_infos.ranking = 1{filter_query}
                        LIMIT %(limit)s OFFSET %(offset)s
                    '''
                    db_cursor.execute(filter_query_values_count_statement, parameter)
                    filter_query_values_count = db_cursor.fetchone()
                    seller_count['filtered_seller_count'] = filter_query_values_count['filtered_seller_count']

                return jsonify({'seller_list': seller_info, 'seller_count': seller_count}), 200

        # 데이터베이스 error
        except Exception as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'error': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def change_seller_info(self, account_info, db_connection):

        """ 계정 셀러정보를 수정(새로운 이력 생성) INSERT INTO DB

        계정 셀러정보를 수정합니다.
        선분이력 관리를 위해 기존 셀러정보 updated_at(수정일시)와 close_time(종료일시)를 업데이트하고,
        새로운 셀러정보 이력을 생성합니다.
        입력한 브랜디 앱 아이디가 존재하는지 확인하는 절차를 가집니다.

        기존 셀러정보와 새로운 셀러정보, 담당자 정보, 셀러 상태 변경 기록이 모두 정상 저장되어야 프로세스가 완료됩니다.
        기존 셀러정보의 종료일시를 새로운 셀러정보의 시작일시와 맞추기 위해 새로운 셀러정보를 먼저 등록했습니다.

        Args:
            account_info: 엔드포인트에서 전달 받은 account 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: 셀러정보 수정(새로운 이력 생성) 완료
            400: INVALID_APP_ID (존재하지 않는 브랜디 앱 아이디 입력)
            403: NO_AUTHORIZATION_FOR_STATUS_CHANGE
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-03 (leejm3@brandi.co.kr): 초기 생성
            2020-04-04 (leejm3@brandi.co.kr): 기본정보, 담당자정보 수정 저장 확인
            2020-04-05 (leejm3@brandi.co.kr): 에러 처리 추가 확인정
            2020-04-08 (leejm3@brandi.co.kr):
                select now() 사용하여 선분이력 관리하도록 수정
                수정 전 셀러정보 id 값을 불러오는 방식 변경
                - 기존 : request.body로 UI에게 받음
                - 변경 : DB를 조회해서 해당 seller_account_id 의 가장 마지막 셀러정보 id 를 불러옴

        """
        try:
            with db_connection.cursor() as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # list 인 manager_infos 가 SQL 에 들어가면 에러를 반환해 미리 manager_infos 에 저장하고 account_info 에서 삭제
                manager_infos = account_info['manager_infos']
                del account_info['manager_infos']

                # 현재 시간 저장
                db_cursor.execute("""
                    SELECT now()
                """)
                now = db_cursor.fetchone()

                account_info['now'] = now['now()']

                # 이전 셀러정보 아이디 가져오기
                # seller_infos 테이블 SELECT
                select_seller_infos_statement = """
                    SELECT seller_info_no
                    FROM seller_infos
                    WHERE seller_account_id = %(seller_account_id)s
                    AND close_time = '2037-12-31 23:59:59'
                """

                db_cursor.execute(select_seller_infos_statement, account_info)

                previous_seller_info_id = db_cursor.fetchone()

                account_info['previous_seller_info_id'] = previous_seller_info_id['seller_info_no']

                # 브랜디앱유저 검색 정보
                brandi_app_user_data = {
                    'app_id': account_info['brandi_app_user_app_id']
                }

                # brandi_app_users 테이블 SELECT
                select_app_id_statement = """
                    SELECT
                    app_user_no
                    FROM
                    brandi_app_users
                    WHERE app_id = %(app_id)s
                    AND is_deleted = 0
                """

                db_cursor.execute(select_app_id_statement, brandi_app_user_data)

                # app_id 출력 결과 저장
                app_id_result = db_cursor.fetchone()

                # app_id가 있으면 account_info 에 app_user_no 저장
                if app_id_result:
                    account_info['app_user_no'] = app_id_result['app_user_no']

                # app_id가 없으면 app_id가 존재하지 않는다고 리턴
                else:
                    return jsonify({'message': 'INVALID_APP_ID'}), 400

                # 셀러 기본 정보 생성
                # seller_infos 테이블 INSERT INTO
                insert_seller_info_statement = """
                    INSERT INTO seller_infos (
                    seller_account_id,
                    profile_image_url,
                    seller_status_id,
                    seller_type_id,
                    product_sort_id,                 
                    name_kr,
                    name_en,
                    brandi_app_user_id,
                    ceo_name,
                    company_name,
                    business_number,
                    certificate_image_url,
                    online_business_number,
                    online_business_image_url,
                    background_image_url,
                    short_description,
                    long_description,
                    site_url,
                    kakao_id,
                    insta_id,
                    yellow_id,
                    center_number,
                    zip_code,
                    address,
                    detail_address,
                    weekday_start_time,
                    weekday_end_time,
                    weekend_start_time,
                    weekend_end_time,
                    bank_name,
                    bank_holder_name,
                    account_number,
                    modifier,
                    start_time
                ) VALUES (
                    %(seller_account_id)s,
                    %(profile_image_url)s,
                    %(seller_status_no)s,
                    %(seller_type_no)s,
                    (SELECT product_sort_id FROM seller_types WHERE seller_type_no = %(seller_type_no)s),                     
                    %(name_kr)s,
                    %(name_en)s,
                    %(app_user_no)s,                    
                    %(ceo_name)s,
                    %(company_name)s,
                    %(business_number)s,
                    %(certificate_image_url)s,
                    %(online_business_number)s,
                    %(online_business_image_url)s,
                    %(background_image_url)s,
                    %(short_description)s,
                    %(long_description)s,
                    %(site_url)s,
                    %(kakao_id)s,
                    %(insta_id)s,
                    %(yellow_id)s,                    
                    %(center_number)s,
                    %(zip_code)s,
                    %(address)s,
                    %(detail_address)s,
                    %(weekday_start_time)s,
                    %(weekday_end_time)s,
                    %(weekend_start_time)s,
                    %(weekend_end_time)s,
                    %(bank_name)s,
                    %(bank_holder_name)s,
                    %(account_number)s,
                    %(decorator_account_no)s,
                    %(now)s
                )"""

                # 셀러 기본정보 insert 함
                db_cursor.execute(insert_seller_info_statement, account_info)

                # 위에서 생성된 새로운 셀러정보의 id 값을 가져옴
                seller_info_no = db_cursor.lastrowid

                # manager_infos 테이블 INSERT INTO
                insert_manager_info_statement = """
                    INSERT INTO manager_infos (
                    name,
                    contact_number,
                    email,
                    ranking,
                    seller_info_id
                ) VALUES (
                    %(name)s,
                    %(contact_number)s,
                    %(email)s,
                    %(ranking)s,
                    %(seller_info_id)s
                )"""

                # for 문을 돌면서 담당자 정보를 insert 함
                for i in range(len(manager_infos)):
                    manager_info_data = {
                        'name': manager_infos[i]['name'],
                        'contact_number': manager_infos[i]['contact_number'],
                        'email': manager_infos[i]['email'],
                        'ranking': manager_infos[i]['ranking'],
                        'seller_info_id': seller_info_no
                    }

                    db_cursor.execute(insert_manager_info_statement, manager_info_data)

                # 이전 셀러정보 수정일시, 종료일시 업데이트
                # previous_seller_info 테이블 UPDATE
                update_previous_seller_info_statement = """
                    UPDATE seller_infos
                    SET
                    close_time = %(now)s
                    WHERE seller_info_no = %(previous_seller_info_id)s
                """

                db_cursor.execute(update_previous_seller_info_statement, account_info)

                # 이전 셀러정보의 셀러 상태값 가져오기
                select_previous_seller_status_statement = """
                    SELECT seller_status_id
                    FROM seller_infos
                    WHERE seller_info_no = %(previous_seller_info_id)s
                """

                db_cursor.execute(select_previous_seller_status_statement, account_info)

                previous_seller_status_id = db_cursor.fetchone()

                account_info['previous_seller_status_id'] = previous_seller_status_id['seller_status_id']

                # 이전 셀러정보의 셀러 상태값과 새로운 셀러정보의 셀러 상태값이 다르면, 셀러 상태정보이력 테이블 INSERT INTO
                if account_info['previous_seller_status_id'] != account_info['seller_status_no']:

                    # 마스터 권한이 아닐 때 셀러 상태(입점 등)를 변경하려고 하면 에러 리턴
                    if account_info['auth_type_id'] != 1:
                        return jsonify({'message': 'NO_AUTHORIZATION_FOR_STATUS_CHANGE'}), 403

                    # INSERT INTO 문에서 확인할 데이터
                    seller_status_data = {
                        'seller_account_id': account_info['seller_account_id'],
                        'new_seller_info_no': seller_info_no,
                        'seller_status_id': account_info['seller_status_no'],
                        'modifier': account_info['decorator_account_no'],
                        'now': now['now()']
                    }

                    # seller_status_change_histories 테이블 INSERT INTO
                    insert_status_history_statement = """
                        INSERT INTO seller_status_change_histories (
                        seller_account_id,
                        changed_time,
                        seller_status_id,
                        modifier
                    ) VALUES (
                        %(seller_account_id)s,
                        %(now)s,
                        %(seller_status_id)s,
                        %(modifier)s
                    )"""

                    db_cursor.execute(insert_status_history_statement, seller_status_data)

                db_connection.commit()
                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_seller_name_list(self, keyword, db_connection):

        """

        Args:
            keyword(string):
            db_connection(DatabaseConnection):

        Returns:
            200: 검색된 셀러 10개
            400: key error
            500: server error

        Authors:

            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-05 (leesh3@brandi.co.kr): 초기 생성
        """
        try:
            with db_connection.cursor() as db_cursor:
                get_stmt = """
                    SELECT seller_account_id, profile_image_url, name_kr, account_id, product_sort_id
                    FROM seller_infos 
                    INNER JOIN seller_accounts ON seller_accounts.seller_account_no = seller_infos.seller_account_id
                    WHERE seller_infos.name_kr 
                    LIKE '%"""+keyword+"""%' AND close_time='2037-12-31 23:59:59.0'
                """
                db_cursor.execute(get_stmt)

                names = db_cursor.fetchmany(10)

                if names:
                    return jsonify({'search_results': names}), 200
                return jsonify({'message': 'SELLER_DOES_NOT_EXISTS'}), 404

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def change_seller_status(self, seller_status_id, seller_account_id, db_connection):

        """ 마스터 권한 셀러 상태 변경
        마스터 권한을 가진 유저가 데이터베이스의 셀러의 상태를 변경함.
        seller_infos테이블에 새로운 이력(row)를 생성하고 seller_infos의 foreign key룰 가지는
        manager_infos테이블에도 새로운 셀러 정보 이력을 foregin key로 가지도록 row를 추가해줌.

            Args:
                seller_status_id: 셀러 상태 아이디
                seller_account_id: 셀러 정보 아이디
                db_connection: 데이터베이스 커넥션 객체

            Returns:
                200: 셀러 상태 정보 수정 성공
                500: 데이터베이스 error, key error

            Authors:
                yoonhc@brandi.co.kr (윤희철)

            History:
                2020-04-05 (yoonhc@brandi.co.kr): 초기 생성
                2020-04-09 (yoonhc@brandi.co.kr): 셀러정보 선분이력 반영

        """

        # 데이터베이스 커서 실행
        try:
            with db_connection as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")

                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # seller_infos : service에서 넘어온 셀러 데이터
                seller_data = {
                    'seller_status_id': seller_status_id,
                    'seller_account_id': seller_account_id
                }

                # 새로운 이력 생성 이전의 셀러 인포 번호를 가져와서 셀러데이터에 저장
                db_cursor.execute('''
                SELECT seller_info_no
                FROM seller_infos
                WHERE seller_account_id = %(seller_account_id)s
                AND close_time = '2037-12-31 23:59:59'
                ''', seller_data)

                # 새로운 버전 이전의 버전의 셀러 번호를 seller_data에 저장장
                seller_data['previous_seller_info_no'] = db_cursor.fetchone()['seller_info_no']

                # seller_infos : 셀러 상태 변경 sql 명령문
                update_seller_status_statement = """
                    INSERT INTO seller_infos
                    (
                        seller_account_id,
                        profile_image_url,
                        seller_status_id,
                        seller_type_id,
                        product_sort_id,                 
                        name_kr,
                        name_en,
                        brandi_app_user_id,
                        ceo_name,
                        company_name,
                        business_number,
                        certificate_image_url,
                        online_business_number,
                        online_business_image_url,
                        background_image_url,
                        short_description,
                        long_description,
                        site_url,
                        kakao_id,
                        insta_id,
                        yellow_id,
                        center_number,
                        zip_code,
                        address,
                        detail_address,
                        weekday_start_time,
                        weekday_end_time,
                        weekend_start_time,
                        weekend_end_time,
                        bank_name,
                        bank_holder_name,
                        account_number,
                        modifier
                    )
                    SELECT
                        seller_account_id,
                        profile_image_url,
                        %(seller_status_id)s,
                        seller_type_id,
                        product_sort_id,                 
                        name_kr,
                        name_en,
                        brandi_app_user_id,
                        ceo_name,
                        company_name,
                        business_number,
                        certificate_image_url,
                        online_business_number,
                        online_business_image_url,
                        background_image_url,
                        short_description,
                        long_description,
                        site_url,
                        kakao_id,
                        insta_id,
                        yellow_id,
                        center_number,
                        zip_code,
                        address,
                        detail_address,
                        weekday_start_time,
                        weekday_end_time,
                        weekend_start_time,
                        weekend_end_time,
                        bank_name,
                        bank_holder_name,
                        account_number,
                        modifier
                    FROM seller_infos                    
                    WHERE
                    seller_account_id = %(seller_account_id)s AND close_time = '2037-12-31 23:59:59'
                """

                # seller_infos : 데이터 sql명령문과 셀러 데이터 바인딩 후 새로운 셀러 정보 이력의 primary key 딕셔너리에 담음
                db_cursor.execute(update_seller_status_statement, seller_data)
                new_seller_info_id = db_cursor.lastrowid
                seller_data['new_seller_info_id'] = new_seller_info_id

                # 선분이력을 닫아주는 시간을 쿼리로 가져옴. 선분이력을 닫아주는 시간을 seller_data에 저장함.
                db_cursor.execute('SELECT NOW()')
                close_time = db_cursor.fetchone()
                seller_data['close_time'] = close_time['NOW()']

                # seller_infos 테이블에 해당 seller_account의 새로운 이력이 생겼기 때문에 이전의 이력을 끊어주는 작업.
                update_previous_seller_infos_stat = '''
                UPDATE
                seller_infos
                SET
                close_time = %(close_time)s
                WHERE
                seller_info_no = %(previous_seller_info_no)s
                AND seller_account_id = %(seller_account_id)s
                '''
                db_cursor.execute(update_previous_seller_infos_stat, seller_data)

                # manager_infos : 매니저 정보에서 셀러 인포 foreign key를 새로 생성된 이력으로 바꿔는 명령문.
                insert_manager_info_statement = """
                    INSERT INTO manager_infos (
                        name,
                        contact_number,
                        email,
                        ranking,
                        seller_info_id
                    ) 
                    SELECT
                        name,
                        contact_number,
                        email,
                        ranking,
                        %(new_seller_info_id)s
                        FROM manager_infos
                        WHERE manager_info_no = (SELECT manager_info_no FROM manager_infos WHERE seller_info_id = %(previous_seller_info_no)s AND ranking = 1)
                        AND ranking = 1
                """

                db_cursor.execute(insert_manager_info_statement, seller_data)
                db_connection.commit()
                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_account_info(self, account_info, db_connection):

        """ 로그인 정보 확인

        account_info 를 통해서 DB 에 있는 특정 계정 정보의 account_no 와 암호화 되어있는 password 를 가져와서 return

        Args:
            account_info: 유효성 검사를 통과한 account 정보 (login_id, password)
            db_connection: 연결된 database connection 객체

        Returns:
            200: db_account_info db 에서 get 한 account_no 와 password
            400: INVALID_KEY
            500: DB_CURSOR_ERROR

        Authors:
            choiyj@brandi.co.kr (최예지)

        History:
            2020-04-05 (choiyj@brandi.co.kr): 초기 생성
            2020-04-05 (choiyj@brandi.co.kr): SQL 문을 통해 DB 에서 원하는 정보를 가지고 와서 return 하는 함수 구현
        """

        try:
            # db_cursor 는 db_connection 에 접근하는 본체 (가져온 정보는 cursor 가 가지고 있다)
            with db_connection as db_cursor:

                # sql 문 작성 (원하는 정보를 가져오거나 집어넣거나)
                select_account_info_statement = """
                    SELECT
                    account_no,
                    password
                    
                    FROM accounts
                    
                    where login_id = %(login_id)s AND is_deleted = 0
                """

                # SELECT 문 실행
                db_cursor.execute(select_account_info_statement, account_info)

                # DB 에 저장하는 로직 작성 (fetchone, fetchall, fetchmany)
                account_info_result = db_cursor.fetchone()

                # DB 에서 꺼내온 정보를 return
                return account_info_result

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def check_overlap_login_id(self, login_id, db_connection):

        """ 로그인 아이디 중복 체크

        service 에서 전달 받은 login_id 가 DB에 존재하는지 확인해서 리턴

        Args:
            login_id: account_info 의 login_id
            db_connection: 연결된 database connection 객체

        Returns:
            login_id로 확인된 계정 번호.
            -> service 에서 계정번호가 검색된 경우 중복처리 진행
            500: DB_CURSOR_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-06 (leejm3@brandi.co.kr): 초기 생성

        """

        try:
            with db_connection.cursor() as db_cursor:

                # 계정 SELECT 문
                select_account_statement = """
                    SELECT
                    account_no
                    FROM
                    accounts
                    WHERE
                    login_id = %(login_id)s
                """

                # service 에서 넘어온 셀러 데이터
                login_id_data = {
                    'login_id': login_id
                }

                # 데이터 sql 명령문과 셀러 데이터 바인딩
                db_cursor.execute(select_account_statement, login_id_data)

                # 쿼리로 나온 계정번호를 저장
                select_result = db_cursor.fetchone()
                return select_result

        # 데이터베이스 error
        except Exception as e:
            print(f'DAO_DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'error': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def check_overlap_name_kr(self, name_kr, db_connection):
        """ 셀러명 중복 체크

        service 에서 전달 받은 name_kr 가 DB에 존재하는지 확인해서 리턴

        Args:
            name_kr: account_info 의 name_kr
            db_connection: 연결된 database connection 객체

        Returns:
            name_kr로 확인된 셀러정보 번호.
                -> service 에서 셀러정보 번호가 검색된 경우 중복처리 진행
            500: INVALID_KEY, DB_CURSOR_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-06 (leejm3@brandi.co.kr): 초기 생성

        """

        try:
            with db_connection.cursor() as db_cursor:

                # 셀러정보 SELECT 문
                select_seller_info_statement = """
                    SELECT
                    seller_info_no
                    FROM
                    seller_infos
                    WHERE
                    name_kr = %(name_kr)s
                    AND is_deleted = 0
                """

                # service 에서 넘어온 셀러 데이터
                name_kr_data = {
                    'name_kr': name_kr
                }

                # 데이터 sql 명령문과 셀러 데이터 바인딩
                db_cursor.execute(select_seller_info_statement, name_kr_data)

                # 쿼리로 나온 셀러정보 번호를 저장
                select_result = db_cursor.fetchone()
                return select_result

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Exception as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'error': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def check_overlap_name_en(self, name_en, db_connection):
        """ 셀러 영문명 중복 체크

        service 에서 전달 받은 name_en 가 DB에 존재하는지 확인해서 리턴

        Args:
            name_en: account_info 의 name_en
            db_connection: 연결된 database connection 객체

        Returns:
            200:name_en로 확인된 셀러정보 번호.
                -> service 에서 셀러정보 번호가 검색된 경우 중복처리 진행
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-06 (leejm3@brandi.co.kr): 초기 생성

        """

        try:
            with db_connection.cursor() as db_cursor:

                # 셀러정보 SELECT 문
                select_seller_info_statement = """
                    SELECT
                    seller_info_no
                    FROM
                    seller_infos
                    WHERE
                    name_en = %(name_en)s
                    AND is_deleted = 0
                """

                # service 에서 넘어온 셀러 데이터
                name_en_data = {
                    'name_en': name_en
                }

                # 데이터 sql 명령문과 셀러 데이터 바인딩
                db_cursor.execute(select_seller_info_statement, name_en_data)

                # 쿼리로 나온 셀러정보 번호를 저장
                select_result = db_cursor.fetchone()
                return select_result

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Exception as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'error': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def sign_up(self, account_info, db_connection):

        """ 계정 회원가입 데이터를 INSERT 하는 DAO

        1. accounts 계정 생성
        2. seller_accounts 셀러 계정 생성
        3. seller_infos 셀러 정보 생성
        4. manage_infos 담당자 정보 생성
        5. seller_status_change_histories 셀러 상태 변경 이력 생성

        Args:
            account_info: 유효성 검사를 통과한 account 정보
                login_id 로그인 아이디
                password 암호화된 비밀번호
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
            500: INVALID_KEY, DB_CURSOR_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-01 (leejm3@brandi.co.kr) : 초기 생성
            
        """

        try:
            with db_connection.cursor() as db_cursor:

                # accounts 생성
                # 계정 INSERT 문
                insert_accounts_statement = """
                    INSERT INTO accounts(
                    auth_type_id,
                    login_id,
                    password
                ) VALUES (
                    2,
                    %(login_id)s,
                    %(password)s
                )"""

                # 데이터 sql 명령문과 셀러 데이터 바인딩
                db_cursor.execute(insert_accounts_statement, account_info)

                # 위에서 생성된 새로운 계정의 id 값을 가져옴
                account_no = db_cursor.lastrowid
                account_info['account_no'] = account_no
                # seller_accounts 생성
                # 셀러계정 INSERT 문
                insert_seller_accounts_statement = """
                    INSERT INTO seller_accounts(
                    account_id
                ) VALUES (
                    %(account_no)s
                )"""

                # 데이터 sql 명령문과 셀러 데이터 바인딩
                db_cursor.execute(insert_seller_accounts_statement, account_info)

                # 위에서 생성된 셀러계정의 id 값을 가져옴
                seller_account_no = db_cursor.lastrowid
                account_info['seller_account_id'] = seller_account_no

                # seller_infos 생성
                # 셀러정보 INSERT 문
                insert_seller_infos_statement = """
                    INSERT INTO seller_infos(
                    seller_account_id,
                    seller_type_id,
                    seller_status_id,
                    product_sort_id,
                    name_kr,
                    name_en,
                    center_number,
                    site_url,
                    kakao_id,
                    insta_id,
                    modifier
                ) VALUES (
                    %(seller_account_id)s,
                    %(seller_type_id)s,
                    1,
                    (SELECT product_sort_id FROM seller_types WHERE seller_type_no = %(seller_type_id)s),
                    %(name_kr)s,
                    %(name_en)s,
                    %(center_number)s,
                    %(site_url)s,
                    %(kakao_id)s,
                    %(insta_id)s,
                    %(account_no)s
                )"""

                # 데이터 sql 명령문과 셀러 데이터 바인딩
                db_cursor.execute(insert_seller_infos_statement, account_info)

                # 위에서 생성된 셀러정보의 id 값을 가져옴
                seller_info_no = db_cursor.lastrowid
                account_info['seller_info_no'] = seller_info_no

                # manager_infos 생성
                # 담당자정보 INSERT 문
                insert_manager_infos_statement = """
                    INSERT INTO manager_infos(
                    contact_number,
                    seller_info_id
                ) VALUES (
                    %(contact_number)s,
                    %(seller_info_no)s
                )"""

                # 데이터 sql 명령문과 셀러 데이터 바인딩
                db_cursor.execute(insert_manager_infos_statement, account_info)

                # seller_status_change_histories 생성
                # 셀러 상태변경 이력 INSERT 문
                insert_status_histories_statement = """
                    INSERT INTO seller_status_change_histories(
                    seller_account_id,
                    seller_status_id,
                    modifier                    
                ) VALUES (
                    %(seller_account_id)s,
                    1,
                    %(account_no)s
                )"""

                # 데이터 sql 명령문과 셀러 데이터 바인딩
                db_cursor.execute(insert_status_histories_statement, account_info)
                db_connection.commit()
                return jsonify({"message": "SUCCESS"}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500
