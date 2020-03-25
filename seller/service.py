from flask  import request, jsonify

class SellerService():
    """
    클래스 설명
    만든 사람
    언제 만들어졌는지 (처음 작성 시작한 때)
    """
    def __init__(self, SellerDao):
        """함수 한 줄 설명 (기능에 대해)

        어떤 기능이 변경 되었고, 필수 요소는 무엇인지    
        파라미터에 대한 설명
        SellerDao: (타입, 설명)
        """

        self.SellerDao = SellerDao

    def create_seller(self, new_seller):
        add_new_seller  = self.SellerDao.create_seller(new_seller)
        return add_new_seller
        