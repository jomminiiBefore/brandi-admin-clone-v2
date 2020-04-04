import React from 'react';
import style from 'src/utils/styles';
import styled from 'styled-components';
import CustomButton from '../common/CustomButton';
import ImageUploader from '../common/ImageUploader';

const SellerProfile = () => {
  return (
    <Container>
      {/* <ImageContainer>
        <Image src="http://image.brandi.me/seller/noimage.png"></Image>
      </ImageContainer>
      <CustomButton /> */}
      {/* <div>
        <form>
          <input type="file" accept="image/*" />
          <button type="submit">Upload Image</button>
        </form>
        {$imagePreview}
      </div> */}
      <ImageUploader />
    </Container>
  );
};

export default SellerProfile;

const Container = styled.div``;

const ImageContainer = styled.div`
  width: 130px;
  height: 100px;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 4px;
  margin-bottom: 5px;
`;
const Image = styled.img`
  max-height: 100%;
  margin: 0 auto;
`;
