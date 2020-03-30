from flask import jsonify
from datetime import datetime, timedelta

class SellerDao:

    """ 셀러 모델

    Authors:
        leesh3@brandi.co.kr (이소헌)
    History:
        2020-03-25 (leesh3@brandi.co.kr): 초기 생성
    """

    def insert_seller(self, new_seller, db_connection):

        """ 신규 셀러 계정 INSERT INTO DB

        입력된 인자가 새로운 셀러로 가입됩니다.
        가입된 셀러의 매니저 인포도 동시에 저장됩니다.
        셀러 인포와 매니저 인포가 모두 정상 저장되어야만 계정 저장이 완료됩니다.

        Args:
            new_seller(dictionary): 신규 가입 셀러
            others(param type):description

        Returns: http 응답코드
            200: 신규 셀러 계정 저장 완료
            400: key error
            500: server error

        Authors:
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-03-25 (leesh3@brandi.co.kr): 초기 생성
        """
        db_cursor = db_connection.cursor(buffered=True, dictionary=True)
        try:
            new_seller_info_data = {
                'name_kr': new_seller['name_kr'],
                'name_en': new_seller['name_en'],
                'site_url': new_seller['site_url'],
                'center_number': new_seller['center_number']
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
                INSERT INTO seller_infos (
                name_kr,
                name_en,
                site_url,
                center_number
            ) VALUES (
                %(name_kr)s,
                %(name_en)s,
                %(site_url)s,
                %(center_number)s
            )""")

            db_cursor.execute(insert_seller_info_statement, new_seller_info_data)

            new_manager_info_data['seller_id'] = db_cursor.lastrowid
            print(db_cursor.lastrowid)
            print(new_manager_info_data)
            # manager_infos 테이블 INSERT INTO
            insert_manager_info_statement = ("""
                INSERT INTO manager_infos (
                contact_number,
                is_deleted,
                seller_id
            ) VALUES (
                %(contact_number)s,
                %(is_deleted)s,
                %(seller_id)s
            )""")

            db_cursor.execute(insert_manager_info_statement, new_manager_info_data)

            db_connection.commit()
            return jsonify({'message': 'SUCCESS'}), 200

        except KeyError as e:
            print(f'KEY_ERROR WITH {e}')
            db_connection.rollback()
            return jsonify({'message': 'INVALID_KEY'}), 400

        finally:
            db_cursor.close()

    def select_seller_info(self, db_connection):

        """ 가입된 모든 셀러 표출

        Returns:
            200: 가입된 모든 셀러 세부 정보

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-03-27 (yoonhc@brandi.co.kr): 초기 생성
        """
        db_cursor = db_connection.cursor(dictionary=True)
        try:
            seller_info = ("""
                    SELECT * FROM seller_infos WHERE seller_info_no=1 
            """)
            db_cursor.execute(seller_info)
            sellers = db_cursor.fetchall()

            for seller in sellers:
                print(seller['weekday_end_time'].days)
                # seller['weekday_end_time'] = seller['weekday_end_time'].days * 24 + seller['weekday_end_time'].hours

            return jsonify(sellers), 200

        except:
            pass

