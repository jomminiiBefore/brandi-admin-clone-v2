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
            500: SERVER ERROR

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
                print(db_connection)
                # 실행 결과 반영
                db_connection.commit()
                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError:
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

