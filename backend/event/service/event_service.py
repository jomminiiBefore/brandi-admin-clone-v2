from flask import jsonify, g
from datetime import datetime, timedelta
from connection import DatabaseConnection

from event.model.event_dao import EventDao


class EventService:

    """ 기획전 서비스

    Authors:
        leejm3@brandi.co.kr (이종민)
    History:
        2020-04-07 (leejm3@brandi.co.kr): 초기생성

        """

    # noinspection PyMethodMayBeStatic
    def register_event(self, event_info, db_connection, event_product_info):

        """ 기획전 등록 로직

        event_info 에 담긴 기획전 타입을 확인하고,
        타입별 들어오지 말아야 할 키들을 유효성검사 해줌.
        각 기획전에 맞는 필드를 등록하는 dao 를 실행함

        Args:
            event_info: 유효성 검사를 통과한 기획전 등록 정보
            db_connection: 연결된 database connection 객체
            event_product_info: 기획전타입이 3, 4, 5인 경우 기획전상품값이 들어옴..

        Returns: http 응답코드
            200: SUCCESS 기획전 신규 등록 완료

        Authors:
            leejm3@brandi.co.kr (이종민)
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-07 (leejm3@brandi.co.kr): 초기생성
            2020-04-10 (yoonhc@brandi.co.kr): 상품(이미지), 상품(텍스트), 유튜브 기획전 작성
            2020-04-12 (leejm3@brandi.co.kr): event_type_id 를 str 로 확인하던 것에서 int 로 확인하도록 변경
            2020-04-15 (yoonhc@brandi.co.kr): 기획전 타입 별 들어오지 말아야할 키 유효성검사 추가.
        """

        event_dao = EventDao()
        try:
            # 기획전 타입이 이벤트일 경우
            if event_info['event_type_id'] == 1:
                # 기획전 이벤트에 들어오면 안되는 필드를 걸러줌.
                if event_info['long_description']:
                    return jsonify({'message': 'INVALID_FIELD_LONG_DESCRIPTION'}), 400
                if event_info['youtube_url']:
                    return jsonify({'message': 'INVALID_FIELD_YOUTUBE_URL'}), 400
                if event_product_info:
                    return jsonify({'message': 'INVALID_FILED_EVENT_PRODUCT'}), 400

                registering_event_result = event_dao.register_event_event(event_info, db_connection)
                return registering_event_result

            # 기획전 타입이 쿠폰일 경우
            if event_info['event_type_id'] == 2:
                if event_info['banner_image_url']:
                    return jsonify({'message': 'INVALID_FIELD_BANNER_IMAGE_URL'}), 400
                if event_info['detail_image_url']:
                    return jsonify({'message': 'INVALID_FIELD_DETAIL_IMAGE_URL'}), 400
                if event_info['youtube_url']:
                    return jsonify({'message': 'INVALID_FIELD_YOUTUBE_URL'}), 400
                if event_product_info:
                    return jsonify({'message': 'INVALID_FILED_EVENT_PRODUCT'}), 400

                registering_event_result = event_dao.register_coupon_event(event_info, db_connection)
                return registering_event_result

            # 기획전 타입이 상품(이미지)일 경우
            if event_info['event_type_id'] == 3:
                # 기획전 값이 상품이미지 일 경우 들어오지 말아야 할 키값을 걸러줌.
                if event_info['long_description']:
                    return jsonify({'message': 'INVALID_FIELD_LONG_DESCRIPTION'}), 400
                if event_info['short_description']:
                    return jsonify({'message': 'INVALID_FIELD_SHORT_DESCRIPTION'}), 400
                if event_info['youtube_url']:
                    return jsonify({'message': 'INVALID_FIELD_YOUTUBE_URL'}), 400
                if event_info['button_name'] or event_info['button_link_type_id'] or event_info['button_link_description']:
                    return jsonify({'message': 'INVALID_FIELD_BUTTON'}), 400

                registering_event_result = event_dao.register_product_image_event(event_info, event_product_info, db_connection)
                return registering_event_result

            # 기획전 타입이 상품(텍스트)일 경우
            if event_info['event_type_id'] == 4:
                # 기획전 타입이 상품텍스트 일 때 들어오지 말아야 할 키값을 걸러줌.
                if event_info['youtube_url']:
                    return jsonify({'message': 'INVALID_FIELD_YOUTUBE_URL'}), 400
                if event_info['button_name'] or event_info['button_link_type_id'] or event_info['button_link_description']:
                    return jsonify({'message': 'INVALID_FIELD_BUTTON'}), 400
                if event_info['detail_image_url']:
                    return jsonify({'message': 'INVALID_FIELD_DETAIL_IMAGE_URL'}), 400
                if event_info['long_description']:
                    return jsonify({'message': 'INVALID_FIELD_LONG_DESCRIPTION'}), 400

                registering_event_result = event_dao.register_product_text_event(event_info, event_product_info, db_connection)
                return registering_event_result

            # 기획전 타입이 유튜브일 경우
            if event_info['event_type_id'] == 5:
                # 기획전 타입이 유튜브일 때 들어오지 말아야 할 키값들을 걸러줌.
                if event_info['button_name'] or event_info['button_link_type_id'] or event_info['button_link_description']:
                    return jsonify({'message': 'INVALID_FIELD_BUTTON'}), 400
                if event_info['long_description']:
                    return jsonify({'message': 'INVALID_FIELD_LONG_DESCRIPTION'}), 400

                registering_event_result = event_dao.register_youtube_event(event_info,event_product_info, db_connection)
                return registering_event_result

        except TypeError as e:
            return jsonify({'service_message': f'{e}'}), 400

    # noinspection PyMethodMayBeStatic
    def get_event_types(self, db_connection):

        """ 기획전 타입 목록 표출

        기획전 전체 타입 목록을 표출합니다.

        Args:
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 기획전 타입 목록
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-09 (leejm3@brandi.co.kr): 초기 생성

        """
        try:
            event_dao = EventDao()
            types = event_dao.get_event_types(db_connection)

            return types

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

    # noinspection PyMethodMayBeStatic
    def get_event_sorts(self, event_type_info, db_connection):
        """ 기획전 타입별 종류 목록 표출

        기획전 특정 타입별 종류 목록을 표출합니다.

        Args:
            event_type_info: 이벤트 타입 정보
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 기획전 타입별 종류 목록
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-09 (leejm3@brandi.co.kr): 초기 생성

        """

        try:
            event_dao = EventDao()
            sorts = event_dao.get_event_sorts(event_type_info, db_connection)

            return sorts

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

    # noinspection PyMethodMayBeStatic
    def get_event_infos(self, event_no, db_connection):

        """ 기획전 정보 표출 로직

        전달 받은 기획전 번계정번호에 맞는 셀러정보를 표출해줍니다.

        Args:
            event_no: 기획전 번호
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: 기획전 정보
            400: INVALID_EVENT_NO
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-10 (leejm3@brandi.co.kr) : 초기 생성

        """

        event_dao = EventDao()
        try:
            getting_event_info_result = event_dao.get_event_infos(event_no, db_connection)
            return getting_event_info_result

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

    # noinspection PyMethodMayBeStatic
    def change_event_infos(self, event_info, event_product_info, db_connection):

        """ 기획전 수정 로직

        event_info 에 담긴 기획전 타입을 확인하고,
        각 기획전 타입에 들어오지 말아야 할 키값을 걸러줌.
        기획전타입 확인과 유효성검사가 끝나면 dao로 arguments 를 넘김.

        Args:보
            event_info: 유효성 검사를 통과한 기획전 등록 정보
            event_product_info: 상품, 유튜브 타입의 기획전에서 사용되는 상품 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 기획전 수정 완료
            400: NOT_ALLOWED_TO_CHANGE_EVENT_TYPE_OR_SORT,
                 INVALID_EVENT_NO,
                 INVALID_FIELD_LONG_DESCRIPTION,
                 INVALID_FIELD_SHORT_DESCRIPTION,
                 INVALID_FIELD_YOUTUBE_URL,
                 INVALID_FILED_EVENT_PRODUCT,
                 INVALID_FIELD_BUTTON,
                 INVALID_FIELD_BANNER_IMAGE_URL,
                 INVALID_FIELD_DETAIL_IMAGE_URL,
            500: DB_CURSOR_ERROR, INVALID_KEY

        Authors:
            leejm3@brandi.co.kr (이종민)
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-10 (leejm3@brandi.co.kr): 초기생성
            2020-04-11 (yoonhc@brandi.co.kr): 각 기획전 타입별 들어오지 말아야할 키값을 걸러주는 로직 추가.

        """

        event_dao = EventDao()
        try:
            # 기획전 타입이 이벤트일 경우
            if event_info['event_type_id'] == 1:

                # 기획전 이벤트에 들어오면 안되는 필드를 걸러줌.
                if event_info['long_description']:
                    return jsonify({'message': 'INVALID_FIELD_LONG_DESCRIPTION'}), 400
                if event_info['youtube_url']:
                    return jsonify({'message': 'INVALID_FIELD_YOUTUBE_URL'}), 400
                if event_product_info:
                    return jsonify({'message': 'INVALID_FILED_EVENT_PRODUCT'}), 400

                # 통과되면(기획전 타입이 이벤트로 판명되면) dao 로 arguments 를 넘겨줌.
                changing_event_result = event_dao.change_event(event_info, db_connection, event_product_info)
                return changing_event_result

            # 기획전 타입이 쿠폰일 경우
            if event_info['event_type_id'] == 2:
                if event_info['banner_image_url']:
                    return jsonify({'message': 'INVALID_FIELD_BANNER_IMAGE_URL'}), 400
                if event_info['detail_image_url']:
                    return jsonify({'message': 'INVALID_FIELD_DETAIL_IMAGE_URL'}), 400
                if event_info['youtube_url']:
                    return jsonify({'message': 'INVALID_FIELD_YOUTUBE_URL'}), 400
                if event_product_info:
                    return jsonify({'message': 'INVALID_FILED_EVENT_PRODUCT'}), 400

                # 통과되면(기획전타입이 쿠폰으로 판명되면) dao 로 arguments 를 넘겨줌
                changing_event_result = event_dao.change_event(event_info, db_connection, event_product_info)
                return changing_event_result

            # 기획전 타입이 상품(이미지)일 경우
            if event_info['event_type_id'] == 3:

                # 기획전 값이 상품이미지 일 경우 들어오지 말아야 할 키값을 걸러줌.
                if event_info['long_description']:
                    return jsonify({'message': 'INVALID_FIELD_LONG_DESCRIPTION'}), 400
                if event_info['short_description']:
                    return jsonify({'message': 'INVALID_FIELD_SHORT_DESCRIPTION'}), 400
                if event_info['youtube_url']:
                    return jsonify({'message': 'INVALID_FIELD_YOUTUBE_URL'}), 400
                if event_info['button_name'] or event_info['button_link_type_id'] or event_info['button_link_description']:
                    return jsonify({'message': 'INVALID_FIELD_BUTTON'}), 400

                # 통과되면(기획전 타입이 상품이미지로 판명되면) dao 로 arguments 를 넘겨줌.
                changing_event_result = event_dao.change_event(event_info, db_connection, event_product_info)
                return changing_event_result

            # 기획전 타입이 상품(텍스트)일 경우
            if event_info['event_type_id'] == 4:

                # 기획전 타입이 상품텍스트 일 때 들어오지 말아야 할 키값을 걸러줌.
                if event_info['youtube_url']:
                    return jsonify({'message': 'INVALID_FIELD_YOUTUBE_URL'}), 400
                if event_info['button_name'] or event_info['button_link_type_id'] or event_info['button_link_description']:
                    return jsonify({'message': 'INVALID_FIELD_BUTTON'}), 400
                if event_info['detail_image_url']:
                    return jsonify({'message': 'INVALID_FIELD_DETAIL_IMAGE_URL'}), 400
                if event_info['long_description']:
                    return jsonify({'message': 'INVALID_FIELD_LONG_DESCRIPTION'}), 400

                # 통과되면(기획전 타입이 상품텍스트로 판명되면) dao 로 arguments 를 넘겨줌.
                changing_event_result = event_dao.change_event(event_info, db_connection, event_product_info)
                return changing_event_result

            # 기획전 타입이 유튜브일 경우
            if event_info['event_type_id'] == 5:

                # 기획전 타입이 유튜브일 때 들어오지 말아야 할 키값들을 걸러줌.
                if event_info['button_name'] or event_info['button_link_type_id'] or event_info['button_link_description']:
                    return jsonify({'message': 'INVALID_FIELD_BUTTON'}), 400
                if event_info['long_description']:
                    return jsonify({'message': 'INVALID_FIELD_LONG_DESCRIPTION'}), 400

                # 통과되면(기획전 타입이 유튜브로 판명되면) dao 로 arguments 를 넘겨줌.
                changing_event_result = event_dao.change_event(event_info, db_connection, event_product_info)
                return changing_event_result

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

    # noinspection PyMethodMayBeStatic
    def get_all_events(self, event_info, db_connection):

        """ 등록된 모든 이벤트 목록 표출

        Args:
            event_info: 이벤트 정보
                event_type_id: 이벤트 타입
                event_name: 검색어에 포함되는 이벤트 이름
                event_start_time: 검색할 이벤트 등록 날짜 시작 지점
                event_end_time: 검색할 이벤트 등록 날짜 끝 지점

            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 검색 조건에 맞는 이벤트 목록
            403: no_authorization

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-12 (leesh3@brandi.co.kr): 초기 생성
        """
        try:
            if event_info['auth_type_id'] == 1:
                event_dao = EventDao()
                events = event_dao.get_all_events(event_info, db_connection)
                return events

            return jsonify({'message': 'NO_AUTHORIZATION'}), 403

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400
