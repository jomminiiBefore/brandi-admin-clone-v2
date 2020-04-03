from flask import jsonify, g

from product.model.product_dao import ProductDao


class ProductService:

    """
    상품 서비스
    """
    def get_first_categories(self, db_connection):

        """ 상품 1차 카테고리 목록 표출

        seller마다 다른 product_type을 기준으로 1차 상품 카테고리를 표출

        Args:
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 셀러에 따른 상품 1차 카테고리 목록

        Authors:

            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성

        """
        product_dao = ProductDao()
        account_no = g.account_info['account_no']
        categories = product_dao.get_first_categories(account_no, db_connection)

        return categories

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
