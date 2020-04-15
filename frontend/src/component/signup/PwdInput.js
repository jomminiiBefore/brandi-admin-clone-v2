import React from "react";
import styled from "styled-components";
import style from "src/utils/styles";

const PwdInput = ({
  width,
  height,
  placeholder,
  name,
  setText,
  setBlur,
  typed,
  blurred,
  valid,
  validationText,
  inputText,
  type,
  isRequired,
  disabled
}) => {
  /*
    setText: 텍스트가 바뀌었을 경우

    typed, blurred, valid: 테두리 색상 변경용 값
      - typed: input안에 값이 한 개라도 들어왔을 경우 true로 변경
      - blurred: input에 focus가 한 번이라도 됐을 경우 true로 변경
      - valid: 정규식 검사 결과에 따라 true로 변경
   */

  let isValid = false;
  if (typed && blurred && valid) {
    isValid = true;
  } else if (typed && blurred && !valid) {
    isValid = false;
  } else {
    isValid = true;
  }
  return (
    <Container>
      {disabled ? (
        <Input
          width={width}
          height={height}
          placeholder={placeholder}
          name={name}
          onChange={e => setText(e)}
          onBlur={e => setBlur(e)}
          typed={typed}
          blurred={blurred}
          valid={valid}
          validationText={validationText}
          inputText={inputText}
          type={type}
          isValid={isValid}
          isRequired={isRequired}
          disabled
        />
      ) : (
        <Input
          width={width}
          height={height}
          placeholder={placeholder}
          name={name}
          onChange={e => setText(e)}
          onBlur={e => setBlur(e)}
          typed={typed}
          blurred={blurred}
          valid={valid}
          validationText={validationText}
          inputText={inputText}
          type={type}
          isValid={isValid}
          isRequired={isRequired}
        />
      )}
    </Container>
  );
};

export default PwdInput;

const Container = styled.div``;

const Input = styled.input`
  width: ${props => props.width}px;
  height: ${props => props.height}px;
  padding: 10px;
  border: 1px solid;
  border-color: ${props => {
    // validation 유무
    if (props.validationText === "none") {
      if (props.inputText || !props.typed) {
        return "#e5e5e5";
      } else {
        return style.color.validationRed;
      }
    } else {
      // 필수 입력 유무
      if (props.isRequired) {
        if (props.isValid) {
          return "#e5e5e5";
        } else {
          return style.color.validationRed;
        }
      } else {
        if (props.isValid || !props.inputText) {
          return "#e5e5e5";
        } else {
          return style.color.validationRed;
        }
      }
    }
  }};
  border-radius: 4px;
  color: #333333;
  font-size: 14px;
  &:focus {
    border: 1px solid;
    border-color: ${props => {
      // validation 유무
      if (props.validationText === "none") {
        if (props.inputText || !props.typed) {
          return "#333333";
        } else {
          return style.color.validationRed;
        }
      } else {
        // 필수 입력 유무
        if (props.isRequired) {
          if (props.isValid) {
            return "#e5e5e5";
          } else {
            return style.color.validationRed;
          }
        } else {
          if (props.isValid || !props.inputText) {
            return "#e5e5e5";
          } else {
            return style.color.validationRed;
          }
        }
      }
    }};
  }
`;
