import React from 'react';
import style from 'src/utils/styles';
import styled from 'styled-components';

const TableItem = props => {
  return (
    <Container>
      {/* 타이틀  */}
      <TitleContainer>
        <TitleText>{props.title}</TitleText>
        {props.isRequired && <RequiredText>*</RequiredText>}
      </TitleContainer>
      <ContentContainer>{props.children}</ContentContainer>
    </Container>
  );
};

export default TableItem;

const Container = styled.div`
  display: flex;
  border: 1px solid #ddd;
  margin-top: -1px;
`;

const TitleContainer = styled.div`
  display: flex;
  border-right: 1px solid #ddd;
  padding: 8px;
  width: 20vw;
  align-items: center;
`;

const TitleText = styled.div`
  font-size: ${style.fontSize.generalFont};
`;

const RequiredText = styled.div`
  color: ${style.color.requiredRed};
  font-size: 20px;
`;

const ContentContainer = styled.div`
  padding: 8px;
  width: 80vw;
`;
