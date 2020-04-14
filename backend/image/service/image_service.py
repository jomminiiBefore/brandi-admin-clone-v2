import uuid, io, os
from connection import get_s3_connection
from flask import jsonify

from PIL import Image


class ImageService:

    # 이미지 리사이즈 : big
    def resize_to_big(self, image_file):
        """
        Args:
            image_file: 이미지 파일

        Returns:
            리사이즈 성공시: ByteIO 객체, uuid

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
                image_file_form = image_file.content_type
                if 'png' in image_file_form:
                    resized_image_big.save(big_io, 'png')
                if 'jpeg' in image_file_form:
                    resized_image_big.save(big_io, 'jpeg')
                big_io.seek(0)
                return [big_io, str(uuid.uuid4())]
        except:
            return None

    # 이미지 리사이즈 : medium
    def resize_to_medium(self, image_file):
        """
        Args:
            image_file: 이미지 파일

        Returns:
            리사이즈 성공시: ByteIO 객체, uuid

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
        """
        Args:
            image_file: 이미지 파일

        Returns:
            리사이즈 성공시: ByteIO 객체, uuid

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

        except:
            return None

    # 요청받은 상품 이미지를 리사이즈 하고 s3에 업로드
    def upload_product_image(self, request):
        """
        Args:
            request: 요청 값

        Returns:
            리사이즈 성공시: s3 버킷에 올라간 이미지파일의 url(dictionary)
            리사이즈 실패시: error message, status code

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-02 (yoonhc@brandi.co.kr): 초기 생성
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
                    return jsonify({'message': 'INVALID_FILE'})

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE1'})

                # big_size 업로드
                big_size_buffer = self.resize_to_big(image_file_1)
                if not big_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE33"}), 400
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
                return jsonify({'message' : 'INVALID_REQUEST'})

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
                    return jsonify({"message": "INVALID_IMAGE2"}), 400
                s3.put_object(Body=big_size_buffer[0], Bucket="brandi-intern", Key=big_size_buffer[1],
                              ContentType='image/jpeg')
                big_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{big_size_buffer[1]}'
                data['image_file_2']['big_size_url'] = big_size_url
                data['image_file_2']['big_image_size_id'] = 1

                # medium_size 업로드
                medium_size_buffer = self.resize_to_medium(image_file_2)
                if not medium_size_buffer:
                    return jsonify({"message": "INVALID_IMAGE33"}), 400
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
        """
        Args:
            request: 요청 값

        Returns:
            s3 버킷에 올라간 이미지 파일의 url(dictionary)

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-02 (yoonhc@brandi.co.kr): 초기 생성
        """

        data = {}
        # print([file for file in request.files])
        seller_profile_image = request.files.get('seller_profile_image', None)
        certificate_image = request.files.get('certificate_image', None)
        online_business_image = request.files.get('online_business_image', None)
        background_image = request.files.get('background_image', None)
        # 파일의 존재여부 확인.
        if seller_profile_image and certificate_image and online_business_image:
            try:
                # 들어온 파일의 사이즈를 구함.
                image_file_size = os.fstat(seller_profile_image.fileno()).st_size
                image_file_form = seller_profile_image.content_type

                # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
                if not ('image' in image_file_form):
                    return jsonify({'message': 'INVALID_FILE1'})

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE1'})

                uploaded_image_name = str(uuid.uuid4())
                s3 = get_s3_connection()
                s3.put_object(Body=seller_profile_image, Bucket="brandi-intern", Key=uploaded_image_name, ContentType='image/jpeg')
                uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
                data["profile_image_url"] = uploaded_image_url

            except Exception as e:
                print(f'Error : {e}')
                return jsonify({'message': 'INVALID_REQUEST1'})

            try:
                # 들어온 파일의 사이즈를 구함.
                image_file_size = os.fstat(certificate_image.fileno()).st_size
                image_file_form = certificate_image.content_type

                # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
                if not ('image' in image_file_form):
                    return jsonify({'message': 'INVALID_FILE2'})

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE2'})

                uploaded_image_name = str(uuid.uuid4())
                s3 = get_s3_connection()
                s3.put_object(Body=certificate_image, Bucket="brandi-intern", Key=uploaded_image_name, ContentType='image/jpeg')
                uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
                data["certificate_image_url"] = uploaded_image_url

            except Exception as e:
                print(f'Error : {e}')
                return jsonify({'message': 'INVALID_REQUEST2'})

            try:
                # 들어온 파일의 사이즈를 구함.
                image_file_size = os.fstat(online_business_image.fileno()).st_size
                image_file_form = online_business_image.content_type

                # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
                if not ('image' in image_file_form):
                    return jsonify({'message': 'INVALID_FILE3'})

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE3'})

                uploaded_image_name = str(uuid.uuid4())
                s3 = get_s3_connection()
                s3.put_object(Body=online_business_image, Bucket="brandi-intern", Key=uploaded_image_name, ContentType='image/jpeg')
                uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
                data["online_business_image_url"] = uploaded_image_url

            except Exception as e:
                print(f'Error : {e}')
                return jsonify({'message': 'INVALID_REQUEST3'})
            
        else:
            return jsonify({'message': 'INVALID_REQUEST'}), 400

        if background_image:
            try:
                # 들어온 파일의 사이즈를 구함.
                image_file_size = os.fstat(background_image.fileno()).st_size
                image_file_form = background_image.content_type

                # 이미지 파일이 아닌 다른형식의 파일이 들어오는 것을 차단.
                if not ('image' in image_file_form):
                    return jsonify({'message': 'INVALID_FILE4'})

                # 들어온 이미지 크기가 10MB보다 크면 request를 받지 않음.
                if image_file_size > 10485760:
                    return jsonify({'message': 'INVALID_IMAGE4'})

                uploaded_image_name = str(uuid.uuid4())
                s3 = get_s3_connection()
                s3.put_object(Body=background_image, Bucket="brandi-intern", Key=uploaded_image_name, ContentType='image/jpeg')
                uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
                data["background_image_url"] = uploaded_image_url

            except Exception as e:
                print(f'Error : {e}')
                return jsonify({'message': 'INVALID_REQUEST4'})

        return data

    # 요청받은 기획전 이미지를 s3에 업로드
    def upload_event_image(self, request):
        """
        Args:
            request: 요청 값

        Returns:
            s3 버킷에 올라간 이미지 파일의 url(dictionary)

        Authors:
            yoonhc@brandi.co.kr (윤희철)

        History:
            2020-04-02 (yoonhc@brandi.co.kr): 초기 생성
        """

        data = {}
        image_file = request.files['imagefile']

        # 500MB 이하만 업로드 가능
        try:
            with Image.open(image_file) as pillow_obj:
                buffer = io.BytesIO()
                pillow_obj.save(buffer, pillow_obj.format)
                print(buffer.tell()/1000)
                if buffer.tell()/1000 > 500000:
                    return jsonify({'message' : f'{buffer}'}), 400
        except:
            return jsonify({'message' : 'INVALID_IMAGE1'}), 400

        uploaded_image_name = str(uuid.uuid4())
        s3 = get_s3_connection()
        s3.put_object(Body=image_file, Bucket="brandi-intern", Key=uploaded_image_name)
        uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
        data["uploaded_image_url"] = uploaded_image_url

        return data