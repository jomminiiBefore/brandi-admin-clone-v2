import React from 'react';
import InputContainer from '../common/InputContainer';
import styled from 'styled-components';

const ManagerInfoItem = ({ managerInfo, setValue, setBlur }) => {
  return (
    <>
      <InputContainer
        width={287}
        height={34}
        placeholder="셀러 한글명"
        name="koreanName"
        setText={setValue}
        setBlur={setBlur}
        typed={isTyped.koreanName}
        blurred={isBlurred.koreanName}
        valid={isValid.koreanName}
        validationText="한글, 영문, 숫자만 입력해주세요."
        inputText={koreanName}
        isRequired={true}
      />
      <InputWrapper>
        <InputContainer
          width={287}
          height={34}
          placeholder="셀러 한글명"
          name="koreanName"
          setText={setValue}
          setBlur={setBlur}
          typed={isTyped.koreanName}
          blurred={isBlurred.koreanName}
          valid={isValid.koreanName}
          validationText="한글, 영문, 숫자만 입력해주세요."
          inputText={koreanName}
          isRequired={true}
        />
      </InputWrapper>
      <InputWrapper>
        <InputContainer
          width={287}
          height={34}
          placeholder="셀러 한글명"
          name="koreanName"
          setText={setValue}
          setBlur={setBlur}
          typed={isTyped.koreanName}
          blurred={isBlurred.koreanName}
          valid={isValid.koreanName}
          validationText="한글, 영문, 숫자만 입력해주세요."
          inputText={koreanName}
          isRequired={true}
        />
      </InputWrapper>
    </>
  );
};

export default ManagerInfoItem;

const InputWrapper = styled.div`
  margin-top: 5px;
`;
