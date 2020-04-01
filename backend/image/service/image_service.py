from connection import get_s3_connection
import boto3

class ImageService:
    def __init__(self, image_dao):
        self.image_dao = image_dao

    def upload_image(self, request, db_connection):
        data = request.json
        # image_file = open('test_image.jpeg', 'rb')
        image_file = request.files.get('imagefiles', None)

        s3 = get_s3_connection()
        s3.upload_fileobj(image_file, "brandi-intern", image_file.name)
        # 올리는 시점에 이름을 정해줌.
        url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{image_file.name}'
        data['image_url'] = url

        image_upload_result = self.image_dao.upload_image(data, db_connection)
        return image_upload_result
