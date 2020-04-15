import React from "react";
import PwdInput from "src/component/signup/PwdInput";
import PwdValidation from "src/component/signup/PwdValidation";

const PwdInputContainer = ({
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
  disabled
}) => {
  return (
    <div>
      <PwdInput
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
      <PwdValidation
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

export default PwdInputContainer;
