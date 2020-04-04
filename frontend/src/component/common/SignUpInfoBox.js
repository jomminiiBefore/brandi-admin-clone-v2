import React, { useState } from "react";
import styled from "styled-components";
import { connect, useSelector, useDispatch } from "react-redux";
import { sendValue, inputValidation } from "../../store/actions";
import Input from "src/component/common/Input";
import Validation from "src/component/common/Validation";

const SignUpInfoBox = ({ sendValue, inputValidation }) => {
  // const storeValue = useSelector(state => state.inputValidation);
  // const dispatch = useDispatch();
  // const [text, setText] = useState("");

  // const checkValue = e => {
  //   //
  // };

  const checkValidation = () => {
    if (text.length > 1) {
      return "필수 입력항목입니다.";
    } else if (text.length > 5) {
      return "아이디의 최소 길이는 5글자입니다.";
    }
  };
  console.log("함수실행!!!!!", checkValidation());
  return (
    <>
      <Container>
        <Input setText={setText} width="410" height="34" placeholder="아이디" />
        <Validation
          validationText={
            text.length > 0 && text.length < 6
              ? "필수 입력 항목입니다."
              : text.length > 5
              ? "아이디의 최소 길이는 5글자입니다."
              : null
          }
        />
      </Container>
    </>
  );
};

// const mapStateToProps = state => {
//   return {
//     inputValidation: state.inputValidation.value
//   };
// };

// export default connect(null, { mapStateToProps })(SignUpInfoBox);
export default SignUpInfoBox;
const Container = styled.div``;
