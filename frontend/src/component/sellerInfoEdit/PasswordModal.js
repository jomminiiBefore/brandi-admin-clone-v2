import React, { useState } from 'react';
import CustomButton from 'src/component/common/CustomButton';
import style from 'src/utils/styles';
import styled, { keyframes, css } from 'styled-components';

const PasswordModal = ({ showPasswordModal }) => {
  const onChangePassword = () => {
    fetch(`${JMURL}/seller/5/password`, {
      headers: {
        Authorization:
          'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
      },
    })
      .then((res) => res.json())
      .then((res) => {});
  };

  const [input, setInput] = useState({ password: '', rePassword: '' });

  const onSetText = (e) => {
    setInput({ ...input, [e.target.name]: e.target.value });
  };
  console.log(input.password, input.rePassword);
  return (
    <>
      <Container></Container>
      <ModalContainer>
        <ModalHeader>비밀번호 변경하기</ModalHeader>
        <ModalBody>
          <InputTitle>변경할 비밀번호</InputTitle>
          <InputForm name="password" onChange={(e) => onSetText(e)} />
          <InputTitle>비밀번호 재입력</InputTitle>
          <InputForm name="rePassword" onChange={(e) => onSetText(e)} />
        </ModalBody>
        <ModalFooter>
          <CustomButton name="취소" onClickEvent={showPasswordModal} />
          <CustomButton
            name="변경"
            color="#5CB85B"
            textColor="#fff"
            onClickEvent={(e) => onChangePassword(e)}
          />
        </ModalFooter>
      </ModalContainer>
    </>
  );
};

export default PasswordModal;

const Container = styled.div`
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  background-color: #000;
  opacity: 0.5;
  animation-fill-mode: forwards;
  ${(props) => {
    return css`
      animation: ${fadeIn} 0.2s linear;
    `;
  }}
`;

const fadeIn = keyframes`
	from {
		opacity: 0;
	}
	to {
		opacity: 0.5;
	}
`;

const ModalContainer = styled.div`
  position: fixed; /* Stay in place */
  z-index: 2; /* Sit on top */
  background-color: #fff;
  margin-left: 150px;
  border-radius: 4px;
  ${(props) => {
    return css`
      animation: ${moveDown} 0.1s linear;
      animation-delay: 0.4s;
      animation-fill-mode: forwards;
    `;
  }};
`;

const moveDown = keyframes`
    from { 
        top: -100px
    }to { 
        top:200px
    }
`;

const ModalHeader = styled.div`
  display: flex;
  align-self: center;
  width: 398px;
  height: 56px;
  font-size: 18px;
  padding: 15px;
`;

const ModalBody = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  width: 398px;
  height: 192px;
  border-top: 1px solid #bdbdbd;
  border-bottom: 1px solid #bdbdbd;
  padding: 15px 25px;
`;

const ModalFooter = styled.div`
  display: flex;
  justify-content: flex-end;
  width: 398px;
  height: 65px;
  padding: 15px;
`;

const InputTitle = styled.div`
  font-size: 14px;
`;

const InputForm = styled.input`
  border: 1px solid #bdbdbd;
  border-radius: 4px;
  padding: 6px 12px;
  width: 338px;
  height: 34px;

  &:focus {
    border: 1px solid #000;
  }
`;
