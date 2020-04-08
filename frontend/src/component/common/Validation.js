import React from "react";
import styled from "styled-components";

const Validation = ({
  inputText,
  validationText,
  typed,
  blurred,
  valid,
  isRequired
}) => {
  // console.log(typed, blurred, valid, inputText);
  // inputText: input에 입력한 값 (input에 아무 값도 입력하지 않았을 때 '필수 입력 항목입니다' 메세지 출력 유무를 판단하기 위해 필요)
  // validationText: validationText 메세지 내용 | 텍스트가 none이면 validation이 존재하지 않는 경우다.
  // typed: input에 글자를 한번이라도 입력한 경우 true
  // blurred: focus out이 한번이라도 된 경우 true
  // valid: 정규식 검사 결과

  return (
    <>
      {validationText !== "none" && typed && blurred && inputText && !valid && (
        <Container>
          <ValidationBox>{validationText}</ValidationBox>
        </Container>
      )}
      {typed && blurred && !inputText && !valid && isRequired && (
        <Container>
          <ValidationBox>필수 입력 항목입니다.</ValidationBox>
        </Container>
      )}
    </>
  );
};
export default Validation;

const Container = styled.div``;

const ValidationBox = styled.div`
  width: 410px;
  padding-top: 10px;
  color: #a94442;
  font-size: 13px;
  letter-spacing: 0px;
`;
