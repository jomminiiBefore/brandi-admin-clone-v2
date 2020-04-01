from flask import jsonify

class ImageDao:
    def upload_image(self, data, db_connection):
        db_cursor = db_connection.cursor(buffered=True, dictionary=True)
        product_image_url = {
            'image_url' : data['image_url'],
            'product_info_id' : data['product_info_id'],
            'image_size_id' : data['image_size_id'],
            'image_order' : data['image_order'],
        }
        sql_command = ("""
        INSERT INTO product_images (
        image_url,
        product_info_id,
        image_size_id,
        image_order
        ) values (
        %(image_url)s,
        %(product_info_id)s,
        %(image_size_id)s,
        %(image_order)s
        )
        """)
        db_cursor.execute(sql_command, product_image_url)

        return jsonify({"message" : "SUCCESS"}), 200