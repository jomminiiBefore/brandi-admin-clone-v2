from flask import jsonify
from mysql.connector.errors import Error


class ProductDao:

    """
    상품 모델
    """

    # noinspection PyMethodMayBeStatic
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
            with db_connection.cursor() as db_cursor:
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

    # noinspection PyMethodMayBeStatic
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
            with db_connection.cursor() as db_cursor:
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

    # noinspection PyMethodMayBeStatic
    def get_product_detail(self, product_no, db_connection):

        """상품 등록/수정시 나타나는 개별 상품의 기존 정보 표출

        상품의 번호를 받아 해당하는 상품의 상세 정보를 표출.

        Args:
            product_no(integer): 동일 상품 변경 이력의 가장 최신 버전 인덱스 번호
            db_connection(DatabaseConnection): 데이터베이스 커넥션 객체

        Returns:
            200: 상품별 상세 정보
            400: key error
            400: database cursor error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-03 (leesh3@brandi.co.kr): 초기 생성
        """
        try:
            with db_connection.cursor() as db_cursor:
                get_stmt = """
                    SELECT * FROM product_infos 
                    INNER JOIN seller_accounts   ON product_infos.seller_id = seller_accounts.seller_account_no
                    INNER JOIN product_tags      ON product_infos.product_info_no = product_tags.product_info_id
                    INNER JOIN product_images    ON product_infos.product_info_no = product_images.product_info_id
                    WHERE product_id=%(product_id)s AND close_time='2037-12-31 23:59:59.0'
                    GROUP BY product_infos.product_info_no
                """
                db_cursor.execute(get_stmt, {'product_id': product_no})
                product_information = db_cursor.fetchall()

                if product_information:
                    return jsonify(product_information), 200
                return jsonify({'message': 'PRODUCT_DOES_NOT_EXIST'}), 404

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def insert_new_product(self, product_info, db_connection):

        """ 새로운 상품 등록

        셀러 혹은 마스터가 새로운 상품을 등록.

        Args:
            product_info: 새로 등록할 제품의 상세 정보 및 담당 셀러의 account_no
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 새로운 상품 등록됨.
                새로운 아이템이 생성되는 테이블은 총 5개다.
                1. products
                2. product_infos
                3. product_images
                4. product_tags
                5. product_change_histories

            400: database cursor error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-06 (leesh3@brandi.co.kr): 초기 생성
        """

        try:
            with db_connection.cursor() as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # 토큰에서 확인한 account_no를 기준으로, product 에 매칭할 seller_id를 찾음
                get_seller_account_stmt = """
                    SELECT seller_account_no, product_sort_id
                    FROM seller_accounts
                    INNER JOIN seller_infos ON seller_infos.seller_account_id = seller_accounts.seller_account_no
                    WHERE account_id=%(account_no)s  
                """
                db_cursor.execute(get_seller_account_stmt, {'account_no': product_info['selected_account_no']})
                seller_account = db_cursor.fetchone()
                product_info['seller_id'] = seller_account['seller_account_no']
                product_info['product_sort_id'] = seller_account['product_sort_id']

                # 1. TABLE products
                # products 테이블에 먼저 요소 생성
                insert_product_stmt = """
                    INSERT INTO products (
                        uploader
                    ) VALUES (
                        %(uploader)s
                    )
                """
                db_cursor.execute(insert_product_stmt, product_info)

                # 2. TABLE product_infos
                # 직전에 product 테이블에 생성한 아이템의 product_no를 product_info 테이블의 product_id에 짝 지어 줌.
                product_info['product_id'] = db_cursor.lastrowid

                # product 테이블 INSERT INTO
                insert_product_info_stmt = """
                    INSERT INTO product_infos
                    (
                        is_available,
                        is_on_display,
                        product_sort_id,
                        first_category_id,
                        second_category_id,
                        name,
                        short_description,
                        color_filter_id,
                        style_filter_id,
                        long_description,
                        youtube_url,
                        stock,
                        price,
                        discount_rate,
                        discount_start_time,
                        discount_end_time,
                        min_unit,
                        max_unit,
                        modifier,
                        seller_id,
                        product_id
                    ) VALUES (
                        %(is_available)s,
                        %(is_on_display)s,
                        %(product_sort_id)s,
                        %(first_category_id)s,
                        %(second_category_id)s,
                        %(name)s,
                        %(short_description)s,
                        %(color_filter_id)s,
                        %(style_filter_id)s,
                        %(long_description)s,
                        %(youtube_url)s,
                        %(stock)s,
                        %(price)s,
                        %(discount_rate)s,
                        %(discount_start_time)s,
                        %(discount_end_time)s,
                        %(min_unit)s,
                        %(max_unit)s,
                        %(modifier)s,
                        %(seller_id)s,
                        %(product_id)s
                    )"""

                db_cursor.execute(insert_product_info_stmt, product_info)

                product_info_id = db_cursor.lastrowid

                # 3. TABLE product_images
                images = product_info['images']
                for image_set in images.keys():
                    image_order = image_set[-1]
                    image_sizes = ['big', 'medium', 'small']

                    if images[image_set]:
                        for size in image_sizes:
                            image_info = {
                                'image_url': images[image_set][f'{size}_size_url'],
                                'product_info_id': product_info_id,
                                'image_size_id': images[image_set][f'{size}_image_size_id'],
                                'image_order': image_order,
                            }

                            insert_image_stmt = """
                                INSERT INTO product_images(
                                    image_url,
                                    product_info_id,
                                    image_size_id,
                                    image_order
                                ) VALUES (
                                    %(image_url)s,
                                    %(product_info_id)s,
                                    %(image_size_id)s,
                                    %(image_order)s
                                )
                            """
                            db_cursor.execute(insert_image_stmt, image_info)
                    else:
                        pass

                # 4. TABLE product_tags
                for tag in product_info['tags']:

                    tag_info = {
                        'name': tag,
                        'product_info_id': product_info_id
                    }

                    insert_tag_stmt = """
                        INSERT INTO product_tags(
                            name,
                            product_info_id
                        ) VALUES (
                            %(name)s,
                            %(product_info_id)s
                        )
                    """
                    db_cursor.execute(insert_tag_stmt, tag_info)

                # 5. TABLE product_change_histories
                insert_history_stmt = """
                    INSERT INTO product_change_histories
                    (
                        product_id,
                        modifier,
                        changed_time, 
                        is_available, 
                        is_on_display, 
                        price, discount_rate, 
                        is_deleted
                    )
                    SELECT 
                        product_id, 
                        modifier, 
                        start_time, 
                        is_available, 
                        is_on_display, 
                        price, 
                        discount_rate, 
                        is_deleted
                    FROM
                        product_infos
                    WHERE
                        product_info_no=%(product_info_no)s
                """
                db_cursor.execute(insert_history_stmt, {'product_info_no': product_info_id})
                db_connection.commit()
                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 400

    def update_product_info(self, product_info, db_connection):

        """ 상품 정보 수정

        셀러 혹은 마스터가 기존 상품의 정보를 수정

        Args:
            product_info: 수정할 제품의 상세 정보 및 담당 셀러의 account_no
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 상품 정보 수정됨.
            400: database cursor error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-08 (leesh3@brandi.co.kr): 초기 생성
        """

        try:
            with db_connection.cursor() as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                db_cursor.execute("SELECT NOW()")
                updated_time = db_cursor.fetchone()
                now = updated_time['NOW()']
                product_info['start_time'] = now

                update_previous_product_info_stmt = """
                        UPDATE product_infos SET close_time=%(close_time)s 
                        WHERE product_id=%(product_id)s AND close_time='2037-12-31 23:59:59.0'
                    """
                db_cursor.execute(update_previous_product_info_stmt,
                                  {'close_time': now, 'product_id': product_info['product_id']})

                # 1. TABLE product_infos
                # product 테이블 INSERT INTO
                insert_product_info_stmt = """
                    INSERT INTO product_infos
                    (
                        is_available,
                        is_on_display,
                        product_sort_id,
                        first_category_id,
                        second_category_id,
                        name,
                        short_description,
                        color_filter_id,
                        style_filter_id,
                        long_description,
                        youtube_url,
                        stock,
                        price,
                        discount_rate,
                        discount_start_time,
                        discount_end_time,
                        min_unit,
                        max_unit,
                        modifier,
                        seller_id,
                        product_id,
                        start_time
                    ) 
                    VALUES (
                        %(is_available)s,
                        %(is_on_display)s,
                        %(product_sort_id)s,
                        %(first_category_id)s,
                        %(second_category_id)s,
                        %(name)s,
                        %(short_description)s,
                        %(color_filter_id)s,
                        %(style_filter_id)s,
                        %(long_description)s,
                        %(youtube_url)s,
                        %(stock)s,
                        %(price)s,
                        %(discount_rate)s,
                        %(discount_start_time)s,
                        %(discount_end_time)s,
                        %(min_unit)s,
                        %(max_unit)s,
                        %(modifier)s,
                        %(seller_id)s,
                        %(product_id)s,
                        %(start_time)s
                    )"""

                db_cursor.execute(insert_product_info_stmt, product_info)

                product_info_id = db_cursor.lastrowid

                # 2. TABLE product_images
                images = product_info['images']
                for image_set in images.keys():
                    image_order = image_set[-1]

                    for size in ['big', 'medium', 'small']:
                        image_info = {
                            'image_url': images[image_set][f'{size}_size_url'],
                            'product_info_id': product_info_id,
                            'image_size_id': images[image_set][f'{size}_image_size_id'],
                            'image_order': image_order,
                        }

                        insert_image_stmt = """
                            INSERT INTO product_images(
                                image_url,
                                product_info_id,
                                image_size_id,
                                image_order
                            ) VALUES (
                                %(image_url)s,
                                %(product_info_id)s,
                                %(image_size_id)s,
                                %(image_order)s
                            )
                        """
                        db_cursor.execute(insert_image_stmt, image_info)

                # 3. TABLE product_tags
                for tag in product_info['tags']:

                    tag_info = {
                        'name': tag,
                        'product_info_id': product_info_id
                    }

                    insert_tag_stmt = """
                        INSERT INTO product_tags(
                            name,
                            product_info_id
                        ) VALUES (
                            %(name)s,
                            %(product_info_id)s
                        )
                    """
                    db_cursor.execute(insert_tag_stmt, tag_info)

                db_connection.commit()

                # 4. TABLE product_change_histories
                insert_history_stmt = """
                    INSERT INTO product_change_histories
                    (
                        product_id,
                        modifier,
                        changed_time, 
                        is_available, 
                        is_on_display, 
                        price, discount_rate, 
                        is_deleted
                    )
                    SELECT 
                        product_id, 
                        modifier, 
                        start_time, 
                        is_available, 
                        is_on_display, 
                        price, 
                        discount_rate, 
                        is_deleted
                    FROM
                        product_infos
                    WHERE
                        product_info_no=%(product_info_no)s
                """

                db_cursor.execute(insert_history_stmt, {'product_info_no': product_info_id})
                db_connection.commit()

                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 400
