from flask import request


class SellerService:

    """
    셀러 서비스
    """
    def __init__(self, seller_dao):
        self.seller_dao = seller_dao

    def create_new_seller(self, request, db_connection):
        """ 신규 셀러 회원가입

        인력된 인자가 신규 셀러로 가입됨

        Args:
            request: 신규 가입 셀러 정보가 담긴 요청
            db_connection: 데이터 베이스 커넥션 객체

        Returns: http 응답 코드
            200: 신규 셀러 계정 저장 완료
            400: key error
            500: server error

        Authors:
            leesh3@brandi.co.kr (이소헌)
            yoonhc@barndi.co.kr (윤희철)

        History:
            2020-03-25 (leesh3@brandi.co.kr): 초기 생성
            2020-03-30 (yoonhc@barndi.co.kr): db_connection 인자 추
        """
        new_seller = request.json
        new_seller_result = self.seller_dao.insert_seller(new_seller, db_connection)

        return new_seller_result 

    def get_all_sellers(self, request, db_connection):

        """

        Args:
            request: 회원 조회 GET 요청 및 권한 정보 (authorization)
            db_connection: 데이터베이스 커넥션 객체

        Returns:
            200: 가입된 모든 셀러 정보 표

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
        """

        get_all_sellers = self.seller_dao.select_seller_info(db_connection)
        return get_all_sellers

