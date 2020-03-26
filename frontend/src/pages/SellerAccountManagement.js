import React from "react";
import styled from "styled-components";

const SellerAccountManagement = () => {
  return (
    <Container>
      <Title>SellerAccountManagement</Title>
    </Container>
  );
};

export default SellerAccountManagement;

const Container = styled.div`
  display: flex;
  justify-content: center;
`;

const Title = styled.div`
  font-size: 100px;
  font-weight: 600;
`;

// 1. 초기 세팅 완료해서 깃허브에 올림
// 2. 개발모드, 배포모드 환경 구분

// db를 열었으면 close가 반드시 되게끔 해야한다
// finally 라는게 있는게 여기에 db close가 있어야한다
