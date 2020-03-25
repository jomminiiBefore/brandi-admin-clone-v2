import mysql.connector
from mysql.connector.cursor import MySQLCursor

class SellerDao:

    def __init__(self, database):
        self.db  = database
    
    def create_seller(self, new_seller):
        
        db_cursor       = self.db.cursor(dictionary = True)
        new_seller_info = {
            'name'  : new_seller['name']
        }

        insert_statement    = (
            "INSERT INTO brandi.seller(name)"
            "VALUES (%s)"
        )
        insert_name         = new_data['name']
        db_cursor.execute(insert_statement, insert_name)
            
        self.db.commit()
        db_cursor.close()
            