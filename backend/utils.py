from connection import get_connection

def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            #decode
            account_no = access_token['account_no']

            db_connection = get_connection()
            with db_connection.cursor(buffered=True, dictionary=True) as db_cursor:
                new


        except Exception as e:
            print(e)