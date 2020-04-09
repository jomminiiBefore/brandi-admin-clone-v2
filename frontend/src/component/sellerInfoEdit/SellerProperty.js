import React, { useState } from 'react';
import style from 'src/utils/styles';
import styled from 'styled-components';

const SellerProperty = ({ sellerTypes, type, onChangeRadio }) => {
  return (
    <Container>
      {sellerTypes
        ? sellerTypes.map((item, key) => (
            <React.Fragment key={key}>
              {type === item.seller_type_no ? (
                <InputButtonContainer>
                  <input
                    type="radio"
                    id="property"
                    name="brand"
                    value={item.seller_type_no}
                    onChange={onChangeRadio}
                    checked
                  />
                  <LabelText>{item.seller_type_name}</LabelText>
                </InputButtonContainer>
              ) : (
                <InputButtonContainer>
                  <input
                    type="radio"
                    id="property"
                    name="brand"
                    value={item.seller_type_no}
                    onChange={onChangeRadio}
                  />
                  <LabelText>{item.seller_type_name}</LabelText>
                </InputButtonContainer>
              )}
            </React.Fragment>
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
