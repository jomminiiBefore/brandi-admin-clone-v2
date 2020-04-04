import React from "react";
import styled from "styled-components";

const Validation = props => {
  console.log(props);
  return (
    <Container>
      <ValidationBox>{props.validationText}</ValidationBox>
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
