import React from "react";
import styled from "styled-components";

const Login = () => {
  return (
    <Container>
      <BGImage />
    </Container>
  );
};

export default Login;

const Container = styled.div`
  display: flex;
  justify-content: center;
  margin-top: 60px;
`;

const BGImage = styled.div`
  background-image: url("http://sadmin.brandi.co.kr/include/img/logo_seller_admin_1.png");
  width: 300px;
  height: 150px;
  background-repeat: no-repeat;
`;
