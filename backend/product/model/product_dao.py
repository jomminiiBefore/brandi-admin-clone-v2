from flask import jsonify
from mysql.connector.errors import Error


class ProductDao:

    """
    상품 모델
    """

    # noinspection PyMethodMayBeStatic
    def get_first_categories(self, account_no, db_connection):

        """ 상품 1차 카테고리 목록 표출

        seller 마다 다른 product_type 을 기준으로 1차 상품 카테고리를 표출

        Args:
            account_no(integer): 선택된 셀러의 account_no
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 셀러의 상품 종류에 해당하는 1차 카테고리
            400: key error
            500: database cursor error

        Authors:
            leesh3@brandi.co.kr (이소헌)
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성
            2020-04-16 (leejm3@brandi.co.kr): SQL 문 별칭 적용

        """
        try:
            with db_connection.cursor() as db_cursor:
                get_stmt = """
                    SELECT 
                        PC04.first_category_no, PC04.name
                    
                    FROM 
                        accounts AS PC01 
                    
                    INNER JOIN seller_accounts AS PC02 
                    ON PC02.account_id = PC01.account_no 
                    
                    INNER JOIN seller_infos AS PC03 
                    ON PC03.seller_account_id = PC02.seller_account_no
                    
                    INNER JOIN first_categories AS PC04 
                    ON PC04.product_sort_id  = PC03.product_sort_id
                    
                    WHERE 
                        PC01.account_no=%(account_no)s 
                        AND PC03.close_time = '2037-12-31 23:59:59.0'
                """

                db_cursor.execute(get_stmt, {'account_no': account_no})
                first_categories = db_cursor.fetchall()
                if first_categories:
                    return jsonify(first_categories), 200
                return jsonify({'message': 'CATEGORY_DOES_NOT_EXIST'}), 404

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

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
            404: CATEGORY_DOES_NOT_EXIST
            500: database cursor error

        Authors:
            leesh3@brandi.co.kr (이소헌)
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성
            2020-04-16 (leejm3@brandi.co.kr): SQL 문 별칭 적용, 에러 주석 추가

        """
        try:
            with db_connection.cursor() as db_cursor:
                get_stmt = """
                    SELECT 
                        PC01.second_category_no, PC01.name 
                    
                    FROM 
                        second_categories AS PC01
                    
                    INNER JOIN first_categories AS PC02 
                    ON PC02.first_category_no = PC01.first_category_id 
                    
                    WHERE 
                        PC02.first_category_no = %(first_category_no)s;
                """
                db_cursor.execute(get_stmt, {'first_category_no': first_category_no})
                second_categories = db_cursor.fetchall()
                if second_categories:
                    return jsonify({'second_categories': second_categories}), 200

                return jsonify({'message': 'CATEGORY_DOES_NOT_EXIST'}), 404

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_product_detail(self, product_no, db_connection):

        """상품 등록/수정시 나타나는 개별 상품의 기존 정보 표출

        상품의 번호를 받아 해당하는 상품의 상세 정보를 표출

        Args:
            product_no(integer): 동일 상품 변경 이력의 가장 최신 버전 인덱스 번호
            db_connection(DatabaseConnection): 데이터베이스 커넥션 객체

        Returns:
            200: 상품별 상세 정보
            400: key_error
            404: page_not_found
            500: database_error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-03 (leesh3@brandi.co.kr): 초기 생성
        """
        try:
            with db_connection.cursor() as db_cursor:
                product_info = {
                    'product_id': product_no
                }

                get_stmt = """
                    SELECT
                        seller_id,
                        is_available,
                        is_on_display,
                        product_sort_id,
                        first_category_id,
                        second_category_id,
                        product_infos.name,
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
                        product_id,
                        product_info_no,
                        seller_account_no
                    FROM 
                        product_infos 
                    INNER JOIN 
                        seller_accounts 
                        ON product_infos.seller_id = seller_accounts.seller_account_no
                    WHERE 
                        product_id=%(product_id)s 
                    AND
                        close_time='2037-12-31 23:59:59.0'
                    GROUP BY
                        product_infos.product_info_no
                """
                db_cursor.execute(get_stmt, product_info)
                product_information = db_cursor.fetchone()

                if product_information:
                    get_tag_stmt = """
                        SELECT
                            name
                        FROM
                            product_tags
                        WHERE
                            product_info_id = %(product_info_no)s
                    """
                    db_cursor.execute(get_tag_stmt, product_information)
                    tags = db_cursor.fetchall()
                    product_information['tags'] = [tag['name'] for tag in tags]

                    get_image_stmt = """
                        SELECT
                            image_order,
                            image_url
                        FROM
                            product_images
                        WHERE
                            product_info_id = %(product_info_no)s
                        AND
                            image_size_id = 3                            
                    """
                    db_cursor.execute(get_image_stmt, product_information)
                    images = db_cursor.fetchall()
                    product_information['images'] = images

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

            400: key_error
            404: ACCOUNT_DOES_NOT_EXIST
            500: database_error

        Authors:
            leesh3@brandi.co.kr (이소헌)
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-06 (leesh3@brandi.co.kr): 초기 생성
            2020-04-09 (leesh3@brandi.co.kr): tag, image 정보 추가 부분 리스트 표현식으로 수정
            2020-04-16 (leejm3@brandi.co.kr): 해당 셀러가 존재하지 않을 경우 에러 반환 추가
        """

        try:
            with db_connection.cursor() as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # 토큰에서 확인한 account_no를 기준으로, product 에 매칭할 seller_id를 찾음
                get_seller_account_stmt = """
                    SELECT
                        seller_account_no,
                        product_sort_id
                        
                    FROM
                        seller_accounts
                        
                    INNER JOIN
                        seller_infos 
                        ON seller_infos.seller_account_id = seller_accounts.seller_account_no
                    
                    WHERE
                        account_id=%(account_no)s  
                """
                db_cursor.execute(get_seller_account_stmt, {'account_no': product_info['selected_account_no']})
                seller_account = db_cursor.fetchone()

                # 셀러가 존재할 경우
                if seller_account:
                    product_info['seller_id'] = seller_account['seller_account_no']
                    product_info['product_sort_id'] = seller_account['product_sort_id']

                # 셀러가 존재하지 않을 경우
                else:
                    return jsonify({'message': 'ACCOUNT_DOES_NOT_EXIST'}), 404

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
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def update_product_info(self, product_info, db_connection):

        """ 상품 정보 수정

        셀러 혹은 마스터가 기존 상품의 정보를 수정

        Args:
            product_info: 수정할 제품의 상세 정보 및 담당 셀러의 account_no
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 상품 정보 수정됨.
            400: key_error
            403: 셀러 불일치
            500: database_error

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

                get_product_owner_stmt = """
                    SELECT
                        account_id
                    
                    FROM
                        seller_accounts
                    
                    INNER JOIN
                        product_infos ON product_infos.seller_id = seller_accounts.seller_account_no
                    
                    WHERE
                        product_id=%(product_id)s
                    
                    AND
                        product_infos.close_time='2037-12-31 23:59:59'
                """
                db_cursor.execute(get_product_owner_stmt, product_info)
                validated_account = db_cursor.fetchone()

                if not validated_account:
                    return jsonify({'message': 'PRODUCT_DOES_NOT_EXIST'}), 404

                # 상품 변경을 시도하는 계정과 상품의 셀러가 다를 경우
                if validated_account['account_id'] != product_info['token_account_no']:
                    return jsonify({'message': 'NO_AUTHORIZATION'}), 403

                db_cursor.execute("SELECT NOW()")
                updated_time = db_cursor.fetchone()
                now = updated_time['NOW()']
                product_info['start_time'] = now

                update_previous_product_info_stmt = """
                        UPDATE
                            product_infos
                        
                        SET
                            close_time=%(close_time)s 
                        
                        WHERE
                            product_id=%(product_id)s
                        
                        AND
                            close_time='2037-12-31 23:59:59.0'
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
                        %(seller_account_id)s,
                        %(product_id)s,
                        %(start_time)s
                    )"""

                db_cursor.execute(insert_product_info_stmt, product_info)

                product_info_id = db_cursor.lastrowid

                # 2. TABLE product_images
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
                                'image_order': image_order
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
                        for image_size_id in range(1, len(image_sizes)+1):

                            image_info = {
                                'product_info_id': product_info_id,
                                'product_id': product_info['product_id'],
                                'image_size_id': image_size_id,
                                'image_order': image_order,
                                'previous_close_time': now
                            }

                            insert_image_stmt = """
                                INSERT INTO product_images(
                                    image_url,
                                    image_size_id,
                                    image_order,
                                    product_info_id
                                ) SELECT 
                                    image_url,
                                    image_size_id,
                                    image_order,
                                    %(product_info_id)s
                                
                                FROM
                                    product_images
                                
                                WHERE
                                    product_info_id=(
                                        SELECT 
                                            product_info_no
                                        FROM 
                                            product_infos 
                                        WHERE 
                                            product_id = %(product_id)s
                                        AND
                                            close_time = %(previous_close_time)s)                                        
                                AND
                                    image_order=%(image_order)s AND image_size_id=%(image_size_id)s                                
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
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_color_filters(self, db_connection):

        """ 상품 등록시 컬러 필터 표출

        Args:
            db_connection: 데이터베이스 연결 객체

        Returns:
            200: 상품 등록시 선택할 수 있는 색상 필터
            400: key_error
            500: 데이터베이스 에러

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-09 (leesh3@brandi.co.kr): 초기 생성
        """
        try:
            with db_connection.cursor() as db_cursor:
                get_colors_stmt = """
                    SELECT
                        *
                    
                    FROM
                        color_filters
                    
                    WHERE NOT
                        color_filter_no=19
                """
                db_cursor.execute(get_colors_stmt)
                colors = db_cursor.fetchall()

                return jsonify({'colors': colors}), 200

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 400

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_product_list(self, filter_info, db_connection):

        """ 필터링된 상품 리스트 표출

        Args:
            filter_info: 필터에 쓰이는 쿼리 정보
            db_connection: 연결된 database connection 객체

        Returns:
            200: 필터링된 상품 정보 리스트
            500: DB_CURSOR_ERROR

        Authors:
            kimsj5@brandi.co.kr (김승준)
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-09 (kimsj5@brandi.co.kr): 초기 생성
            2020-04-13 (leejm3@brandi.co.kr):
               - offset / limit 유효성 view 에서 확인하도록 이동
               - 조회기간 필터 추가
               - 필터링 부분 일부 리팩토링
            2020-04-15 (leejm3@brandi.co.kr):
                - f-string 으로 필터링 조건 추가했던 것을 파라미터 바인딩 형태로 변경
                - JOIN 문에서 약어 추가
                - 주석 추가
        """

        try:
            with db_connection as db_cursor:

                # 상품 리스트를 가져오는 sql 명령문, 쿼리가 들어오면 쿼리문을 바인딩해서 검색 실행
                select_product_list_statement = '''
                    SELECT 
                        PL01.created_at, 
                        PL03.image_url, 
                        PL02.name as product_name,
                        PL01.product_no, 
                        PL05.name as seller_type_name,
                        PL04.name_kr as seller_name,
                        PL02.price,
                        FLOOR(PL02.price*(1-PL02.discount_rate)) as discount_price,
                        PL02.is_available,
                        PL02.is_on_display,
                        (CASE WHEN PL02.discount_rate > 0 THEN 1 ELSE 0 END) AS is_discount

                    FROM products as PL01
                    
                    # 상품 정보 조인
                    LEFT JOIN product_infos as PL02
                    ON PL01.product_no = PL02.product_id
                    
                    # 상품 이미지 조인
                    LEFT JOIN product_images as PL03 
                    ON PL02.product_info_no = PL03.product_info_id
                     
                     # 셀러 정보 조인
                    LEFT JOIN seller_infos as PL04 
                    ON PL04.seller_account_id = PL02.seller_id
                    
                    # 셀러 속성 조인
                    LEFT JOIN seller_types as PL05
                    ON PL04.seller_type_id = PL05.seller_type_no
                    
                    # 셀러 계정 조인
                    LEFT JOIN seller_accounts as PL06 
                    ON PL04.seller_account_id = PL06.seller_account_no

                    WHERE
                    -- 셀러 계정과 상품 삭제여부
                    PL06.is_deleted = 0
                    AND PL01.is_deleted = 0
                    
                    -- 상품 이미지 제한
                    AND PL03.image_order = 1
                    AND PL03.image_size_id = 1
                    
                    -- 상품, 셀러 정보 최신 이력 제한
                    AND PL02.close_time ='2037-12-31 23:59:59'
                    AND PL04.close_time = '2037-12-31 23:59:59'
                    '''
                # 검색 조건
                # 등록 기간 시작
                if filter_info.get('period_start', None):
                    select_product_list_statement += " AND PL01.created_at > %(period_start)s"

                # 등록기간 종료
                if filter_info.get('period_end', None):
                    select_product_list_statement += " AND PL01.created_at < %(period_end)s"

                # 셀러명
                if filter_info.get('seller_name', None):
                    select_product_list_statement += " AND PL04.name_kr = %(seller_name)s"

                # 상품명
                if filter_info.get('product_name', None):
                    select_product_list_statement += " AND PL02.name = %(product_name)s"

                # 상품번호
                if filter_info.get('product_number', None):
                    select_product_list_statement += " AND PL01.product_no = %(product_number)s"

                # 셀러 속성
                if filter_info.get('seller_type_id', None):
                    filter_info['seller_type_id'] = tuple(filter_info['seller_type_id'])
                    select_product_list_statement += " AND PL05.seller_type_no in %(seller_type_id)s"

                # 판매여부
                if filter_info.get('is_available', None) is not None:
                    select_product_list_statement += " AND PL02.is_available = %(is_available)s"

                # 진열여부
                if filter_info.get('is_on_display', None) is not None:
                    select_product_list_statement += " AND PL02.is_on_display = %(is_on_display)s"

                # 할인여부
                if filter_info.get('is_on_discount', None) is not None:
                    if filter_info['is_on_discount'] == 1:
                        select_product_list_statement += " AND PL02.discount_rate > 0"

                    else:
                        select_product_list_statement += " AND PL02.discount_rate = 0"

                # 페이징 마지막
                if filter_info.get('limit', None):
                    select_product_list_statement += " LIMIT %(limit)s"

                # 페이징 시작
                if filter_info.get('offset', None):
                    select_product_list_statement += " OFFSET %(offset)s"

                # sql 쿼리와 pagination 데이터 바인딩
                db_cursor.execute(select_product_list_statement, filter_info)
                product_info = db_cursor.fetchall()

                # pagination 을 위해서 상품 몇개인지 카운트
                product_count_statement = '''
                    SELECT 
                      COUNT(0) as filtered_product_count

                    FROM products as PL01
                    
                    # 상품 정보 조인
                    LEFT JOIN product_infos as PL02
                    ON PL01.product_no = PL02.product_id
                    
                    # 상품 이미지 조인
                    LEFT JOIN product_images as PL03 
                    ON PL02.product_info_no = PL03.product_info_id
                     
                     # 셀러 정보 조인
                    LEFT JOIN seller_infos as PL04 
                    ON PL04.seller_account_id = PL02.seller_id
                    
                    # 셀러 속성 조인
                    LEFT JOIN seller_types as PL05
                    ON PL04.seller_type_id = PL05.seller_type_no
                    
                    # 셀러 계정 조인
                    LEFT JOIN seller_accounts as PL06 
                    ON PL04.seller_account_id = PL06.seller_account_no

                    WHERE
                    -- 셀러 계정과 상품 삭제여부
                    PL06.is_deleted = 0
                    AND PL01.is_deleted = 0
                    
                    -- 상품 이미지 제한
                    AND PL03.image_order = 1
                    AND PL03.image_size_id = 1
                    
                    -- 상품, 셀러 정보 최신 이력 제한
                    AND PL02.close_time ='2037-12-31 23:59:59'
                    AND PL04.close_time = '2037-12-31 23:59:59'

                   '''
                # 검색 조건
                # 등록 기간 시작
                if filter_info.get('period_start', None):
                    product_count_statement += " AND PL01.created_at > %(period_start)s"

                # 등록기간 종료
                if filter_info.get('period_end', None):
                    product_count_statement += " AND PL01.created_at < %(period_end)s"

                # 셀러명
                if filter_info.get('seller_name', None):
                    product_count_statement += " AND PL04.name_kr = %(seller_name)s"

                # 상품명
                if filter_info.get('product_name', None):
                    product_count_statement += " AND PL02.name = %(product_name)s"

                # 상품번호
                if filter_info.get('product_number', None):
                    product_count_statement += " AND PL01.product_no = %(product_number)s"

                # 셀러 속성
                if filter_info.get('seller_type_id', None):
                    filter_info['seller_type_id'] = tuple(filter_info['seller_type_id'])
                    product_count_statement += " AND PL05.seller_type_no in %(seller_type_id)s"

                # 판매 여부
                if filter_info.get('is_available', None) is not None:
                    product_count_statement += " AND PL02.is_available = %(is_available)s"

                # 진열여부
                if filter_info.get('is_on_display', None) is not None:
                    product_count_statement += " AND PL02.is_on_display = %(is_on_display)s"

                # 할인여부
                if filter_info.get('is_on_discount', None) is not None:
                    if filter_info['is_on_discount'] == 1:
                        product_count_statement += " AND PL02.discount_rate > 0"

                    else:
                        product_count_statement += " AND PL02.discount_rate = 0"

                # 실행
                db_cursor.execute(product_count_statement, filter_info)
                product_count = db_cursor.fetchone()

                # 상품 리스트와 검색된 상품 수 리턴
                return jsonify({'product_list': product_info,
                                'product_count': product_count['filtered_product_count']
                                }), 200

        # 데이터베이스 error
        except Exception as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'error': 'DB_CURSOR_ERROR'}), 500
