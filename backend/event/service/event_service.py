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
    def register_event(self, event_info, db_connection):

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

        History:
            2020-04-07 (leejm3@brandi.co.kr): 초기생성

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

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400
