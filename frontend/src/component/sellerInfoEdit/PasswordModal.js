import React, { useState } from 'react';
import CustomButton from 'src/component/common/CustomButton';
import { JMURL } from 'src/utils/config';
import { four_length_case } from 'src/utils/regexp';
import style from 'src/utils/styles';
import styled, { keyframes, css } from 'styled-components';

const PasswordModal = ({ showPasswordModal }) => {
  // 비밀번호 변경
  const onChangePassword = () => {
    if (!input.password) {
      alert('변경할 비밀번호를 입력하세요.');
    } else if (!input.rePassword) {
      alert('변경할 비밀번호를 한번 더 입력해주세요.');
    } else if (input.password === input.rePassword) {
      if (four_length_case.test(input.password)) {
        if (confirm('비밀번호를 변경하시겠습니까?')) {
          changePassword();
        }
      } else {
        alert('비밀번호의 최소 길이는 4글자입니다.');
      }
    } else {
      alert('비밀번호가 일치하지 않습니다.');
    }
  };

  const changePassword = () => {
    fetch(`${JMURL}/seller/5/password`, {
      method: 'PUT',
      headers: {
        Authorization: localStorage.getItem('token'),
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        original_password: null,
        new_password: input.password,
      }),
    })
      .then((res) => res.json())
      .then((res) => {
        if (res.message === 'SUCCESS') {
          alert('비밀번호가 변경되었습니다.');
          showPasswordModal();
        }
      });
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
          <InputForm
            name="password"
            onChange={(e) => onSetText(e)}
            type="password"
          />
          <InputTitle>비밀번호 재입력</InputTitle>
          <InputForm
            name="rePassword"
            onChange={(e) => onSetText(e)}
            type="password"
          />
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
