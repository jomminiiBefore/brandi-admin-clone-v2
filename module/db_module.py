import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(
            host        = 'localhost',
            user        = 'root',
            password    = '',
            db          = 'brandi',
            charset     = 'utf8',
            port        = '3306'
        )

        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
    
    def commit(self):
        self.db.commit()