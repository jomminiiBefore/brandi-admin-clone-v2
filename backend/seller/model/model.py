import mysql.connector
from flask import jsonify, abort
from mysql.connector.errors import ProgrammingError


class SellerDao:
    """ 셀러 모델

    :authors:
        leesh3@brandi.co.kr (이소헌)
    :history:
        2020-03-25 (leesh3@brandi.co.kr): 초기 생성
    """

    def __init__(self, db_connection):
        self.db_connection = db_connection

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

        db_cursor = self.db_connection.cursor(buffered = True, dictionary = True)
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
            return jsonify({'message' : 'success'}), 200

        
        except KeyError:
            return jsonify({'message': 'INVALID_KEY'}), 400
        
        except ProgrammingError:
            return jsonify({'message': 'PRGRAMMING_ERROR'}), 400
        
        except AttributeError:
            self.db_connection.rollback()
            return jsonify({'message': 'ATTRIBUTE_ERROR'}), 400
        
        finally:
            db_cursor.close()
    
    def select_seller_info(self):
        db_cursor = self.db_connection.cursor(buffered=True, dictionary=True)
        try:
            seler_info = ("""
                    SELECT * FROM sellers
            """)
            db_cursor.execute(seler_info)
            result = db_cursor.fetchmany(size=3)
            return jsonify({'result' : result}), 200
        
        except :
            pass




            
