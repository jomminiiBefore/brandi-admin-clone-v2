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
        각 기획전에 맞는 필드를 등록하는 dao 를 실행함

        Args:
            event_info: 유효성 검사를 통과한 기획전 등록 정보
            db_connection: 연결된 database connection 객체

        Returns: http 응답코드
            200: SUCCESS 기획전 신규 등록 완료

        Authors:
            leejm3@brandi.co.kr (이종민)
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-07 (leejm3@brandi.co.kr): 초기생성
            2020-04-10 (yoonhc@brandi.co.kr): 상품(이미지), 상품(텍스트), 유튜브 기획전 작성
        """

        event_dao = EventDao()
        try:
            # 기획전 타입이 이벤트일 경우
            if event_info['event_type_id'] == "1":
                registering_event_result = event_dao.register_event_event(event_info, db_connection)
                return registering_event_result

            # 기획전 타입이 쿠폰일 경우
            if event_info['event_type_id'] == "2":
                registering_event_result = event_dao.register_coupon_event(event_info, db_connection)
                return registering_event_result

            # 기획전 타입이 상품(이미지)일 경우
            if event_info['event_type_id'] == "3":
                registering_event_result = event_dao.register_product_image_event(event_info, event_product_info, db_connection)
                print(1)
                return registering_event_result

            # 기획전 타입이 상품(텍스트)일 경우
            if event_info['event_type_id'] == "4":
                registering_event_result = event_dao.register_product_text_event(event_info, event_product_info, db_connection)
                return registering_event_result

            # 기획전 타입이 유튜브일 경우
            if event_info['event_type_id'] == "5":
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
