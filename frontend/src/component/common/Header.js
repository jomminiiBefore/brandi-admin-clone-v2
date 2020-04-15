import React from 'react';
import { withRouter } from 'react-router-dom';
import styled from 'styled-components';

const Header = (props) => {
  const onClickEvent = (e) => {
    localStorage.removeItem('token');
    props.history.push(`/login`);
  };

  return (
    <Container>
      <LogoImage src="http://sadmin.brandi.co.kr/include/img/logo_2.png" />
      <LogoutButtonWrapper>
        <LogoutButton onClick={onClickEvent}>로그아웃</LogoutButton>
      </LogoutButtonWrapper>
    </Container>
  );
};

export default withRouter(Header);

const Container = styled.div`
  display: flex;
  align-items: center;
  height: 45px;
  background-color: #81007f;
  width: 100vw;
  justify-content: space-between;
`;

const LogoImage = styled.img`
  width: 140px;
  padding: 0 20px;
`;

const LogoutButtonWrapper = styled.div`
  margin-right: 20px;
`;

const LogoutButton = styled.div`
  font-size: 15px;
  color: #fff;
  background-color: #0f0f0f;
  padding: 7px;
  border-radius: 4px;

  &:hover {
    background-color: #bdbdbd;
    cursor: pointer;
  }
`;
