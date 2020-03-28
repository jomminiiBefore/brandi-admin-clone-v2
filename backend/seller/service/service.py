class SellerService:
    def __init__(self, seller_dao):
        self.seller_dao = seller_dao

    def create_new_seller(self, new_seller):

        """ 신규 셀러 생성

        입력된 인자가 신규 셀러로 가입됩니다.

        :param new_seller:
            신규 가입 셀러
        :return:
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
        """가입된 모든 셀러 표출
        :return:
            200: 가입된 모든 셀러 및 셀러 세부 정보 표출

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
        """
        get_all_sellers = self.seller_dao.select_seller_info()
        return get_all_sellers

