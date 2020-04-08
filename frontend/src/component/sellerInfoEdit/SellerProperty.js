import React, { useState } from 'react';
import style from 'src/utils/styles';
import styled from 'styled-components';

const SellerProperty = ({ sellerTypes }) => {
  const onChangeRadio = (e) => {
    console.log(e.target.value);
  };

  return (
    <Container>
      {sellerTypes
        ? sellerTypes.map((item, key) => (
            <InputButtonContainer key={key}>
              <input
                type="radio"
                id={item.seller_type_no}
                name="brand"
                value={item.seller_type_no}
                onChange={onChangeRadio}
              />
              <LabelText>{item.seller_type_name}</LabelText>
            </InputButtonContainer>
          ))
        : ''}
    </Container>
  );
};

export default SellerProperty;

const Container = styled.div`
  display: flex;
  flex-direction: row;
  padding: 7px 0;
`;

const InputButtonContainer = styled.div`
  margin-right: 15px;
`;

const LabelText = styled.label`
  font-size: 13px;
`;
