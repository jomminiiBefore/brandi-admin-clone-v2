import React from 'react';
import style from 'src/utils/styles';
import styled from 'styled-components';

const Input = ({
  name,
  placeholder,
  width,
  height,
  setText,
  setBlur,
  typed,
  blurred,
  valid,
  validationText,
  inputText,
  isRequired,
}) => {
  /*
    setText: 텍스트가 바뀌었을 경우

    # typed, blurred, valid: 테두리 색상 변경용 값
      - typed: input에 글자를 한번이라도 입력한 경우 true
      - blurred: focus out이 한번이라도 된 경우 true
      - valid: 정규식 검사 결과
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
      <InputBox
        type="text"
        placeholder={placeholder}
        onChange={(e) => setText(e)}
        onBlur={(e) => setBlur(e)}
        width={width}
        height={height}
        name={name}
        typed={typed}
        blurred={blurred}
        valid={valid}
        isValid={isValid}
        validationText={validationText}
        inputText={inputText}
        isRequired={isRequired}
      />
    </Container>
  );
};

export default Input;

const Container = styled.div``;

const InputBox = styled.input`
  width: ${(props) => props.width}px;
  height: ${(props) => props.height}px;
  padding: 10px;
  border: 1px solid;
  border-color: ${(props) => {
    // validation 유무
    if (props.validationText === 'none') {
      if (props.inputText || !props.typed) {
        return '#e5e5e5';
      } else {
        return style.color.validationRed;
      }
    } else {
      // 필수 입력 유무
      if (props.isRequired) {
        if (props.isValid) {
          return '#e5e5e5';
        } else {
          return style.color.validationRed;
        }
      } else {
        if (props.isValid || !props.inputText) {
          return '#e5e5e5';
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
    border-color: ${(props) => {
      // validation 유무
      if (props.validationText === 'none') {
        if (props.inputText || !props.typed) {
          return '#333333';
        } else {
          return style.color.validationRed;
        }
      } else {
        // 필수 입력 유무
        if (props.isRequired) {
          if (props.isValid) {
            return '#e5e5e5';
          } else {
            return style.color.validationRed;
          }
        } else {
          if (props.isValid || !props.inputText) {
            return '#e5e5e5';
          } else {
            return style.color.validationRed;
          }
        }
      }
    }};
  }
`;
