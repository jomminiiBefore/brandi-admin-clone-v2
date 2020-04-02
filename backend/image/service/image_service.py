import uuid, io
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
                resized_image_big.save(big_io, "JPEG")
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

    # 요청받은 이미지를 리사이즈 하고 s3에 업로드
    def upload_resized_image(self, request):
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

        data = {}
        image_file = request.files['imagefile']
        s3 = get_s3_connection()

        # big_size 업로드
        big_size_buffer = self.resize_to_big(image_file)
        if not big_size_buffer:
            return jsonify({"message" : "INVALID_IMAGE"}), 400
        s3.put_object(Body = big_size_buffer[0], Bucket = "brandi-intern", Key = big_size_buffer[1])
        big_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{big_size_buffer[1]}'
        data['big_size_url'] = big_size_url

        # medium_size 업로드
        medium_size_buffer = self.resize_to_medium(image_file)
        if not medium_size_buffer:
            return jsonify({"message" : "INVALID_IMAGE"}), 400
        s3.put_object(Body = medium_size_buffer[0], Bucket = "brandi-intern", Key = medium_size_buffer[1])
        medium_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{medium_size_buffer[1]}'
        data['medium_size_url'] = medium_size_url

        # small_size 업로드
        small_size_buffer = self.resize_to_small(image_file)
        if not small_size_buffer:
            return jsonify({"message" : "INVALID_IMAGE"}), 400
        s3.put_object(Body = small_size_buffer[0], Bucket = "brandi-intern", Key = small_size_buffer[1])
        small_size_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{small_size_buffer[1]}'
        data['small_size_url'] = small_size_url

        return data

    # 요청받은 이미지를 s3에 업로드
    def upload_image(self, request):
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
        uploaded_image_name = str(uuid.uuid4())
        s3 = get_s3_connection()
        s3.put_object(Body = image_file, Bucket = "brandi-intern", Key = uploaded_image_name)
        uploaded_image_url = f'https://brandi-intern.s3.ap-northeast-2.amazonaws.com/{uploaded_image_name}'
        data["uploaded_image_url"] = uploaded_image_url

        return data
