from flask import jsonify
from mysql.connector.errors import Error


class EventDao:
    """ 기획전 모델

    Authors:
        leejm3@brandi.co.kr (이종민)
    History:
        2020-04-07 (leejm3@brandi.co.kr): 초기생성

    """

    # noinspection PyMethodMayBeStatic
    def register_event_event(self, event_info, db_connection):

        """ 이벤트 타입 기획전 생성 DAO

        기획전 타입이 이벤트 타입인 기획전을 생성

        Args:
            event_info: 유효성 검사를 통과한 기획전 등록 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 이벤트 기획전 생성 완료
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-07 (leejm3@brandi.co.kr): 초기생성

        """

        try:
            with db_connection.cursor() as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # 이벤트 기획전 생성
                # 기획전 INSERT 문
                insert_events_statement = """
                    INSERT INTO events(
                    uploader
                ) VALUES (
                    %(account_no)s
                )"""

                db_cursor.execute(insert_events_statement, event_info)

                # 위에서 생성된 기획전의 id 값을 가져옴
                event_no = db_cursor.lastrowid
                event_info['event_no'] = event_no

                # 이벤트 기획전 정보 생성
                # 기획전 정보 INSERT 문
                insert_event_infos_infostatement = """
                    INSERT INTO event_infos(
                    event_id,
                    event_type_id,
                    event_sort_id,
                    is_on_main,
                    is_on_event,
                    name,
                    event_start_time,
                    event_end_time,
                    short_description,
                    banner_image_url,
                    detail_image_url,
                    modifier
                ) VALUES (
                    %(event_no)s,
                    %(event_type_id)s,
                    %(event_sort_id)s,
                    %(is_on_main)s,
                    %(is_on_event)s,
                    %(name)s,
                    %(event_start_time)s,
                    %(event_end_time)s,
                    %(short_description)s,
                    %(banner_image_url)s,
                    %(detail_image_url)s,
                    %(account_no)s
                )"""

                db_cursor.execute(insert_event_infos_infostatement, event_info)

                # 위에서 생성된 기획전 정보의 id 값을 가져옴
                event_info_no = db_cursor.lastrowid
                event_info['event_info_no'] = event_info_no

                # 이벤트 기획전 상세정보 생성
                # 기획전 이벤트 상세정보 INSERT 문
                insert_event_detail_infos_statement = """
                    INSERT INTO event_detail_infos(
                    event_info_id,
                    button_name,
                    button_link_type_id,
                    button_link_description
                ) VALUES (
                    %(event_info_no)s,
                    %(button_name)s,
                    %(button_link_type_id)s,
                    %(button_link_description)s
                )"""

                db_cursor.execute(insert_event_detail_infos_statement, event_info)

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

    # noinspection PyMethodMayBeStatic
    def register_coupon_event(self, event_info, db_connection):

        """ 쿠폰 타입 기획전 생성 DAO

        기획전 타입이 쿠폰 타입인 기획전을 생성

        Args:
            event_info: 유효성 검사를 통과한 기획전 등록 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 쿠 기획전 생성 완료
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-09 (leejm3@brandi.co.kr): 초기생성

        """

        try:
            with db_connection.cursor() as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # 쿠폰 기획전 생성
                # 기획전 INSERT 문
                insert_events_statement = """
                    INSERT INTO events(
                    uploader
                ) VALUES (
                    %(account_no)s
                )"""

                db_cursor.execute(insert_events_statement, event_info)

                # 위에서 생성된 기획전의 id 값을 가져옴
                event_no = db_cursor.lastrowid
                event_info['event_no'] = event_no

                # 이벤트 기획전 정보 생성
                # 기획전 정보 INSERT 문
                insert_event_infos_infostatement = """
                    INSERT INTO event_infos(
                    event_id,
                    event_type_id,
                    event_sort_id,
                    is_on_main,
                    is_on_event,
                    name,
                    event_start_time,
                    event_end_time,
                    short_description,
                    long_description,
                    modifier
                ) VALUES (
                    %(event_no)s,
                    %(event_type_id)s,
                    %(event_sort_id)s,
                    %(is_on_main)s,
                    %(is_on_event)s,
                    %(name)s,
                    %(event_start_time)s,
                    %(event_end_time)s,
                    %(short_description)s,
                    %(long_description)s,
                    %(account_no)s
                )"""

                db_cursor.execute(insert_event_infos_infostatement, event_info)

                # 위에서 생성된 기획전 정보의 id 값을 가져옴
                event_info_no = db_cursor.lastrowid
                event_info['event_info_no'] = event_info_no

                # 쿠폰 기획전 상세정보 생성
                # 기획전 이벤트 상세정보 INSERT 문
                insert_event_detail_infos_statement = """
                    INSERT INTO event_detail_infos(
                    event_info_id,
                    button_name,
                    button_link_type_id,
                    button_link_description
                ) VALUES (
                    %(event_info_no)s,
                    %(button_name)s,
                    %(button_link_type_id)s,
                    %(button_link_description)s
                )"""

                db_cursor.execute(insert_event_detail_infos_statement, event_info)

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

    # 상품(이미지) 기획전 등록
    def register_product_image_event(self, event_info, event_product_info, db_connection):
        """ 상품(이미지) 기획전 등록

        기획전 타입이 상품(이미지)인 기획전을 등록함.

        Args:
            event_info: parameter validation을 통과한 values.
            event_product_info: 기획전용 상품. 값이 없으면 None이 들어옴.
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: SUCCESS
            500: INVALID_KEY, DB_CURSOR_ERROR

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-10 (yoonhc@brandi.co.kr): 초기 생성

        """
        try:
            with db_connection.cursor() as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # 이벤트 테이블에 새로운 이벤트 생성
                insert_event_statement = '''
                    INSERT INTO events(
                        uploader
                    ) VALUES (
                        %(account_no)s
                    )
                '''

                # 생성된 row의 아이디를 가져와서 event_info 사전에 저장.
                db_cursor.execute(insert_event_statement, event_info)
                event_no = db_cursor.lastrowid
                event_info['event_no'] = event_no

                # 이벤트 인포 이력테이블에 새로운 이력 생성
                insert_event_infos_statement = '''
                    INSERT INTO event_infos(
                    event_id,
                    event_type_id,
                    event_sort_id,
                    is_on_main,
                    is_on_event,
                    name,
                    event_start_time,
                    event_end_time,
                    banner_image_url,
                    detail_image_url,
                    modifier
                ) VALUES (
                    %(event_no)s,
                    %(event_type_id)s,
                    %(event_sort_id)s,
                    %(is_on_main)s,
                    %(is_on_event)s,
                    %(name)s,
                    %(event_start_time)s,
                    %(event_end_time)s,
                    %(banner_image_url)s,
                    %(detail_image_url)s,
                    %(account_no)s
                )'''

                db_cursor.execute(insert_event_infos_statement, event_info)
                # excute문 시행 후 방금 만들어진 이벤트인포 번호를 event_info 사전에 저장시킴
                new_event_info_id = db_cursor.lastrowid

                # 상품리스트가 있으면 이벤트용 상품 테이블에 row를 생성해줌.
                if event_product_info:

                    # for문을 돌면서 이벤트용 상품 리스트를 해당 테이블의 row로 생성함.
                    for product in event_product_info:
                        # 바인딩을 위해서 한개의 상품정보에 새로 생성된 이벤트인포 아이디를 넣어줌
                        product['new_event_info_id'] = new_event_info_id
                        print(product)

                        insert_event_detail_product_infos = '''
                        INSERT INTO event_detail_product_infos(
                            product_order,
                            product_id,
                            event_info_id
                        ) VALUES (
                            %(product_order)s,
                            %(product_id)s,
                            %(new_event_info_id)s
                        )
                        '''
                        db_cursor.execute(insert_event_detail_product_infos, product)

                        db_connection.commit()
                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'dao_message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'dao_message': 'DB_CURSOR_ERROR'}), 500

    # 상품(텍스트) 기획전 등록
    def register_product_text_event(self, event_info, event_product_info, db_connection):
        """ 상품(텍스트) 기획전 등록

        기획전 타입이 상품(텍스트)인 기획전을 등록함.

        Args:
            event_info: parameter validation을 통과한 values.
            event_product_info: 기획전용 상품. 값이 없으면 None이 들어옴.
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: SUCCESS
            500: INVALID_KEY, DB_CURSOR_ERROR

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-10 (yoonhc@brandi.co.kr): 초기 생성

        """
        try:
            with db_connection.cursor() as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # 이벤트 테이블에 새로운 이벤트 생성
                insert_event_statement = '''
                    INSERT INTO events(
                        uploader
                    ) VALUES (
                        %(account_no)s
                    )
                '''

                # 생성된 row의 아이디를 가져와서 event_info 사전에 저장.
                db_cursor.execute(insert_event_statement, event_info)
                event_no = db_cursor.lastrowid
                event_info['event_no'] = event_no

                # 이벤트 인포 이력테이블에 새로운 이력 생성
                insert_event_infos_statement = '''
                    INSERT INTO event_infos(
                    event_id,
                    event_type_id,
                    event_sort_id,
                    is_on_main,
                    is_on_event,
                    name,
                    event_start_time,
                    event_end_time,
                    short_description,
                    banner_image_url,
                    modifier
                ) VALUES (
                    %(event_no)s,
                    %(event_type_id)s,
                    %(event_sort_id)s,
                    %(is_on_main)s,
                    %(is_on_event)s,
                    %(name)s,
                    %(event_start_time)s,
                    %(event_end_time)s,
                    %(short_description)s,
                    %(banner_image_url)s,
                    %(account_no)s
                )'''

                db_cursor.execute(insert_event_infos_statement, event_info)
                # excute문 시행 후 방금 만들어진 이벤트인포 번호를 event_info 사전에 저장시킴
                new_event_info_id = db_cursor.lastrowid

                # 상품리스트가 있으면 이벤트용 상품 테이블에 row를 생성해줌.
                if event_product_info:

                    # for문을 돌면서 이벤트용 상품 리스트를 해당 테이블의 row로 생성함.
                    for product in event_product_info:
                        # 바인딩을 위해서 한개의 상품정보에 새로 생성된 이벤트인포 아이디를 넣어줌
                        product['new_event_info_id'] = new_event_info_id

                        insert_event_detail_product_infos = '''
                        INSERT INTO event_detail_product_infos(
                            product_order,
                            product_id,
                            event_info_id
                        ) VALUES (
                            %(product_order)s,
                            %(product_id)s,
                            %(new_event_info_id)s
                        )
                        '''
                        db_cursor.execute(insert_event_detail_product_infos, product)

                        db_connection.commit()
                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'dao_message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'dao_message': 'DB_CURSOR_ERROR'}), 500

    # 유튜브 이벤트 기획전 등록
    def register_youtube_event(self, event_info, event_product_info, db_connection):
        """ 유튜브 기획전 등록

        기획전 타입이 유튜브인 기획전을 등록함.

        Args:
            event_info: parameter validation을 통과한 values.
            event_product_info: 기획전용 상품. 값이 없으면 None이 들어옴.
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: SUCCESS
            500: INVALID_KEY, DB_CURSOR_ERROR

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-10 (yoonhc@brandi.co.kr): 초기 생성

        """
        try:
            with db_connection.cursor() as db_cursor:

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # 이벤트 테이블에 새로운 이벤트 생성
                insert_event_statement = '''
                    INSERT INTO events(
                        uploader
                    ) VALUES (
                        %(account_no)s
                    )
                '''

                # 생성된 row의 아이디를 가져와서 event_info 사전에 저장.
                db_cursor.execute(insert_event_statement, event_info)
                event_no = db_cursor.lastrowid
                event_info['event_no'] = event_no

                # 이벤트 인포 이력테이블에 새로운 이력 생성
                insert_event_infos_statement = '''
                        INSERT INTO event_infos(
                        event_id,
                        event_type_id,
                        event_sort_id,
                        is_on_main,
                        is_on_event,
                        name,
                        event_start_time,
                        event_end_time,
                        short_description,
                        banner_image_url,
                        detail_image_url,
                        youtube_url
                        modifier
                    ) VALUES (
                        %(event_no)s,
                        %(event_type_id)s,
                        %(event_sort_id)s,
                        %(is_on_main)s,
                        %(is_on_event)s,
                        %(name)s,
                        %(event_start_time)s,
                        %(event_end_time)s,
                        %(short_description)s,
                        %(banner_image_url)s,
                        %(detail_image_url)s,
                        %(youtube_url)s,
                        %(account_no)s
                    )'''

                db_cursor.execute(insert_event_infos_statement, event_info)
                # excute문 시행 후 방금 만들어진 이벤트인포 번호를 event_info 사전에 저장시킴
                new_event_info_id = db_cursor.lastrowid

                # 상품리스트가 있으면 이벤트용 상품 테이블에 row를 생성해줌.
                if event_product_info:

                    # for문을 돌면서 이벤트용 상품 리스트를 해당 테이블의 row로 생성함.
                    for product in event_product_info:
                        # 바인딩을 위해서 한개의 상품정보에 새로 생성된 이벤트인포 아이디를 넣어줌
                        product['new_event_info_id'] = new_event_info_id

                        insert_event_detail_product_infos = '''
                        INSERT INTO event_detail_product_infos(
                            product_order,
                            product_id,
                            event_info_id
                        ) VALUES (
                            %(product_order)s,
                            %(product_id)s,
                            %(new_event_info_id)s
                        )
                        '''
                        db_cursor.execute(insert_event_detail_product_infos, product)

                        db_connection.commit()
                return jsonify({'message': 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'dao_message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'dao_message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_event_types(self, db_connection):

        """ 기획전 타입 목록 표출

        기획전 전체 타입 목록을 표출합니다.

        Args:
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 기획전 타입 목록
            500: INVALID_KEY, DB_CURSOR_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-09 (leejm3@brandi.co.kr): 초기 생성

        """
        try:
            with db_connection.cursor() as db_cursor:
                select_statement = """
                    SELECT 
                    event_type_no as event_type_id,
                    name as event_type_name
                    FROM event_types
                    ORDER BY event_type_no
                """

                db_cursor.execute(select_statement)
                types = db_cursor.fetchall()

                return jsonify({'event_types': types}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_event_sorts(self, event_type_info, db_connection):

        """ 기획전 타입별 종류 목록 표출

        기획전 특정 타입별 종류 목록을 표출합니다.

        Args:
            event_type_info: 이벤트 타입 정보
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 기획전 타입 목록
            500: INVALID_KEY, DB_CURSOR_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-09 (leejm3@brandi.co.kr): 초기 생성

        """
        try:
            with db_connection.cursor() as db_cursor:
                select_statement = """
                    SELECT 
                    event_sort_no as event_sort_id,
                    name as event_sort_name
                    FROM event_sorts
                    WHERE event_type_id = %(event_type_id)s
                    ORDER BY event_sort_no
                """

                db_cursor.execute(select_statement, event_type_info)
                sorts = db_cursor.fetchall()

                return jsonify({'event_sorts': sorts}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def get_event_infos(self, event_no, db_connection):

        """ 기획전 정보 표출 DAO

        기획전 정보를 가져오는 DAO 입니다.

        Args:
            event_no: 기획전 번호
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 기획전 정보
            400: INVALID_EVENT_NO
            500: INVALID_KEY, DB_CURSOR_ERROR

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-10 (leejm3@brandi.co.kr): 초기 생성

        """
        try:
            with db_connection.cursor() as db_cursor:
                select_statement = """
                SELECT
                a.event_no,
                b.event_type_id,
                c.name as event_type_name,
                b.event_sort_id,
                d.name as event_sort_name,
                b.is_on_main,
                b.is_on_event,
                b.name as event_name,
                b.event_start_time,
                b.event_end_time,
                b.short_description,
                b.long_description,
                b.banner_image_url,
                b.detail_image_url,
                e.button_name,
                e.button_link_type_id,
                f.name as button_link_type_name,
                b.youtube_url
                
                FROM
                events as a
                INNER JOIN
                event_infos as b
                ON a.event_no = b.event_id
                INNER JOIN
                event_types as c
                ON b.event_type_id = c.event_type_no
                INNER JOIN
                event_sorts as d
                ON b.event_sort_id = d.event_sort_no
                LEFT JOIN
                event_detail_infos as e
                ON b.event_info_no = e.event_info_id
                INNER JOIN
                event_button_link_types as f
                ON e.button_link_type_id = f.event_button_link_type_no
                
                -- 해당 기획전 번호의 가장 최신 이력 정보를 가져옴
                WHERE a.event_no = %(event_no)s 
                AND b.close_time = '2037-12-31 23:59:59'
                """

                db_cursor.execute(select_statement, {'event_no': event_no})
                info = db_cursor.fetchone()

                # 쿼리 값이 나오지 않으면 에러 메시지 리턴
                if not info:
                    return jsonify({'message': 'INVALID_EVENT_NO'}), 400

                return jsonify({'event_info': info}), 200

        except KeyError as e:
            print(f'KEY_ERROR_WITH {e}')
            return jsonify({'message': 'INVALID_KEY'}), 500

        except Error as e:
            print(f'DATABASE_CURSOR_ERROR_WITH {e}')
            return jsonify({'message': 'DB_CURSOR_ERROR'}), 500

    # noinspection PyMethodMayBeStatic
    def change_event_event(self, event_info, db_connection):

        """ 이벤트 타입 기획전 수정 DAO

        기획전 타입이 이벤트 타입인 기획전을 생성

        Args:
            event_info: 유효성 검사를 통과한 기획전 수정 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 이벤트 기획전 수정 완료
            400: NOT_ALLOWED_TO_CHANGE_EVENT_TYPE_OR_SORT, INVALID_EVENT_NO
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-10 (leejm3@brandi.co.kr): 초기생성

        """

        try:
            with db_connection.cursor() as db_cursor:

                # 이전 기획전 정보 가져오기
                # 기획전 정보 SELECT 문
                select_event_info_statement = """
                    SELECT
                    event_type_id,
                    event_sort_id
                    
                    FROM
                    event_infos
                    
                    WHERE
                    close_time = '2037-12-31 23:59:59'
                    AND event_id = %(event_no)s
                """

                db_cursor.execute(select_event_info_statement, event_info)
                previous_info = db_cursor.fetchone()

                # 기획전 정보가 존재하지 않을 경우
                if not previous_info:
                    return jsonify({'message': 'INVALID_EVENT_NO'}), 400

                # 이전 기획전 정보의 기획전 타입과 종류가 수정하려는 정보와 다르면 에러 반
                if event_info['event_type_id'] != previous_info['event_type_id'] \
                        or event_info['event_sort_id'] != previous_info['event_sort_id']:

                    return jsonify({'message': 'NOT_ALLOWED_TO_CHANGE_EVENT_TYPE_OR_SORT'}), 400

                # 트랜잭션 시작
                db_cursor.execute("START TRANSACTION")
                # 자동 커밋 비활성화
                db_cursor.execute("SET AUTOCOMMIT=0")

                # 이벤트 기획전 정보 생성
                # 기획전 정보 INSERT 문
                insert_event_infos_infostatement = """
                    INSERT INTO event_infos(
                    event_id,
                    event_type_id,
                    event_sort_id,
                    is_on_main,
                    is_on_event,
                    name,
                    event_start_time,
                    event_end_time,
                    short_description,
                    banner_image_url,
                    detail_image_url,
                    modifier
                ) VALUES (
                    %(event_no)s,
                    %(event_type_id)s,
                    %(event_sort_id)s,
                    %(is_on_main)s,
                    %(is_on_event)s,
                    %(name)s,
                    %(event_start_time)s,
                    %(event_end_time)s,
                    %(short_description)s,
                    %(banner_image_url)s,
                    %(detail_image_url)s,
                    %(account_no)s
                )"""

                db_cursor.execute(insert_event_infos_infostatement, event_info)

                # 위에서 생성된 기획전 정보의 id 값을 가져옴
                event_info_no = db_cursor.lastrowid
                event_info['event_info_no'] = event_info_no

                # 이벤트 기획전 상세정보 생성
                # 기획전 이벤트 상세정보 INSERT 문
                insert_event_detail_infos_statement = """
                    INSERT INTO event_detail_infos(
                    event_info_id,
                    button_name,
                    button_link_type_id,
                    button_link_description
                ) VALUES (
                    %(event_info_no)s,
                    %(button_name)s,
                    %(button_link_type_id)s,
                    %(button_link_description)s
                )"""

                db_cursor.execute(insert_event_detail_infos_statement, event_info)

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
