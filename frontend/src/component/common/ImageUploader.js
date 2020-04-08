import React, { useState, useEffect } from 'react';
import style from 'src/utils/styles';
import styled from 'styled-components';
import CustomButton from './CustomButton';
import InfoText from './InfoText';

const ImageUploader = ({ name, setImg, img }) => {
  const [imagePreviewUrl, setImagePreviewUrl] = useState();
  useEffect(() => {
    setImagePreviewUrl(img);
  }, [img]);

  // 이미지 변경
  const _handleImageChange = (e) => {
    e.preventDefault();

    let reader = new FileReader();
    let file = e.target.files[0];

    reader.onloadend = () => {
      setImagePreviewUrl(reader.result);
      setImg(name, reader.result);
    };

    reader.readAsDataURL(file);
  };

  // 이미지 삭제
  const onRemove = () => {
    console.log('onRemove');
    setImagePreviewUrl(null);
    setImg(name, null);
  };

  return (
    <div>
      {imagePreviewUrl ? (
        // 이미지를 선택 함
        <>
          <div>
            <Image src={imagePreviewUrl} alt="" />
          </div>
          <InputButtonWrapper>
            <InputButtonText>변경</InputButtonText>

            <InputUpdateButton
              type="file"
              onChange={_handleImageChange}
              accept="image/jpg,image/png,image/jpeg"
            />
          </InputButtonWrapper>
          <CustomButton
            name="삭제"
            onClickEvent={onRemove}
            color={style.color.validationRed}
            textColor="#fff"
          />
        </>
      ) : (
        // 이미지를 선택하지 않음 (기본 이미지)
        <>
          <div>
            <DefaultImage src="http://image.brandi.me/seller/noimage.png" />
          </div>
          <InputButtonWrapper>
            <InputButtonText>이미지 선택</InputButtonText>
            <InputImageSelect
              type="file"
              onChange={_handleImageChange}
              accept="image/jpg,image/png,image/jpeg"
            />
          </InputButtonWrapper>
        </>
      )}
    </div>
  );
};
export default ImageUploader;

const DefaultImage = styled.img`
  max-height: 100px;
  margin: 0 auto;
  padding: 4px;
  margin-bottom: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
`;

const Image = styled.img`
  max-height: 150px;
  margin: 0 auto;
  padding: 4px;
  margin-bottom: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
`;

const InputButtonWrapper = styled.span`
  display: inline-block;
  border: 1px solid #ddd;
  padding: 6px 12px;
  border-radius: 4px;
  text-align: center;
  cursor: pointer;
  &:hover {
    background-color: #afafaf;
    filter: brightness(80%);
  }
`;

const InputImageSelect = styled.input`
  opacity: 0;
  width: 70px;
`;

const InputUpdateButton = styled.input`
  opacity: 0;
  width: 24px;
  cursor: pointer;
  z-index: 1;
  padding: 0px;
  margin: 0px;
`;

const InputButtonText = styled.span`
  position: absolute;
  z-index: -1;
  font-size: 14px;
`;
