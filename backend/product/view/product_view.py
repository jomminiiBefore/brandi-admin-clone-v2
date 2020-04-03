from flask import request, Blueprint, jsonify

from product.service.product_service import ProductService
from connection import DatabaseConnection
from utils import login_required


class ProductView():
    """
    프로덕트 뷰
    """
    product_app = Blueprint('product_app', __name__, url_prefix='/product')

    @product_app.route("/first_category", methods=["GET"])
    @login_required
    def get_first_categories():

        """ 상품 분류별 1차 카테고리 표 엔드포인트

        Returns:
            200: 셀러가 속한 상품 분류에 따른 1차 카테고리
            400: 데이터베이스 연결 에러
            500: server error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성

        """

        db_connection = DatabaseConnection()
        if db_connection:
            try:
                product_service = ProductService()
                categories = product_service.get_first_categories(request, db_connection)

                return categories

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()

                except Exception as e:
                    return jsonify({'message': f'{e}'}), 400
        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400

    @product_app.route("/first_category/<int:first_category_no>/second_category", methods=["GET"])
    def get_second_categories(first_category_no):

        """ 상품 2차 카테고리 목록 표출

        선택된 상품 1차 카테고릭에 따라 해당하는 2차카테고리 목록 표출

        Args:
            first_category_no(integer): 1차 카테고리 인덱스 번호

        Returns:
            200: 1차 카테고리에 해당하는 2차 카테고리 목록
            400: 데이터베이스 연결 에러
            500: server error

        Authors:

            leesh3@brandi.co.kr (이소헌)

        History:
            2020-04-02 (leesh3@brandi.co.kr): 초기 생성

        """

        db_connection = DatabaseConnection()
        if db_connection:
            try:
                product_service = ProductService()
                categories = product_service.get_second_categories(request, db_connection, first_category_no)
                return categories

            except Exception as e:
                return jsonify({'message': f'{e}'}), 400

            finally:
                try:
                    db_connection.close()

                except Exception as e:
                    return jsonify({'message': f'{e}'}), 400
        else:
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400
