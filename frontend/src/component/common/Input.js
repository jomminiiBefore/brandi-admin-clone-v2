import React, { useState } from "react";
import styled from "styled-components";

const Input = props => {
  const [innerText, setInnerText] = useState("");

  return (
    <Container>
      <InputBox
        {...props}
        type="text"
        placeholder={props.placeholder}
        onChange={e => console.log("타겟밸류::", e.target.value)}
      />
    </Container>
  );
};

export default Input;

const Container = styled.div``;

const InputBox = styled.input`
  width: ${props => props.width}px;
  height: ${props => props.height}px;
  margin-top: 15px;
  padding: 10px;
  border: 1px solid #e5e5e5;
  border-radius: 4px;
  color: #333333;
  font-size: 14px;
  &:focus {
    border: 1px solid #333333;
    color: #333333;
  }
`;
