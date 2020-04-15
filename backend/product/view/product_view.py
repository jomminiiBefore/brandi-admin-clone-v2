import json

from flask import request, Blueprint, jsonify, g
from flask_request_validator import (
    GET,
    FORM,
    PATH,
    Param,
    Pattern,
    validate_params
)
from product.service.product_service import ProductService
from connection import get_db_connection, DatabaseConnection
from utils import login_required, ImageUpload


class ProductView:
    """
    프로덕트 뷰
    """
    product_app = Blueprint('product_app', __name__, url_prefix='/product')

    @product_app.route('', methods=['GET'], endpoint='get_product_list')
    @login_required
    @validate_params(
        Param('period_start', GET, str, required=False,
              rules=[Pattern(r"^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])$")]),
        Param('period_end', GET, str, required=False,
              rules=[Pattern(r"^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])$")]),
        Param('seller_name', GET, str, required=False),
        Param('product_name', GET, str, required=False),
        Param('product_number', GET, int, required=False),

        # 셀러 속성은 다중 값이 들어올 수 있어서 리스트로 받음
        Param('seller_type_id', GET, list, required=False),
        Param('is_available', GET, int, required=False),
        Param('is_on_display', GET, int, required=False),
        Param('is_on_discount', GET, int, required=False),
        Param('offset', GET, int),
        Param('limit', GET, int),
        Param('is_available', GET, str, required=False,
              rules=[Pattern(r"^[0-1]{1}$")]),
        Param('is_on_display', GET, str, required=False,
              rules=[Pattern(r"^[0-1]{1}$")]),
        Param('is_on_discount', GET, str, required=False,
              rules=[Pattern(r"^[0-1]{1}$")])
    )
    def get_product_list(*args):

        """ 상품 리스트 표출 엔드포인트

        상품 관리 페이지에서 표출되는 필터링된 상품 리스트를 표출합니다.
        쿼리 파라미터로 필터링에 사용할 파라미터 값을 받습니다.

        Returns:
            200: 상품 리스트
            403: NO_AUTHORIZATION
            500: NO_DATABASE_CONNECTION, DB_CURSOR_ERROR
                 NO_DATABASE_CONNECTION

        Authors:
            kimsj5@barndi.co.kr (김승준)
            leejm3@brandi.co.kr (이종민)

        History:
            2020-04-09 (kimsj5@brandi.co.kr): 초기 생성
            2020-04-13 (leejm3@brandi.co.kr): 수정
                - 주석 내용 보완
                - 쿼리파라미터 유효성 검사 추가
                - 마스터 권한이 아니면 접근 불가 처리(NO_AUTHORIZATION)
                - db connection try/except 추가
                - 셀러속성 쿼리 값을 리스트 형태로 받도록 변경
        """

        if g.account_info['auth_type_id'] != 1:
            return jsonify({'message': 'NO_AUTHORIZATION'}), 403

        # 유효성 확인 위해 기간 데이터 먼저 정의
        period_start, period_end = args[0], args[1]

        # 두 값이 모두 들어왔을 때, 시작 기간이 종료 기간보다 늦으면 시작기간 = 종료기간
        if period_start and period_end:
            if period_end < period_start:
                period_start = period_end

        # 두 값이 각각 안들어왔을 경우 default 값 설정
        if not period_start:
            period_start = '2016-07-01'

        if not period_end:
            period_end = '2037-12-31'

        # seller_type_id 보정
        seller_type_id = args[5]
        if seller_type_id:
            seller_type_id.append(0)

        # 유효성 검사를 통과한 쿼리 값을 filter_info 에저장
        filter_info = {
            # '2020-04-14' 형식으로 들어오는 기간 데이터 변환
            'period_start': period_start + ' 00:00:00',
            'period_end': period_end + ' 23:59:59',
            'seller_name': args[2],
            'product_name': args[3],
            'product_number': args[4],
            'seller_type_id': seller_type_id,
            'is_available': args[6],
            'is_on_display': args[7],
            'is_on_discount': args[8],
            'offset': args[9],
            'limit': args[10]
        }

        # offset 과 limit 에 음수가 들어오면 default 값 지정
        if filter_info['offset'] < 0:
            filter_info['offset'] = 0

        if filter_info['limit'] < 0:
            filter_info['limit'] = 10

        try:
            db_connection = get_db_connection()
            if db_connection:
                product_service = ProductService()
                product_list_result = product_service.get_product_list(filter_info, db_connection)
                return product_list_result
            else:
                return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

        finally:
            try:
                db_connection.close()
            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

    @product_app.route("/<int:product_no>", methods=["GET"], endpoint='get_product_detail')
    @login_required
    @validate_params(Param('product_no', PATH, int))
    def get_product_detail(product_no):

        """ 상품 등록/수정시 나타나는 개별 상품의 기존 정보 표출 엔드포인트

        상품의 번호를 path parameter 로 받아 해당하는 상품의 기존 상세 정보를 표출.

        Args:
            product_no(integer): 상품 id

        Returns:
            200: 상품별 상세 정보
            500: 데이터베이스 에러

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-03 (leesh3@brandi.co.kr): 초기 생성
            2020-04-07 (leesh3@brandi.co.kr): 파라미터 변수를 product_info_no -> product_no로 변경
        """

        try:
            db_connection = get_db_connection()
            if db_connection:
                product_service = ProductService()
                product_infos = product_service.get_product_detail(product_no, db_connection)
                return product_infos
            else:
                return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message': f'{e}'}), 500

        finally:
            try:
                db_connection.close()
            except Exception as e:
                return jsonify({'message': f'{e}'}), 500

    @product_app.route("/category", methods=["GET"])
    @login_required
    @validate_params(
        Param('account_no', GET, int, required=False)
    )
    def get_first_categories(*args):

        """ 상품 분류별 1차 카테고리 표출 엔드포인트

        Returns:
            200: 셀러가 속한 상품 분류에 따른 1차 카테고리
            400: 데이터베이스 연결 에러
            500: server error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성
            2020-04-13 (leesh3@brandi.co.kr): 셀러 정보 얻어오는 경로를 token 내부 데이터에서 query string 으로 변경
        """
        account_info = {
            'account_no': args[0]
        }

        try:
            db_connection = get_db_connection()
            if db_connection:
                product_service = ProductService()
                categories = product_service.get_first_categories(account_info, db_connection)
                return categories
            else:
                return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

        finally:
            try:
                db_connection.close()
            except Exception as e:
                return jsonify({'message': f'{e}'}), 400


    @product_app.route(
        "/category/<int:first_category_no>",
        methods=["GET"], endpoint='get_second_categories')
    @login_required
    @validate_params(
        Param('first_category_no', PATH, int),

        # 유효한 카테고리 범위 벗어날 시 에러 반환
        Param('first_category_no', PATH, str,
              rules=[Pattern(r'^([0-9]|[0-3][0-9])$')]),
    )
    def get_second_categories(*args):

        """ 상품 2차 카테고리 목록 표출

        선택된 상품 1차 카테고릭에 따라 해당하는 2차카테고리 목록 표출

        Args:
            *args:
                first_category_no(integer): 1차 카테고리 인덱스 번호

        Returns:
            200: 1차 카테고리에 해당하는 2차 카테고리 목록
            400: 데이터베이스 연결 에러
            500: server error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성
            2020-04-07 (leesh3@brandi.co.kr): URL 구조 변경
        """
        first_category_no = args[0]
        db_connection = get_db_connection()

        try:
            if db_connection:
                product_service = ProductService()
                categories = product_service.get_second_categories(db_connection, first_category_no)
                return categories
            else:
                return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400

        except Exception as e:
            return jsonify({'message': f'{e}'}), 400

        finally:
            try:
                db_connection.close()
            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

    @product_app.route("/color", methods=["GET"])
    def get_color_filters():

        """ 상품 등록시 컬러 필터 표출 엔드포인트

        Returns:
            200: 상품 등록시 선택할 수 있는 색상 필터
            500: 데이터 베이스 에러

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-09 (leesh3@brandi.co.kr): 초기 생성
        """
        try:
            db_connection = get_db_connection()
            if db_connection:
                product_service = ProductService()
                get_color_result = product_service.get_color_filters(db_connection)
                return get_color_result
            else:
                return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message': f'{e}'}), 500

        finally:
            try:
                db_connection.close()
            except Exception as e:
                return jsonify({'message': f'{e}'}), 500

    @product_app.route('', methods=['POST'], endpoint='insert_new_product')
    @login_required
    @validate_params(
        Param('is_available', FORM, int),
        Param('is_on_display', FORM, int),
        Param('first_category_id', FORM, int),
        Param('second_category_id', FORM, int, required=False),
        Param('name', FORM, str,
              rules=[Pattern(r"[^\"\']")]),
        Param('short_description', FORM, str, required=False),
        Param('color_filter_id', FORM, int),
        Param('style_filter_id', FORM, int),
        Param('long_description', FORM, str),
        Param('youtube_url', FORM, str, required=False),
        Param('stock', FORM, int),
        Param('price', FORM, int),
        Param('discount_rate', FORM, float),
        Param('discount_start_time', FORM, str, required=False),
        Param('discount_end_time', FORM, str, required=False),
        Param('min_unit', FORM, int),
        Param('max_unit', FORM, int),
        Param('tags', FORM, str, required=False),
        Param('selected_account_no', FORM, int, required=False),

        # integer parameter 범위 지정을 위한 검증
        Param('is_available', FORM, str,
              rules=[Pattern(r'^([0-1])$')]),
        Param('is_on_display', FORM, str,
              rules=[Pattern(r'^([0-1])$')]),
        Param('first_category_id', FORM, str,
              rules=[Pattern(r'^([0-9]|[1][0-1])$')]),
        Param('second_category_id', FORM, str,
              rules=[Pattern(r'^([0-9]|[0-9][0-9]|[1][0][0-9]|[1][1][0-4])$')]),
    )
    def insert_new_product(*args):
        """ 상품 등록 엔드포인트

        새로운 상품을 등록하는 엔드포인트.
        등록하려는 셀러의 정보에 따라 내부 내용이 달라지므로, 데코레이터에서 셀러 정보를 먼저 읽어옴.
        등록 상세 정보는 request.body 내부에 존재함.
        유효성 검사를 위한 조건 통과 후 product_info 변수에 내용을 담아 product_service로 전달.

        Args:
            *args: 등록할 제품의 상세 정보

        g.account_info: 데코레이터에서 넘겨받은 수정을 수행하는 계정 정보
            auth_type_id: 계정의 권한정보
            account_no: 데코레이터에서 확인된 계정번호

        Returns: Http 응답코드
            200: 신규 상품 등록 성공
            500: 데이터베이스 에

        Authors:
            leesh3@brandi.co.kr (이소헌)
            
        History:
            2020-04-06 (leesh3@brandi.co.kr): 초기 생성
            2020-04-14 (leesh3@brandi.co.kr): 이미지 순서 문제 캐치
        """
        image_uploader = ImageUpload()
        uploaded_images = image_uploader.upload_product_image(request)
        if (400 in uploaded_images) or (500 in uploaded_images):
            return uploaded_images

        # 상품 등록시 대표 사진인 1번 사진부터 들어와야함
        if not uploaded_images['image_file_1']:
            return jsonify({'message': 'REPRESENTATIVE_IMAGE_DOES_NOT_EXIST'}), 400
        # 1번 사진부터 순서대로 들어와야함
        for i in range(2, 6):
            if uploaded_images[f'image_file_{i}']:
                if not uploaded_images[f'image_file_{i-1}']:
                    return jsonify({'message': 'IMAGES_SHOULD_BE_IN_ORDER'}), 400

        product_info = {
            'auth_type_id': g.account_info['auth_type_id'],
            'account_no': g.account_info['account_no'],
            'uploader': g.account_info['account_no'],
            'modifier': g.account_info['account_no'],
            'is_available': args[0],
            'is_on_display': args[1],
            'first_category_id': args[2],
            'second_category_id': args[3],
            'name': args[4],
            'short_description': args[5],
            'color_filter_id': args[6],
            'style_filter_id': args[7],
            'long_description': args[8],
            'youtube_url': args[9],
            'stock': args[10],
            'price': args[11],
            'discount_rate': args[12]/100,
            'discount_start_time': args[13],
            'discount_end_time': args[14],
            'min_unit': args[15],
            'max_unit': args[16],
            'tags': json.loads(args[17]),
            'selected_account_no': args[18],
            'images': uploaded_images,
        }

        try:
            db_connection = get_db_connection()
            if db_connection:
                product_service = ProductService()
                product_insert_result = product_service.insert_new_product(product_info, db_connection)
                return product_insert_result
            else:
                return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message': f'{e}'}), 500

        finally:
            try:
                db_connection.close()
            except Exception as e:
                return jsonify({'message': f'{e}'}), 500

    @product_app.route("/<int:product_id>", methods=['PUT'], endpoint='update_product_info')
    @login_required
    @validate_params(
        Param('is_available', FORM, int),
        Param('is_on_display', FORM, int),
        Param('product_sort_id', FORM, int),
        Param('first_category_id', FORM, int),
        Param('second_category_id', FORM, int),
        Param('name', FORM, str,
              rules=[Pattern(r"^((?!(?=.*\")(?=.*\')).)*$")]),
        Param('short_description', FORM, str, required=False),
        Param('color_filter_id', FORM, int),
        Param('style_filter_id', FORM, int),
        Param('long_description', FORM, str),
        Param('youtube_url', FORM, str, required=False),
        Param('stock', FORM, int),
        Param('price', FORM, int),
        Param('discount_rate', FORM, float),
        Param('discount_start_time', FORM, str, required=False),
        Param('discount_end_time', FORM, str, required=False),
        Param('min_unit', FORM, int),
        Param('max_unit', FORM, int),
        Param('tags', FORM, str, required=False),
        Param('product_id', PATH, int),
        Param('seller_account_no', FORM, int),
    )
    def update_product_info(*args):

        """ 상품 정보 수정 엔드포인트

        상품의 정보를 수정하는 엔드포인트.
        등록하려는 셀러의 정보에 따라 내부 내용이 달라지므로, 데코레이터에서 셀러 정보를 먼저 읽어옴.
        수정 상세 정보는 request.body 내부에 존재함.
        유효성 검사를 위한 조건 통과 후 product_info 변수에 내용을 담아 product_service로 전달.

        Args:
            *args: 등록할 제품의 상세 정보

        g.account_info: 데코레이터에서 넘겨받은 수정을 수행하는 계정 정보
            auth_type_id: 계정의 권한정보
            account_no: 데코레이터에서 확인된 계정번호

        Returns: Http 응답코드
            200: 상품 정보 수정 성공
            500: 데이터베이스 에러

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-08 (leesh3@brandi.co.kr): 초기 생성
        """

        image_uploader = ImageUpload()
        uploaded_images = image_uploader.upload_product_image(request)

        # 이미지 업로더를 호출한 결과값에 애러코드 400이 포함되어있으면 utils.py에서 발생한 러메세지를 그대로 리턴
        if (400 in uploaded_images) or (500 in uploaded_images):
            return uploaded_images

        product_info = {
            'auth_type_id': g.account_info['auth_type_id'],
            'token_account_no': g.account_info['account_no'],
            'modifier': g.account_info['account_no'],
            'is_available': args[0],
            'is_on_display': args[1],
            'product_sort_id': args[2],
            'first_category_id': args[3],
            'second_category_id': args[4],
            'name': args[5],
            'short_description': args[6],
            'color_filter_id': args[7],
            'style_filter_id': args[8],
            'long_description': args[9],
            'youtube_url': args[10],
            'stock': args[11],
            'price': args[12],
            'discount_rate': args[13]/100,
            'discount_start_time': args[14],
            'discount_end_time': args[15],
            'min_unit': args[16],
            'max_unit': args[17],
            'tags': json.loads(args[18]),
            'product_id': args[19],
            'seller_account_id': args[20],
            'images': uploaded_images,
        }

        try:
            db_connection = get_db_connection()
            if db_connection:
                product_service = ProductService()
                product_update_result = product_service.update_product_info(product_info, db_connection)
                return product_update_result
            else:
                return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

        except Exception as e:
            return jsonify({'message': f'{e}'}), 500

        finally:
            try:
                db_connection.close()
            except Exception as e:
                return jsonify({'message': f'{e}'}), 500
