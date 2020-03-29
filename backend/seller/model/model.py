import mysql.connector

from flask import jsonify
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

        # with self.db_connection.cursor(buffered=True, dictionary=True) as db_cursor:
        db_cursor = self.db_connection.cursor(buffered=True, dictionary=True)
        try:
            new_seller_info_data = {
                'name_kr': new_seller['name_kr'],
                'name_en': new_seller['name_en'],
                'site_url': new_seller['site_url'],
                'center_number': new_seller['center_number'],
            }

            new_manager_info_data = {
                'contact_number': new_seller['contact_number'],
                'is_deleted': new_seller['is_deleted']
            }


            # 트랜잭션 시작
            db_cursor.execute("START TRANSACTION")
            # 자동 커밋 비활성화
            db_cursor.execute("SET AUTOCOMMIT=0")


            # seller_infos 테이블 INSERT INTO
            insert_seller_info_statement = ("""
                INSERT INTO seller_infos (name_kr, name_en, site_url, center_number)
                VALUES (%(name_kr)s, %(name_en)s, %(site_url)s, %(center_number)s)
            """)

            db_cursor.execute(insert_seller_info_statement, new_seller_info_data)

            new_manager_info_data['seller_id'] = db_cursor.lastrowid
            print(db_cursor.lastrowid)
            print(new_manager_info_data)
            # manager_infos 테이블 INSERT INTO
            insert_manager_info_statement = ("""
                INSERT INTO manager_infos (contact_number, is_deleted, seller_id)
                VALUES (%(contact_number)s, %(is_deleted)s, %(seller_id)s)
            """)

            db_cursor.execute(insert_manager_info_statement, new_manager_info_data)

            self.db_connection.commit()
            return jsonify({'message' : 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            self.db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 400
        
        except ProgrammingError:
            self.db_connection.rollback()
            return jsonify({'message': 'PROGRAMMING_ERROR'}), 400
        
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
