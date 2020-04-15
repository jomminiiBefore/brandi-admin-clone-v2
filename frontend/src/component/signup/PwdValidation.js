import React from "react";
import styled from "styled-components";

const PwdValidation = ({
  inputText,
  validationText,
  typed,
  blurred,
  valid,
  isRequired
}) => {
  return (
    // inputText: input에 입력한 값 (input에 아무 값도 입력하지 않았을 때 '필수 입력 항목입니다' 메세지 출력 유무를 판단하기 위해 필요)
    // validationText: validationText 메세지 내용 (텍스트가 none이면 validation이 존재하지 않을 경우)
    // typed: input안에 값이 한 개라도 들어왔을 경우 true로 변경
    // blurred: input에 focus가 한 번이라도 됐을 경우 true로 변경
    // valid: 정규식 검사 결과에 따라 true로 변경
    <>
      {validationText !== "none" && typed && blurred && inputText && !valid && (
        <Container>
          <Validation>{validationText}</Validation>
        </Container>
      )}
      {typed && blurred && !inputText && !valid && isRequired && (
        <Container>
          <Validation>필수 입력 항목입니다.</Validation>
        </Container>
      )}
    </>
  );
};

export default PwdValidation;

const Container = styled.div``;

const Validation = styled.div`
  width: 410px;
  padding-top: 10px;
  color: #a94442;
  font-size: 13px;
  letter-spacing: 0px;
`;
