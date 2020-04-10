import re, json
from datetime import datetime

from flask import request, Blueprint, jsonify, g
from flask_request_validator import (
    GET,
    PATH,
    JSON,
    Param,
    Pattern,
    MinLength,
    MaxLength,
    validate_params
)

from event.service.event_service import EventService
from connection import get_db_connection
from utils import login_required


class EventView:

    """ 기획전 뷰

    Authors:
        leejm3@brandi.co.kr (이종민)
    History:
        2020-04-07 (leejm3@brandi.co.kr): 초기생성

    """

    event_app = Blueprint('event_app', __name__, url_prefix='/event')

    @event_app.route('', methods=['POST'], endpoint='register_event_info')
    @login_required
    @validate_params(
        # 전체 기획전 필수값
        Param('event_type_id', JSON, str,
              rules=[Pattern(r"^[1-5]{1}$")]),
        Param('event_sort_id', JSON, int),
        Param('is_on_main', JSON, str,
              rules=[Pattern(r"^[0-1]{1}$")]),
        Param('is_on_event', JSON, str,
              rules=[Pattern(r"^[0-1]{1}$")]),
        Param('name', JSON, str,
              rules=[Pattern(r"^.{1,25}$")]),
        Param('event_start_time', JSON, str,
              rules=[Pattern(r"^([2][0]\d{2})-([0-2]\d)-([0-2]\d) ([0-2]\d):([0-5]\d)$")]),
        Param('event_end_time', JSON, str,
              rules=[Pattern(r"^([2][0]\d{2})-([0-2]\d)-([0-2]\d) ([0-2]\d):([0-5]\d)$")]),

        # 각 기획전 타입 필수값 여부는 function 내부에서 확인
        Param('short_description', JSON, str, required=False,
              rules=[MaxLength(45)]),
        Param('long_description', JSON, str, required=False),
        Param('banner_image_url', JSON, str, required=False,
              rules=[Pattern(r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")]),
        Param('banner_image_url', JSON, str, required=False,
              rules=[MaxLength(200)]),
        Param('detail_image_url', JSON, str, required=False,
              rules=[Pattern(r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")]),
        Param('detail_image_url', JSON, str, required=False,
              rules=[MaxLength(200)]),
        Param('button_name', JSON, str, required=False,
              rules=[MaxLength(10)]),
        Param('button_link_type_id', JSON, str, required=False,
              rules=[Pattern(r"^[1-6]{1}$")]),
        Param('button_link_description', JSON, str, required=False,
              rules=[MaxLength(45)]),
        Param('product', JSON, list, required=False),
        Param('youtube_url', JSON, str, required=False,
              rules=[Pattern(r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")]),
        Param('youtube_url', JSON, str, required=False,
              rules=[MaxLength(200)])
    )
    def register_event_info(*args):
        """ 기획전 등록 엔드포인트

        기획전을 신규 등록하는 엔드포인트 입니다.
        request.body 로 등록 정보를 받고, 유효성을 확인합니다.
        기획전 전 타입 공통 필수 파라미터는 먼저 확인하고,
        각 타입별 필수 파라미터는 function 내에서 확인합니다.

        확인이 끝나면 event_info 에 모든 파라미터를 저장합니다.
        등록을 수행하는 계정의 정보를 데코레이터에서 받아와 event_info 에 저장합니다.

        function 진입 후 마스터 권한이 없으면 에러를 리턴하고,
        마스터 권한이면 서비스로 값을 넘깁니다.

        Args:
            *args: 유효성 검사를 통과한 파라미터

        request.body:
            event_type_id 기획전 타입 외래키
            event_sort_id 기획전 종류 외래키
            is_on_main 메인 노출여부
            is_on_event 기획전 진열여부
            name 기획전명
            event_start_time 기획전 시작시간 (ex) 2020-04-10 23:59
            event_end_time 기획전 종료시간
            short_description 기획전 간략설명
            long_description 기획전 상세설명
            banner_image_url 배너 이미지 url
            detail_image_url 상세 이미지 url
            button_name 이벤트 버튼 이름
            button_link_type_id 이벤트 버튼 링크타입 외래키
            button_link_description 이벤트 버튼링크 내용
            product_order 상품 진열 순서
            product_id 상품 외래키
            youtube_url 유튜브 url

        Returns: http 응답코드
            200: SUCCESS 기획전 신규 등록 완료
            400: NO_SHORT_DESCRIPTION, BANNER_IMAGE_URL, NO_DETAIL_IMAGE_URL,
                 NO_BUTTON_NAME, NO_BUTTON_LINK_DESCRIPTION, INVALID_EVENT_SORT
            403: NO_AUTHORIZATION
            500: NO_DATABASE_CONNECTION

        Authors:
            leejm3@brandi.co.kr (이종민)
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-07 (leejm3@brandi.co.kr): 초기생성 / 이벤트 기획전 부분 작성
            2020-04-08 (leejm3@brandi.co.kr): 기획전 기간 밸리데이션 추가
            2020-04-10 (yoonhc@brandi.co.kr): 상품(이미지), 상품(텍스트), 유튜브 기획전 작성

        """

        if g.account_info['auth_type_id'] != 1:
            return jsonify({'message': 'NO_AUTHORIZATION'}), 403

        # validation(형식) 확인된 데이터 저장
        event_info = {
            'event_type_id': args[0],
            'event_sort_id': args[1],
            'is_on_main': args[2],
            'is_on_event': args[3],
            'name': args[4],
            'event_start_time': args[5],
            'event_end_time': args[6],
            'short_description': args[7],
            'long_description': args[8],
            'banner_image_url': args[9],
            'detail_image_url': args[11],
            'button_name': args[13],
            'button_link_type_id': args[14],
            'button_link_description': args[15],
            'youtube_url': args[17],
            'auth_type_id': g.account_info['auth_type_id'],
            'account_no': g.account_info['account_no']
            }

        # 이벤트 상품을 service로 넘길 변수에 담아준다. None이 들어와도 일단 넘긴다.
        event_product_info = args[16]

        # 기획전 기간 밸리데이션
        now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M')

        # 시작시간이 현재 시간보다 전이거나 시작시간이 종료시간보다 늦으면 에러 반환
        if event_info['event_start_time'] < now or event_info['event_start_time'] > event_info['event_end_time']:
            return jsonify({'message': 'INVALID_EVENT_TIME'}), 400

        # 기획전 타입이 이벤트일 경우 필수값 확인
        if event_info['event_type_id'] == "1":
            if not event_info['short_description']:
                return jsonify({'message': 'NO_SHORT_DESCRIPTION'}), 400

            if not event_info['banner_image_url']:
                return jsonify({'message': 'BANNER_IMAGE_URL'}), 400

            if not event_info['detail_image_url']:
                return jsonify({'message': 'NO_DETAIL_IMAGE_URL'}), 400

            if event_info['event_sort_id'] not in range(1, 3):
                return jsonify({'message': 'INVALID_EVENT_SORT'}), 400

        # 기획전 타입이 쿠폰일 경우 필수값 확인
        if event_info['event_type_id'] == "2":
            if not event_info['short_description']:
                return jsonify({'message': 'NO_SHORT_DESCRIPTION'}), 400

            if event_info['event_sort_id'] not in range(3, 9):
                return jsonify({'message': 'INVALID_EVENT_SORT'}), 400

        # 기획전 타입이 상품(이미지)일 경우 필수값 확인
        if event_info['event_type_id'] == "3":
            if not event_info['banner_image_url']:
                return jsonify({'message': 'MISSING_BANNER_IMAGE'}), 400

            if not event_info['detail_image_url']:
                return jsonify({'message': 'MISSING_DETAIL_IMAGE'}), 400
            
            if event_info['event_sort_id'] not in range(9,11):
                return jsonify({'message': 'INVALID_EVENT_SORT'}), 400

        # 기획전 타입이 상품(텍스트)일 경우 필수값 확인
        if event_info['event_type_id'] == "4":
            if not event_info['short_description']:
                return jsonify({'message': 'MISSING_SHORT_DESC'}), 400

            if not event_info['banner_image_url']:
                return jsonify({'message': 'MISSING_BANNER_IMAGE'}), 400

        # 기획전 타입이 유튜브일 경우 필수값 확인
        if event_info['event_type_id'] == "5":
            if not event_info['short_description']:
                return jsonify({'message': 'MISSING_SHORT_DESC'}), 400

            if not event_info['banner_image_url']:
                return jsonify({'message': 'MISSING_BANNER_IMAGE'}), 400

            if not event_info['youtube_url']:
                return jsonify({'message': 'MISSING_YOUTUBE_URL'}), 400

        # 입력 인자 관계에 따른 필수값 확인
        if event_info['button_link_type_id']:
            if not event_info['button_name']:
                return jsonify({'message': 'NO_BUTTON_NAME'}), 400

            if event_info['button_link_type_id'] in range(4, 7):
                if not event_info['button_link_description']:
                    return jsonify({'message': 'NO_BUTTON_LINK_DESCRIPTION'}), 400

        # 데이터베이스 연결
        db_connection = get_db_connection()
        if db_connection:
            try:
                event_service = EventService()

                registering_event_result = event_service.register_event(event_info, db_connection, event_product_info)
                return registering_event_result

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()
                except Exception as e:
                    return jsonify({'message': f'{e}'}), 400
        else:
            return jsonify({'view_message': 'NO_DATABASE_CONNECTION'}), 500

    @event_app.route("/type", methods=["GET"])
    @login_required
    def get_event_types():

        """ 기획전 타입 표출 엔드포인트

        기획전 타입 표출 엔드포인트 입니다.
        기획전 등록페이지에서 기획전 타입 목록을 표출할때 사용됩니다.

        Returns:
            200: 기획전 타입 목록
            500: DB_CURSOR_ERROR, INVALID_KEY, NO_DATABASE_CONNECTION

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-09 (leejm3@brandi.co.kr): 초기 생성

        """

        db_connection = get_db_connection()
        if db_connection:
            try:
                event_service = EventService()
                types = event_service.get_event_types(db_connection)

                return types

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()

                except Exception as e:
                    return jsonify({'message': f'{e}'}), 400
        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

    @event_app.route("/type/<int:event_type_id>", methods=["GET"], endpoint='get_event_sorts')
    @login_required
    @validate_params(
        Param('event_type_id', PATH, str,
              rules=[Pattern(r"^[1-5]{1}$")])
    )
    def get_event_sorts(*args):

        """ 기획전 타입별 종류 표출 엔드포인트

        기획전 타입별 종류 표출 엔드포인트 입니다.
        기획전 등록페이지에서 기획전 타입 별 목록을 표출할때 사됩니다.

        Args:
            *args: 유효성 검사를 통과한 파라미터

        url Parameter:
            event_type_id: 기획전 타입 아이디

        Returns:
            200: 기획전 타입별 종류 목록
            500: DB_CURSOR_ERROR, INVALID_KEY, NO_DATABASE_CONNECTION

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-09 (leejm3@brandi.co.kr): 초기 생성

        """

        # event_type_id 저장
        event_type_info = {"event_type_id": args[0]}

        db_connection = get_db_connection()
        if db_connection:
            try:
                event_service = EventService()
                sorts = event_service.get_event_sorts(event_type_info, db_connection)

                return sorts

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()

                except Exception as e:
                    return jsonify({'message': f'{e}'}), 400
        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

    @event_app.route("/<int:event_no>", methods=["GET"], endpoint='get_event_infos')
    @login_required
    def get_event_infos(event_no):

        """ 기획전 정보 표출 엔드포인트

        기획전 정보 표출 엔드포인트 입니다.
        url parameter 로 받은 기획전 번호에 해당하는 정보를 표출합니다.

        Args:
            event_no: 기획전 번호

        Returns:
            200: 기획전 정보
            400: INVALID_EVENT_NO
            500: DB_CURSOR_ERROR, INVALID_KEY, NO_DATABASE_CONNECTION

        Authors:
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-10 (leejm3@brandi.co.kr): 초기 생성

        """

        # 마스터 권한이 아니면 반려
        if g.account_info['auth_type_id'] != 1:
            return jsonify({'message': 'NO_AUTHORIZATION'}), 403

        db_connection = get_db_connection()
        if db_connection:
            try:
                event_service = EventService()
                info = event_service.get_event_infos(event_no, db_connection)

                return info

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()

                except Exception as e:
                    return jsonify({'message': f'{e}'}), 400
        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500
