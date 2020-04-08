import React from 'react';
import style from 'src/utils/styles';
import styled from 'styled-components';

const InfoText = ({ content }) => {
  return (
    <Container>
      <Text>{content}</Text>
    </Container>
  );
};

export default InfoText;

const Container = styled.div``;

const Text = styled.div`
  padding-top: 10px;
  font-size: 13px;
  color: ${style.color.infoBlue};
`;
