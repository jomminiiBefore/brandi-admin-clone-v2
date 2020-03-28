class SellerService:

    """
    셀러 서비스
    """
    def __init__(self, seller_dao):
        self.seller_dao = seller_dao

    def create_new_seller(self, new_seller):

        """ 신규 셀러 회원가입

        입력된 인자가 신규 셀러로 가입됩니다.

        Args:
            new_seller: 신규 가입 셀러
            others(param type):description

        Returns: http 응답 코
            200: 신규 셀러 계정 저장 완료
            400: key error
            500: server error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-03-25 (leesh3@brandi.co.kr): 초기 생성
        """
        insert_new_seller = self.seller_dao.insert_seller(new_seller)

        return insert_new_seller

    def get_all_sellers(self):

        """ 가입된 모든 셀러 표출

        가입되어있는 모든 셀러의 세부 정보를 표출합니다.

        Returns:
            200: 가입된 모든 셀러  정보 표출

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
        """
        get_all_sellers = self.seller_dao.select_seller_info()
        return get_all_sellers

