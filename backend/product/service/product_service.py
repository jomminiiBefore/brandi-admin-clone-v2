from flask import jsonify, g
from product.model.product_dao import ProductDao


class ProductService:

    """
    상품 서비스
    """
    # noinspection PyMethodMayBeStatic
    def get_first_categories(self, account_info, db_connection):

        """ 상품 1차 카테고리 목록 표출

        seller마다 다른 product_type을 기준으로 1차 상품 카테고리를 표출

        Args:
            account_info: 상품 등록시 상품 소유 셀러
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 셀러에 따른 상품 1차 카테고리 목록

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성
        """
        product_dao = ProductDao()
        auth_type_id = g.account_info['auth_type_id']
        # 상품을 등록하는 주체가 마스터이면, query string 에 담긴 셀러 어카운트 넘버로 셀러 선택해서 카테고리 탐색
        if auth_type_id == 1:
            account_no = account_info['account_no']
        # 상품을 등록하는 주체가 셀러이면, 자기 토큰을 이용해 카테고리 탐색
        elif auth_type_id == 2:
            account_no = g.account_info['account_no']

        categories = product_dao.get_first_categories(account_no, db_connection)

        return categories

    # noinspection PyMethodMayBeStatic
    def get_second_categories(self, db_connection, first_category_no):

        """ 상품 2차 카테고리 목록 표출

        선택된 상품 1차 카테고릭에 따라 해당하는 2차카테고리 목록 표출

        Args:
            first_category_no(integer): 1차 카테고리 인덱스 번호
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 1차 카테고리에 해당하는 상품 2차 카테고리 목록

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성

        """
        product_dao = ProductDao()
        categories = product_dao.get_second_categories(db_connection, first_category_no)

        return categories

    # noinspection PyMethodMayBeStatic
    def get_product_detail(self, product_no, db_connection):

        """ 상품 등록/수정시 나타나는 개별 상품의 기존 정보 표출

        상품의 번호를 받아 해당하는 상품의 상세 정보를 표출.

        Args:
            product_no(integer): 동일 상품 변경 이력의 가장 최신 버전 인덱스 번호
            db_connection(DatabaseConnection): 데이터베이스 커넥션 객체

        Returns:
            200: 상품별 상세 정보

        Authors:

            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-03 (leesh3@brandi.co.kr): 초기 생성

        """

        product_dao = ProductDao()
        product_infos = product_dao.get_product_detail(product_no, db_connection)

        return product_infos

    # noinspection PyMethodMayBeStatic
    def insert_new_product(self, product_info, db_connection):

        """ 신규 상품 등록

        등록하려는 셀러의 정보에 따라 내부 내용이 달라지므로, 데코레이터에서 셀러 정보를 먼저 읽어옴.
        등록 상세 정보는 request.body 내부에 존재함.
        유효성 검사를 위한 조건 통과 후 product_info 변수에 내용을 담아 product_service로 전달.

        Args:
            product_info: 등록하려는 신규 상품 정보
            db_connection: 데이터베이스 커넥션 객체

        Returns: Http 응답코드
            200: 신규 상품 등록 성공

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-06 (leesh3@brandi.co.kr): 초기 생성
        """
        product_dao = ProductDao()
        auth_type = product_info['auth_type_id']

        if auth_type == 1:
            insert_new_product_result = product_dao.insert_new_product(product_info, db_connection)

            return insert_new_product_result

        elif auth_type == 2:
            if product_info['account_no'] == product_info['selected_account_no']:
                insert_new_product_result = product_dao.insert_new_product(product_info, db_connection)
                return insert_new_product_result

            return jsonify({'message': 'NO_AUTHORIZATION'}), 403

        return jsonify({'message': 'INVALID_AUTH_ID'}), 400

    # noinspection PyMethodMayBeStatic
    def update_product_info(self, product_info, db_connection):

        """ 상품 정보 수

        등록하려는 셀러의 정보에 따라 내부 내용이 달라지므로, 데코레이터에서 셀러 정보를 먼저 읽어옴.
        상세 수정 정보는 request.body 내부에 존재함.

        Args:
            product_info: 상품 수정 정보
            db_connection: 데이터베이스 커넥션 객체

        Returns: Http 응답코드
            200: 상품 정보 수정 완료

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-08 (leesh3@brandi.co.kr): 초기 생성
        """

        product_dao = ProductDao()
        auth_type = product_info['auth_type_id']
        if auth_type == 1:
            update_product_result = product_dao.update_product_info(product_info, db_connection)

            return update_product_result

        elif auth_type == 2:
            if product_info['token_account_no'] == product_info['seller_account_id']:
                update_product_result = product_dao.update_product_info(product_info, db_connection)
                return update_product_result

            return jsonify({'message': 'NO_AUTHORIZATION'}), 403

        return jsonify({'message': 'INVALID_AUTH_ID'}), 400

    # noinspection PyMethodMayBeStatic
    def get_color_filters(self, db_connection):

        """ 상품 등록시 컬러 필터 표출

        Args:
            db_connection: 데이터베이스 연결 객체

        Returns:
            200: 상품 등록시 선택할 수 있는 색상 필터

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-09 (leesh3@brandi.co.kr): 초기 생성
        """
        product_dao = ProductDao()
        return product_dao.get_color_filters(db_connection)
