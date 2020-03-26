from flask import abort


class SellerDao:
    """ 셀러 모델

    :authors:
        leesh3@brandi.co.kr (이소헌)
    :history:
        2020-03-25 (leesh3@brandi.co.kr): 초기 생
    """

    def __init__(self, database):
        self.db_connection = database.get_connection()
    
    def insert_seller(self, new_seller):

        """ 신규 셀러 계정 INSERT INTO DB성

        :param new_seller: 신규 가입 셀러
        :return:
            신규 셀러 생성
        :authors:
            leesh3@brandi.co.kr (이소헌)
        :history:
            2020-03-25 (leesh3@brandi.co.kr): 초기 생성
        """

        db_cursor = self.db_connection.cursor(buffered=True, dictionary=True)
        try:
            new_seller_data = {
                'name': new_seller['name']
            }

            insert_statement = ("""
                INSERT INTO sellers(name)
                VALUES (%(name)s)
            """)

            db_cursor.execute(insert_statement, new_seller_data)
            self.db_connection.commit()
            db_cursor.close()

        except TypeError:
            abort(400, description='INVALID_VALUE')
