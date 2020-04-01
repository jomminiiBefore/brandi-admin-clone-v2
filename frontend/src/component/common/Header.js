import React from 'react';
import styled from 'styled-components';

const Header = () => {
  return (
    <Container>
      <LogoImage src="http://sadmin.brandi.co.kr/include/img/logo_2.png" />
    </Container>
  );
};

export default Header;

const Container = styled.div`
  display: flex;
  align-items: center;
  width: 100vw;
  height: 45px;
  background-color: #873a52;
`;

const LogoImage = styled.img`
  width: 140px;
  padding: 0 20px;
`;
