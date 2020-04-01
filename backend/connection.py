from config import DATABASES, S3_CONFIG
import mysql.connector, boto3
# from botocore.client import Config


# make database connection
def get_db_connection():
    """ database connection 생성

    Returns:
        database connection 객체

    Authors:
        yoonhc@brandi.co.kr (윤희철)

    History:
        2020-03-30 (yoonhc@brandi.co.kr): 초기 생성
    """
    db_config = {
        'database': DATABASES['database'],
        'user': DATABASES['user'],
        'password': DATABASES['password'],
        'host': DATABASES['host'],
        'port': DATABASES['port'],
        'charset': DATABASES['charset'],
        'collation': DATABASES['collation'],
    }
    db_connection = mysql.connector.connect(**db_config)
    return db_connection


# make s3 connection
def get_s3_connection():
    s3_connection = boto3.client(
        's3',
        aws_access_key_id = S3_CONFIG['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key = S3_CONFIG['AWS_SECRET_ACCESS_KEY'],
        region_name = S3_CONFIG['REGION_NAME'],
    )
    return s3_connection



