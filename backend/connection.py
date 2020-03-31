import mysql.connector
from mysql.connector.errors import InterfaceError, ProgrammingError, NotSupportedError

from config import DATABASES


# make database connection
def get_connection():
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
    try:
        db_connection = mysql.connector.connect(**db_config)
        return db_connection

    except InterfaceError as e:
        print(f'INTERFACE_ERROR_WITH {e}')
        return

    except ProgrammingError as e:
        print(f'PROGRAMMING_ERROR_WITH {e}')
        return

    except NotSupportedError as e:
        print(f'NOT_SUPPORTED_ERROR_WITH {e}')

