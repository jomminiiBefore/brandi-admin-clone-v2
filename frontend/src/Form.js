import React, { useState } from "react";
import ReactDOM from "react-dom";
import styled from "styled-components";
import GlobalStyles from "src/GlobalStyles";

const Button = styled.div`
  color: blue;
  font-weight: bold;
`;

const Form = () => {
  const [value, setValue] = useState("");
  const handleChange = e => {
    const { value } = e.target;
    setValue(value);
  };
  return (
    <form>
      <GlobalStyles></GlobalStyles>
      <Button type="text" value={value} onChange={handleChange}>
        brandi
      </Button>
    </form>
  );
};

export default Form;
const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<Form />, wrapper) : false;
