import React from 'react';
import Input from 'src/component/common/Input';
import Validation from 'src/component/common/Validation';
import style from 'src/utils/styles';
import styled from 'styled-components';

const InputContainer = ({
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
  isRequired,
  type,
  disabled,
}) => {
  return (
    <div>
      <Input
        width={width}
        height={height}
        placeholder={placeholder}
        name={name}
        setText={setText}
        setBlur={setBlur}
        typed={typed}
        blurred={blurred}
        valid={valid}
        validationText={validationText}
        inputText={inputText}
        isRequired={isRequired}
        type={type}
        // input 입력 활성화 유무
        disabled={disabled}
      />
      <Validation
        validationText={validationText}
        inputText={inputText}
        typed={typed}
        blurred={blurred}
        valid={valid}
        isRequired={isRequired}
      />
    </div>
  );
};

export default InputContainer;
