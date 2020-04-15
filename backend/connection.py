import pymysql
import mysql.connector
import boto3

from flask import jsonify

from mysql.connector.errors import InterfaceError, ProgrammingError, NotSupportedError
from config import DATABASES, S3_CONFIG


def get_s3_connection():

    """ s3와 커넥션을 만들어주는 함수

    import 되어서 사용될 때 마다 하나의 s3 커넥션이 생긴다

    Returns:
        s3_connection 객체

    Authors:
        yoonhc@brandi.co.kr (윤희철)

    History:
        2020-04-01 (yoonhc@brandi.co.kr): 초기 생성
    """
    s3_connection = boto3.client(
        's3',
        aws_access_key_id=S3_CONFIG['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=S3_CONFIG['AWS_SECRET_ACCESS_KEY'],
        region_name=S3_CONFIG['REGION_NAME'],
    )
    return s3_connection


class DatabaseConnection:

    def __init__(self):

        """ 데이터베이스 커넥션을 만들어주는 클래스.

        import 되어서 사용될 때 마다 하나의 데이터베이스 커넥션이 생긴다.
        하나의 요청에 하나의 커넥션이라는 독립성을 지켜주기 위해서 connection 은 요청이 들어올 때 마다 만들어준다.

        Returns:
            database connection 객체

        Authors:
            yoonhc@brandi.co.kr (윤희철)
            leesh3@brandi.co.kr (이소헌)

        History:
            2020-03-30 (yoonhc@brandi.co.kr): 초기 생성
            2020-04-01 (leesh3@brandi.co.kr): 클래스화

        """
        self.db_config = {
            'database': DATABASES['database'],
            'user': DATABASES['user'],
            'password': DATABASES['password'],
            'host': DATABASES['host'],
            'port': DATABASES['port'],
            'charset': DATABASES['charset'],
            'collation': DATABASES['collation'],
        }
        try:
            self.db_connection = mysql.connector.connect(**self.db_config)

        except InterfaceError as e:
            print(f'INTERFACE_ERROR_WITH {e}')

        except ProgrammingError as e:
            print(f'PROGRAMMING_ERROR_WITH {e}')

        except NotSupportedError as e:
            print(f'NOT_SUPPORTED_ERROR_WITH {e}')

    def __enter__(self):
        try:
            self.cursor = self.db_connection.cursor(buffered=True, dictionary=True)
            return self.cursor

        except AttributeError as e:
            print(e)
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

    def __exit__(self, exc_type, exc_value, exc_trance):
        try:
            self.cursor.close()
        except AttributeError as e:
            print(e)
            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 500

    def close(self):
        return self.db_connection.close()

    def commit(self):
        return self.db_connection.commit()

    def rollback(self):
        return self.db_connection.rollback()


def get_db_connection():
    """ 데이터베이스 커넥션 생성

    import 되어서 사용될 때 마다 하나의 데이터베이스 커넥션이 생성

    Returns:
        database connection 객체

    Authors:
        leesh3@brandi.co.kr (이소헌)

    History:
        2020-04-03 (leesh3@brandi.co.kr): 초기 생성

    """
    db_config = {
        'database': DATABASES['database'],
        'user': DATABASES['user'],
        'password': DATABASES['password'],
        'host': DATABASES['host'],
        'port': DATABASES['port'],
        'charset': DATABASES['charset'],
        'cursorclass': pymysql.cursors.DictCursor,
    }
    db = pymysql.connect(**db_config)
    return db
