import React, { useState } from 'react';
import style from 'src/utils/styles';
import styled from 'styled-components';

const SellerProperty = () => {
  const [property, setProperty] = useState();

  const onChangeRadio = e => {
    console.log(e.target.value);
  };

  return (
    <Container>
      <InputButtonContainer>
        <input
          type="radio"
          id="designer"
          name="brand"
          value="designer"
          onChange={onChangeRadio}
        />
        <label for="designer">디자이너브랜드</label>
      </InputButtonContainer>
      <InputButtonContainer>
        <input
          type="radio"
          id="general"
          name="brand"
          value="general"
          onChange={onChangeRadio}
        />
        <label for="general">제너럴브랜드</label>
      </InputButtonContainer>
      <InputButtonContainer>
        <input
          type="radio"
          id="national"
          name="brand"
          value="national"
          onChange={onChangeRadio}
        />
        <label for="national">내셔널브랜드</label>
      </InputButtonContainer>
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
