import jwt, uuid, io, os
from mysql.connector.errors import Error
from flask import request, jsonify, g

from connection import DatabaseConnection, get_s3_connection
from PIL import Image
from config import SECRET


def login_required(func):
    def wrapper(*args, **kwargs):
        access_token = request.headers.get('Authorization', None)

        if access_token:
            try:
                payload = jwt.decode(access_token, SECRET['secret_key'], algorithm=SECRET['algorithm'])
                account_no = payload['account_no']

                db_connection = DatabaseConnection()
                if db_connection:
                    try:
                        with db_connection as db_cursor:
                            get_account_info_stmt = ("""
                                SELECT auth_type_id, is_deleted FROM accounts WHERE account_no=%(account_no)s
                            """)
                            db_cursor.execute(get_account_info_stmt, {'account_no': account_no})
                            account = db_cursor.fetchone()
                            if account:
                                if account['is_deleted'] == 0:
                                    g.account_info = {
                                        'account_no': account_no,
                                        'auth_type_id': account['auth_type_id']
                                    }
                                    return func(*args, **kwargs)
                                return jsonify({'message': 'DELETED_ACCOUNT'}), 400
                            return jsonify({'message': 'ACCOUNT_DOES_NOT_EXIST'}), 404

                    except Error as e:
                        print(f'DATABASE_CURSOR_ERROR_WITH {e}')
                        return jsonify({'message': 'DB_CURSOR_ERROR'}), 400

            except jwt.InvalidTokenError:
                return jsonify({'message': 'INVALID_TOKEN'}), 401

            return jsonify({'message': 'NO_DATABASE_CONNECTION'}), 400
        return jsonify({'message': 'INVALID_TOKEN'}), 401
    return wrapper


class ImageUpload:

    # 이미지 리사이즈 : big
    def resize_to_big(self, image_file):
        """ 이미지를 big 사이즈로 리사이즈
        pillow 라이브러리를 사용하여 들어온 이미지 파일을 pillow객체로 만들고 pillow객체에 있는 매서드를 사용하여 리사이즈.
        가로의 길이를 고정 사이즈로 이용하여 세로의 길이를 구해서 리사이즈함.
        리사이즈 된 pillow객체를 bytesIO buffer에 담고 랜덤으로 생성한 이름과 buffer 자체를 리턴함.

        Args:
            image_file: 이미지 파일 객체

        Returns:
            리사이즈 성공: ByteIO 객체, uuid를 리스트에 담아서 리턴
            리사이즈 실패: None을 리턴해서 애러처리

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-02 (yoonhc@brandi.co.kr): 초기 생성
        """

        standard_size = 640
        try:
            with Image.open(image_file) as opened_image:
                big = (int(standard_size), int(opened_image.size[1]*(standard_size/opened_image.size[0])))
                resized_image_big = opened_image.resize(big)
                big_io = io.BytesIO()
                resized_image_big.save(big_io, "JPEG")
                big_io.seek(0)
                return [big_io, str(uuid.uuid4())]

        except:
            return None

    # 이미지 리사이즈 : medium
    def resize_to_medium(self, image_file):
        """ 이미지를 medium사이즈로 리사이즈
        pillow 라이브러리를 사용하여 들어온 이미지 파일을 pillow객체로 만들고 pillow객체에 있는 매서드를 사용하여 리사이즈.
        가로의 길이를 고정 사이즈로 이용하여 세로의 길이를 구해서 리사이즈함.
        리사이즈 된 pillow객체를 bytesIO buffer에 담고 랜덤으로 생성한 이름과 buffer 자체를 리턴함.

        Args:
            image_file: 이미지 파일 객체

        Returns:
            리사이즈 성공: ByteIO 객체, uuid를 리스트에 담아서 리턴
            리사이즈 실패: None을 리턴해서 애러처리

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-02 (yoonhc@brandi.co.kr): 초기 생성
        """
        standard_size = 320
        try:
            with Image.open(image_file) as opened_image:
                medium = (int(standard_size), int(opened_image.size[1]*(standard_size/opened_image.size[0])))
                resized_image_medium = opened_image.resize(medium)
                medium_io = io.BytesIO()
                resized_image_medium.save(medium_io, "JPEG")
                medium_io.seek(0)
                return [medium_io, str(uuid.uuid4())]

        except:
            return None

    # 이미지 리사이즈 : small
    def resize_to_small(self, image_file):
        """ 이미지를 small 사이즈로 리사이즈
        pillow 라이브러리를 사용하여 들어온 이미지 파일을 pillow객체로 만들고 pillow객체에 있는 매서드를 사용하여 리사이즈.
        가로의 길이를 고정 사이즈로 이용하여 세로의 길이를 구해서 리사이즈함.
        리사이즈 된 pillow객체를 bytesIO buffer에 담고 랜덤으로 생성한 이름과 buffer 자체를 리턴함.

        Args:
            image_file: 이미지 파일 객체

        Returns:
            리사이즈 성공: ByteIO 객체, uuid를 리스트에 담아서 리턴
            리사이즈 실패: None을 리턴해서 애러처리

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-02 (yoonhc@brandi.co.kr): 초기 생성
        """
        standard_size = 120
        try:
            with Image.open(image_file) as opened_image:
                small = (int(standard_size), int(opened_image.size[1]*(standard_size/opened_image.size[0])))
                resized_image_small = opened_image.resize(small)
                small_io = io.BytesIO()
                resized_image_small.save(small_io, "JPEG")
                small_io.seek(0)
                return [small_io, str(uuid.uuid4())]

        # 이미지를 pillow객체로 만들지 못하는 경우 애러처리를 위해 None을 리턴
        except:
            return None

    # 요청받은 상품 이미지를 리사이즈 하고 s3에 업로드
    def upload_product_image(self, request):
        """ 상품 이미지 파일을 3가지 크기로 리사이즈 해서 s3에 업로드 하고 업로드한 이미지의 url, 사이즈를 리턴하는 함수.
        들어올 것으로 예상되는 key값을 지정하고 해당 key로 들어오지 않으면 None을 변수에 담아서 처리.
        파일의 형식이 image가 아닐 경우 이미지를 업로드 하지 않음.
        파일의 크기가 일정크기를 넘으면 업로드 하지 않음.
        이미지가 들어오지 않아도 해당 이미지 순서에 있는 key는 존재하도록 설계

        Args:
            request: 상품 이미지 파일을 포함한 요청 값.

        Returns:
            data: s3 버킷에 올라간 이미지파일의 url(dictionary), size를 포함한 딕셔너리
            400: 파일형식이 잘못된 경우, 파일 크기가 너무 큰 경우

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-02 (yoonhc@brandi.co.kr): 초기 생성
            2020-04-09 (yoonhc@brandi.co,kr): RESTful api형식에 맞추기 위해서 이미지 업로드 기능의 모듈화.
        """
        # s3 연결
        s3 = get_s3_connection()

        # 리턴값이 들어갈 리스트
        data = {
            'image_file_1': {},
            'image_file_2': {},
            'image_file_3': {},
            'image_file_4': {},
            'image_file_5': {}
        }

        # 파일의 존재여부 확인, 이미지 순서를 파일 이름으로 받음.
        image_file_1 = request.files.get('image_file_1', None)
        image_file_2 = request.files.get('image_file_2', None)
        image_file_3 = request.files.get('image_file_3', None)
        image_file_4 = request.files.get('image_file_4', None)
        image_file_5 = request.files.get('image_file_5', None)

        # 순서1번의 이미지파일 이 존재하면 업로드하고 url을 딕셔너리에 추가
        if image_file_1:
            try:
                # 들어온 파일의 사이즈와 확장자를 구함.
                image_file_size = os.fstat(image_file_1.fileno()).st_size
                image_file_form = image_file_1.content_type

                # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
                if not ('image' in image_file_form):
                    return jsonify({'message': 'INVALID_FILE'}), 400

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE1'}), 400

                # big_size 업로드
                big_size_buffer = self.resize_to_big(image_file_1)
                if not big_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=big_size_buffer[0], Bucket="brandi-intern", Key=big_size_buffer[1],
                              ContentType='image/jpeg')
                big_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{big_size_buffer[1]}'
                data['image_file_1']['big_size_url'] = big_size_url
                data['image_file_1']['big_image_size_id'] = 1

                # medium_size 업로드
                medium_size_buffer = self.resize_to_medium(image_file_1)
                if not medium_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=medium_size_buffer[0], Bucket="brandi-intern", Key=medium_size_buffer[1],
                              ContentType='image/jpeg')
                medium_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{medium_size_buffer[1]}'
                data['image_file_1']['medium_size_url'] = medium_size_url
                data['image_file_1']['medium_image_size_id'] = 2

                # small_size 업로드
                small_size_buffer = self.resize_to_small(image_file_1)
                if not small_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=small_size_buffer[0], Bucket="brandi-intern", Key=small_size_buffer[1],
                              ContentType='image/jpeg')
                small_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{small_size_buffer[1]}'
                data['image_file_1']['small_size_url'] = small_size_url
                data['image_file_1']['small_image_size_id'] = 3

            except Exception as e:
                print(f'error1 : {e}')
                return jsonify({'message' : 'INVALID_REQUEST'}), 400

        # 순서2번의 이미지파일 이 존재하면 업로드하고 url을 딕셔너리에 추가
        if image_file_2:
            try:
                # 들어온 파일의 사이즈와 확장자를 구함.
                image_file_size = os.fstat(image_file_2.fileno()).st_size
                image_file_form = image_file_2.content_type

                # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
                if not ('image' in image_file_form):
                    return jsonify({'message': 'INVALID_FILE'})

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE1'})

                # big_size 업로드
                big_size_buffer = self.resize_to_big(image_file_2)
                if not big_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=big_size_buffer[0], Bucket="brandi-intern", Key=big_size_buffer[1],
                              ContentType='image/jpeg')
                big_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{big_size_buffer[1]}'
                data['image_file_2']['big_size_url'] = big_size_url
                data['image_file_2']['big_image_size_id'] = 1

                # medium_size 업로드
                medium_size_buffer = self.resize_to_medium(image_file_2)
                if not medium_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=medium_size_buffer[0], Bucket="brandi-intern", Key=medium_size_buffer[1],
                              ContentType='image/jpeg')
                medium_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{medium_size_buffer[1]}'
                data['image_file_2']['medium_size_url'] = medium_size_url
                data['image_file_2']['medium_image_size_id'] = 2

                # small_size 업로드
                small_size_buffer = self.resize_to_small(image_file_2)
                if not small_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=small_size_buffer[0], Bucket="brandi-intern", Key=small_size_buffer[1],
                              ContentType='image/jpeg')
                small_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{small_size_buffer[1]}'
                data['image_file_2']['small_size_url'] = small_size_url
                data['image_file_2']['small_image_size_id'] = 3

            except Exception as e:
                print(f'error1 : {e}')
                return jsonify({'message' : 'INVALID_REQUEST'})

        # 순서3번의 이미지파일 이 존재하면 업로드하고 url을 딕셔너리에 추가
        if image_file_3:
            try:
                # 들어온 파일의 사이즈와 확장자를 구함.
                image_file_size = os.fstat(image_file_3.fileno()).st_size
                image_file_form = image_file_3.content_type

                # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
                if not ('image' in image_file_form):
                    return jsonify({'message': 'INVALID_FILE'})

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE1'})

                # big_size 업로드
                big_size_buffer = self.resize_to_big(image_file_3)
                if not big_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=big_size_buffer[0], Bucket="brandi-intern", Key=big_size_buffer[1],
                              ContentType='image/jpeg')
                big_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{big_size_buffer[1]}'
                data['image_file_3']['big_size_url'] = big_size_url
                data['image_file_3']['big_image_size_id'] = 1

                # medium_size 업로드
                medium_size_buffer = self.resize_to_medium(image_file_3)
                if not medium_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=medium_size_buffer[0], Bucket="brandi-intern", Key=medium_size_buffer[1],
                              ContentType='image/jpeg')
                medium_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{medium_size_buffer[1]}'
                data['image_file_3']['medium_size_url'] = medium_size_url
                data['image_file_3']['medium_image_size_id'] = 2

                # small_size 업로드
                small_size_buffer = self.resize_to_small(image_file_3)
                if not small_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=small_size_buffer[0], Bucket="brandi-intern", Key=small_size_buffer[1],
                              ContentType='image/jpeg')
                small_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{small_size_buffer[1]}'
                data['image_file_3']['small_size_url'] = small_size_url
                data['image_file_3']['small_image_size_id'] = 3

            except Exception as e:
                print(f'error1 : {e}')
                return jsonify({'message' : 'INVALID_REQUEST'})

        # 순서4번의 이미지파일 이 존재하면 업로드하고 url을 딕셔너리에 추가
        if image_file_4:
            try:
                # 들어온 파일의 사이즈와 확장자를 구함.
                image_file_size = os.fstat(image_file_4.fileno()).st_size
                image_file_form = image_file_4.content_type

                # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
                if not ('image' in image_file_form):
                    return jsonify({'message': 'INVALID_FILE'})

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE1'})

                # big_size 업로드
                big_size_buffer = self.resize_to_big(image_file_4)
                if not big_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=big_size_buffer[0], Bucket="brandi-intern", Key=big_size_buffer[1],
                              ContentType='image/jpeg')
                big_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{big_size_buffer[1]}'
                data['image_file_4']['big_size_url'] = big_size_url
                data['image_file_4']['big_image_size_id'] = 1

                # medium_size 업로드
                medium_size_buffer = self.resize_to_medium(image_file_4)
                if not medium_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=medium_size_buffer[0], Bucket="brandi-intern", Key=medium_size_buffer[1],
                              ContentType='image/jpeg')
                medium_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{medium_size_buffer[1]}'
                data['image_file_4']['medium_size_url'] = medium_size_url
                data['image_file_4']['medium_image_size_id'] = 2

                # small_size 업로드
                small_size_buffer = self.resize_to_small(image_file_4)
                if not small_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=small_size_buffer[0], Bucket="brandi-intern", Key=small_size_buffer[1],
                              ContentType='image/jpeg')
                small_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{small_size_buffer[1]}'
                data['image_file_4']['small_size_url'] = small_size_url
                data['image_file_4']['small_image_size_id'] = 3

            except Exception as e:
                print(f'error1 : {e}')
                return jsonify({'message' : 'INVALID_REQUEST'})

        # 순서5번의 이미지파일 이 존재하면 업로드하고 url을 딕셔너리에 추가
        if image_file_5:
            try:
                # 들어온 파일의 사이즈와 확장자를 구함.
                image_file_size = os.fstat(image_file_5.fileno()).st_size
                image_file_form = image_file_5.content_type

                # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
                if not ('image' in image_file_form):
                    return jsonify({'message': 'INVALID_FILE'})

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE1'})

                # big_size 업로드
                big_size_buffer = self.resize_to_big(image_file_5)
                if not big_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=big_size_buffer[0], Bucket="brandi-intern", Key=big_size_buffer[1],
                              ContentType='image/jpeg')
                big_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{big_size_buffer[1]}'
                data['image_file_5']['big_size_url'] = big_size_url
                data['image_file_5']['big_image_size_id'] = 1

                # medium_size 업로드
                medium_size_buffer = self.resize_to_medium(image_file_5)
                if not medium_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=medium_size_buffer[0], Bucket="brandi-intern", Key=medium_size_buffer[1],
                              ContentType='image/jpeg')
                medium_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{medium_size_buffer[1]}'
                data['image_file_5']['medium_size_url'] = medium_size_url
                data['image_file_5']['medium_image_size_id'] = 2

                # small_size 업로드
                small_size_buffer = self.resize_to_small(image_file_5)
                if not small_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE"}), 400
                s3.put_object(Body=small_size_buffer[0], Bucket="brandi-intern", Key=small_size_buffer[1],
                              ContentType='image/jpeg')
                small_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{small_size_buffer[1]}'
                data['image_file_5']['small_size_url'] = small_size_url
                data['image_file_5']['small_image_size_id'] = 3

            except Exception as e:
                print(f'error1 : {e}')
                return jsonify({'message' : 'INVALID_REQUEST'})

        return data

    # 요청받은 셀러 이미지를 s3에 업로드
    def upload_seller_image(self, request):
        """ 셀러 이미지 파일을 업로드하고 url을 리턴하는 매서드
        들어올 것으로 예상되는 key값을 지정하고 해당 key로 들어오지 않으면 None을 변수에 담아서 처리.
        파일의 형식이 image가 아닐 경우 이미지를 업로드 하지 않음.
        파일의 크기가 일정크기를 넘으면 업로드 하지 않음.
        boto3 라이브러리를 이용하여 s3에 업로드하고 url을 리턴함.

        Args:
            request: 이미지 파일을 포함한 요청 값

        Returns:
            data: s3 버킷에 올라간 이미지 파일의 url(dictionary)

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-02 (yoonhc@brandi.co.kr): 초기 생성
            2020-04-09 (yoonhc@brandi.co.kr): image파일 업로드 형식을 RESTful api 기준에 맞추어 모듈로 만들고 필요한 앱에서 import해서 사용하는 방식 채택
        """

        data = {}
        # print([file for file in request.files])
        seller_profile_image = request.files.get('seller_profile_image', None)
        certificate_image = request.files.get('certificate_image', None)
        online_business_image = request.files.get('online_business_image', None)
        background_image = request.files.get('background_image', None)

        # 필수로 들어와야 하는 파일의 존재여부 확인.
        if seller_profile_image:

            # 들어온 파일의 사이즈를 구함.
            image_file_size = os.fstat(seller_profile_image.fileno()).st_size
            image_file_form = seller_profile_image.content_type

            # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
            if not ('image' in image_file_form):
                return jsonify({'message': 'INVALID_FILE1'}), 400

            # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
            if image_file_size > 10485760:
                return jsonify({'message': 'INVALID_IMAGE1'}), 400

            uploaded_image_name = str(uuid.uuid4())
            s3 = get_s3_connection()
            s3.put_object(Body=seller_profile_image, Bucket="brandi-intern", Key=uploaded_image_name, ContentType='image/jpeg')
            uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
            data["s3_profile_image_url"] = uploaded_image_url

        if certificate_image:

            # 들어온 파일의 사이즈를 구함.
            image_file_size = os.fstat(certificate_image.fileno()).st_size
            image_file_form = certificate_image.content_type

            # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
            if not ('image' in image_file_form):
                return jsonify({'message': 'INVALID_FILE2'}), 400

            # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
            if image_file_size > 10485760:
                return jsonify({'message': 'INVALID_IMAGE2'}), 400

            uploaded_image_name = str(uuid.uuid4())
            s3 = get_s3_connection()
            s3.put_object(Body=certificate_image, Bucket="brandi-intern", Key=uploaded_image_name, ContentType='image/jpeg')
            uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
            data["s3_certificate_image_url"] = uploaded_image_url

        if online_business_image:
            # 들어온 파일의 사이즈를 구함.
            image_file_size = os.fstat(online_business_image.fileno()).st_size
            image_file_form = online_business_image.content_type

            # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
            if not ('image' in image_file_form):
                return jsonify({'message': 'INVALID_FILE3'}), 400

            # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
            if image_file_size > 10485760:
                return jsonify({'message': 'INVALID_IMAGE3'}), 400

            uploaded_image_name = str(uuid.uuid4())
            s3 = get_s3_connection()
            s3.put_object(Body=online_business_image, Bucket="brandi-intern", Key=uploaded_image_name, ContentType='image/jpeg')
            uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
            data["s3_online_business_image_url"] = uploaded_image_url

        if background_image:

            # 들어온 파일의 사이즈를 구함.
            image_file_size = os.fstat(background_image.fileno()).st_size
            image_file_form = background_image.content_type

            # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
            if not ('image' in image_file_form):
                return jsonify({'message': 'INVALID_FILE4'}), 400

            # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
            if image_file_size > 10485760:
                return jsonify({'message': 'INVALID_IMAGE4'}), 400

            uploaded_image_name = str(uuid.uuid4())
            s3 = get_s3_connection()
            s3.put_object(Body=background_image, Bucket="brandi-intern", Key=uploaded_image_name, ContentType='image/jpeg')
            uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
            data["s3_background_image_url"] = uploaded_image_url

        return data