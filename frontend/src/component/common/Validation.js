import React from "react";
import styled from "styled-components";

const Validation = props => {
  return (
    <Container>
      <ValidationBox {...props}>{props.ValidationText}</ValidationBox>
    </Container>
  );
};

export default Validation;

const Container = styled.div``;

const ValidationBox = styled.div`
  padding-top: 10px;
  color: #a94442;
  font-size: 13px;
  letter-spacing: 0px;
`;
