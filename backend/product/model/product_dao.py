from flask import jsonify
from mysql.connector.errors import Error

class ProductDao:

    """
    품 모델
    """

    def get_first_categories(self, account_no, db_connection):

        """ 상품 1차 카테고리 목록 표출

        seller마다 다른 product_type을 기준으로 1차 상품 카테고리를 표출

        Args:
            account_no(integer): 선택된 셀러의 account_no
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 셀러의 상품 종류에 해당하는 1차 카테고리
            400: key error
            400: database cursor error

        Authors:

            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성

        """
        try:
            with db_connection as db_cursor:
                get_stmt = """
                    SELECT e.first_category_no, e.name
                    FROM accounts AS a 
                    INNER JOIN seller_accounts   AS b ON b.account_id = a.account_no 
                    INNER JOIN seller_infos 	 AS c ON c.seller_account_id = b.seller_account_no
                    INNER JOIN first_categories  AS e ON e.product_sort_id  = c.product_sort_id
                    WHERE a.account_no=%(account_no)s AND c.close_time = '2037-12-31 23:59:59.0'
                """

                db_cursor.execute(get_stmt, {'account_no': account_no})

                first_categories = db_cursor.fetchall()

                return jsonify({'first_categories': first_categories}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 400

    def get_second_categories(self, db_connection, first_category_no):

        """ 상품 2차 카테고리 목록 표출

        선택된 상품 1차 카테고릭에 따라 해당하는 2차카테고리 목록 표출

        Args:
            first_category_no(integer): 1차 카테고리 인덱스 번호
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 1차 카테고리에 해당하는 상품 2차 카테고리 목록
            400: key error
            400: database cursor error

        Authors:

            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성

        """
        try:
            with db_connection as db_cursor:
                get_stmt = """
                    SELECT sc.second_category_no, sc.name FROM second_categories AS sc
                    INNER JOIN first_categories     AS fc ON fc.first_category_no = sc.first_category_id 
                    WHERE fc.first_category_no = %(first_category_no)s;
                """
                db_cursor.execute(get_stmt, {'first_category_no': first_category_no})

                second_categories = db_cursor.fetchall()

                return jsonify({'second_categories': second_categories}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 400
