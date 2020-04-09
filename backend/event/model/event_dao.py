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
