import React from "react";
import styled from "styled-components";
import Input from "src/component/common/Input";
import Footer from "src/component/common/Footer";
import styles from "src/utils/styles";

const Login = () => {
  return (
    <Container>
      <BgBox>
        <BgImage />
      </BgBox>
      <LoginBox>
        <InputBox>
          <MainTitle>셀러 로그인</MainTitle>
          <Input width="300" height="34" placeholder="셀러 아이디" />
          <Input width="300" height="34" placeholder="셀러 비밀번호" />
        </InputBox>
        <SellerInfoBox>
          <InputCheckbox type="checkbox" />
          <RememberInfo>아이디/비밀번호 기억하기</RememberInfo>
          <FindPw>비밀번호 찾기</FindPw>
        </SellerInfoBox>
        <HelpiImg />
        <BottomInfoBox>
          <div style={{ fontWeight: "300" }}>
            입점안내{" "}
            <span
              style={{ color: `${styles.color.buttonBlue}`, fontWeight: "200" }}
            >
              보러가기
            </span>
          </div>
          <div style={{ fontWeight: "300" }}>고객센터</div>
          <div style={{ fontSize: "13px" }}>| 대표번호 : 1566-1910</div>
          <div style={{ fontSize: "13px" }}>
            | 카카오톡 플러스친구 :{" "}
            <span style={{ color: `${styles.color.buttonBlue}` }}>
              @브랜디셀러
            </span>
          </div>
        </BottomInfoBox>
      </LoginBox>
      <div style={{ padding: "25px" }}></div>
      <Footer />
    </Container>
  );
};

export default Login;

const Container = styled.div`
  width: 100vw;
  height: 100vh;
  background-color: #fafafa;
`;

const BgBox = styled.div`
  display: flex;
  justify-content: center;
  padding-top: 60px;
`;

const BgImage = styled.div`
  width: 130px;
  height: 52px;
  margin-bottom: 15px;
  background-image: url("http://sadmin.brandi.co.kr/include/img/logo_seller_admin_1.png");
  background-size: cover;
  background-repeat: no-repeat;
`;

const LoginBox = styled.div`
  width: 360px;
  margin: 0px auto;
  padding: 20px 0px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff;
`;

const MainTitle = styled.div`
  margin: 25px 170px 10px 0px;
  font-size: ${styles.fontSize.mainTitle};
  font-weight: ${styles.fontWeight.thin};
`;

const InputBox = styled.div`
  display: flex;
  align-items: center;
  flex-direction: column;
`;

const SellerInfoBox = styled.div`
  margin-top: 25px;
  display: flex;
  align-items: center;
`;

const InputCheckbox = styled.input`
  margin-right: 5px;
  border: 1px solid blue;
`;

const RememberInfo = styled.div`
  margin-right: 35px;
  font-size: ${styles.fontSize.generalFont};
`;

const FindPw = styled.div`
  color: ${styles.color.buttonBlue};
  font-size: ${styles.fontSize.generalFont};
`;

const HelpiImg = styled.img`
  width: 360px;
  height: 120px;
  margin: 15px 0px;
  background-size: cover;
  background-image: url("http://sadmin.brandi.co.kr/include/img/admin_mainbn_helpi.png");
`;

const BottomInfoBox = styled.div`
  margin-right: 70px;
  line-height: 25px;
`;
