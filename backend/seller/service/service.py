class SellerService:
    def __init__(self, seller_dao):
        self.seller_dao = seller_dao

    def create_new_seller(self, new_seller):

        """ 신규 셀러 생성

        입력된 인자가 신규 셀러로 가입됩니다.

        :param new_seller:
            신규 가입 셀러
        :return:
            신규 셀러 생성
        :authors:
            leesh3@brandi.co.kr (이소헌)
        :history:
            2020-03-25 (leesh3@brandi.co.kr): 초기 생성
        """

        insert_new_seller = self.seller_dao.insert_seller(new_seller)

        return insert_new_seller

    def get_all_sellers(self):
        get_all_sellers = self.seller_dao.select_seller_info()
        return get_all_sellers

