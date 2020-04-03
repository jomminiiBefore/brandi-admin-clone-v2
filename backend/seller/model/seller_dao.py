from flask import jsonify
from mysql.connector.errors import Error


class SellerDao:

    """ 셀러 모델

    Authors:
        leesh3@brandi.co.kr (이소헌)
    History:
        2020-03-25 (leesh3@brandi.co.kr): 초기 생성
    """

    def insert_seller(self, new_seller, db_connection):

        """ 신규 셀러 계정 INSERT INTO DB

        입력된 인자가 새로운 셀러로 가입됩니다.
        가입된 셀러의 매니저 인포도 동시에 저장됩니다.
        셀러 인포와 매니저 인포가 모두 정상 저장되어야만 계정 저장이 완료됩니다.

        Args:
            new_seller(dictionary): 신규 가입 셀러
            db_connection: 데이터베이스 커넥션 객체

        Returns: http 응답코드
            200: 신규 셀러 계정 저장 완료
            400: key error
            500: server error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-03-25 (leesh3@brandi.co.kr): 초기 생성
        """
        try:
            with db_connection as db_cursor:

                new_seller_info_data = {
                    'name_kr': new_seller['name_kr'],
                    'name_en': new_seller['name_en'],
                    'site_url': new_seller['site_url'],
                    'center_number': new_seller['center_number']
                }

                new_manager_info_data = {
                    'contact_number': new_seller['contact_number'],
                    'is_deleted': new_seller['is_deleted']
                }


                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")


                # seller_infos 테이블 INSERT INTO
                insert_seller_info_statement = ("""
                    INSERT INTO seller_infos (
                    name_kr,
                    name_en,
                    site_url,
                    center_number
                ) VALUES (
                    %(name_kr)s,
                    %(name_en)s,
                    %(site_url)s,
                    %(center_number)s
                )""")

                db_cursor.execute(insert_seller_info_statement, new_seller_info_data)

                new_manager_info_data['seller_id'] = db_cursor.lastrowid

                # manager_infos 테이블 INSERT INTO
                insert_manager_info_statement = ("""
                    INSERT INTO manager_infos (
                    contact_number,
                    is_deleted,
                    seller_id
                ) VALUES (
                    %(contact_number)s,
                    %(is_deleted)s,
                    %(seller_id)s
                )""")

                db_cursor.execute(insert_manager_info_statement, new_manager_info_data)

                db_connection.commit()
                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 400

    def select_seller_info(self, db_connection):

        """ 가입된 모든 셀러 표출

        Args:
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 가입된 모든 셀러 세부 정보

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
        """

        try:
            with db_connection as db_cursor:
                seller_info = ("""
                        SELECT * FROM seller_infos
                """)
                db_cursor.execute(seller_info)
                sellers = db_cursor.fetchall()

                return jsonify({'sellers': sellers}), 200

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'})

        except Exception as e:
            print(e)

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
            400: 존재하지 않는 계정 정보
            500: SERVER ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr): 초기 생성
        """

        try:
            with db_connection as db_cursor:

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
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

        finally:
            db_cursor.close()

    # noinspection PyMethodMayBeStatic
    def change_password(self, account_info, db_connection):

        """ UPDATE 계정 비밀번호 DB

        Args:
            account_info: account 정보
            (parameter_account_no: 비밀번호를 확인할 account_no
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 비밀번호 변경 완료
            400: INVALID_KEY
            500: DB_CURSOR_ERROR, SERVER_ERROR

        Authors:
            leejm@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr): 초기 생성
        """

        try:
            with db_connection as db_cursor:

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
            400: 존재하지 않는 계정 정보
            500: DB_CURSOR_ERROR, SERVER_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-03-31 (leejm3@brandi.co.kr): 초기 생성
            2020-04-01 (leejm3@brandi.co.kr): seller_info 기본 정보 표출
            2020-04-02 (leejm3@brandi.co.kr): 외래키 관련 정보 표출
        """
        try:
            with db_connection as db_cursor:

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
                    c.name as seller_status,
                    d.name as seller_type,
                    e.login_id,
                    f.app_id as brandi_app_id,
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
                    ORDER BY b.seller_info_no DESC LIMIT 1
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
                                b.email
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
                                & d.is_deleted = 0
                                
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
                                c.name as seller_types

                                FROM 
                                product_sorts as a
                                
                                INNER JOIN
                                seller_infos as b
                                ON a.product_sort_no = b.product_sort_id
                                
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
                seller_info_result['seller_types'] = [seller_type['seller_types'] for seller_type in seller_types]

                return seller_info_result

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    def get_seller_list(self, db_connection):

        """ GET 셀러 리스트 표

        Args:
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: 셀러 리스트 표출
            500: SERVER ERROR

        Authors:
            heechul@brandi.co.kr (윤희)

        History:
            2020-04-03(heechul@brandi.co.kr): 초기 생성
        """

        try:
            with db_connection as db_cursor:
                # 셀러 리스트 표출
                sql_command = '''
                    SELECT 
                    seller_accounts.seller_account_no, 
                    accounts.login_id,
                    name_kr,
                    name_en,
                    product_infos.product_info_no, 
                    seller_infos.seller_info_no, 
                    seller_infos.seller_account_id,
                    brandi_app_user_id,
                    manager_infos.name,
                    manager_infos.contact_number,
                    manager_infos.email,
                    seller_status_id,
                    seller_types.name,
                    COUNT(products.product_no) as product_count,
                    site_url,
                    seller_accounts.created_at
                    FROM seller_infos
                    RIGHT JOIN seller_accounts ON seller_accounts.seller_account_no = seller_infos.seller_account_id
                    LEFT JOIN accounts ON seller_accounts.account_id = accounts.account_no
                    LEFT JOIN product_infos ON seller_infos.seller_account_id = product_infos.seller_id
                    LEFT JOIN seller_statuses ON seller_infos.seller_status_id = seller_statuses.status_no
                    LEFT JOIN seller_types ON seller_infos.seller_type_id = seller_types.seller_type_no 
                    LEFT JOIN products ON product_infos.product_id = products.product_no 
                    LEFT JOIN manager_infos ON manager_infos.seller_info_id = seller_infos.seller_info_no 
                    GROUP BY seller_accounts.seller_account_no
                '''
                db_cursor.execute(sql_command)
                seller_list = db_cursor.fetchall()
                return jsonify({'data': seller_list}), 200

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'error': 'DB_CURSOR_ERROR'}), 500


