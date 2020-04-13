import React from "react";
import style from "src/utils/styles";
import styled from "styled-components";

/*
 * Author: Seungjune
 * 커스텀 버튼
 */

const CustomButton = ({
  name,
  color,
  textColor,
  onClickEvent,
  managerLength,
}) => {
  // console.log('onclicke:: ', onClickEvent);
  return (
    <Container onClick={onClickEvent}>
      <ButtonWrapper color={color}>
        <ButtonText textColor={textColor}>{name}</ButtonText>
      </ButtonWrapper>
    </Container>
  );
};

export default CustomButton;

const Container = styled.span`
  display: inline-block;
  margin-right: 3px;
`;

const ButtonWrapper = styled.span`
  display: inline-block;
  padding: 6px 12px;
  border: 1px solid #e5e5e5;
  border-radius: 4px;
  cursor: pointer;
  &:hover {
    filter: ${style.filter.brightness};
  }
  background-color: ${(props) => props.color};
`;

const ButtonText = styled.span`
  font-size: 13px;
  color: ${(props) => props.textColor};
`;
