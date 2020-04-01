import React from "react";
import styled from "styled-components";

const TitleText = props => {
  return <Container {...props}>{props.title}</Container>;
};

export default TitleText;

const Container = styled.div`
  margin-top: 25px;
  font-size: ${props => props.fontSize}px;
  font-weight: 300;
`;
