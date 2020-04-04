import React, { useState } from "react";
import styled from "styled-components";
import SignUpInfoBox from "src/component/common/SignUpInfoBox";
import Input from "src/component/common/Input";
import Validation from "src/component/common/Validation";
import Footer from "src/component/common/Footer";
import styles from "src/utils/styles";

const SignUp = () => {
  return (
    <Container>
      <BgBox>
        <BgImage />
      </BgBox>
      <SignUpBox>
        <MainTitle>셀러 회원 가입</MainTitle>
        <Border></Border>
        <Img></Img>
        <InputBox>
          <SubTitle>가입정보</SubTitle>
          <div>
            <Input width="410" height="34" placeholder="아이디" />
            <Validation />
          </div>
          <div>
            <Input width="410" height="34" placeholder="비밀번호" />
            <Validation ValidationText="비밀번호의 최소 길이는 4글자입니다." />
          </div>
          <div>
            <Input width="410" height="34" placeholder="비밀번호 재입력" />
            <Validation ValidationText="비밀번호가 일치하지 않습니다." />
          </div>
          <SubTitle>담당자 정보</SubTitle>
          <SubTitle>셀러 정보</SubTitle>
        </InputBox>
      </SignUpBox>
      <div style={{ padding: "25px" }}></div>
      <Footer />
    </Container>
  );
};

export default SignUp;

const Container = styled.div`
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

const SignUpBox = styled.div`
  width: 500px;
  margin: 0px auto;
  padding: 20px 0px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff;
`;

const MainTitle = styled.div`
  margin-top: 25px;
  font-size: ${styles.fontSize.mainTitle};
  font-weight: ${styles.fontWeight.thin};
`;

const Border = styled.div`
  width: 440px;
  margin-top: 15px;
  border: 1px solid #eee;
`;

const Img = styled.img`
  width: 408px;
  height: 45px;
  margin-top: 20px;
  background-image: url("http://sadmin.brandi.co.kr/include/img/seller_join_top_2.png");
`;

const InputBox = styled.div`
  display: flex;
  align-items: center;
  flex-direction: column;
`;

const SubTitle = styled.div`
  margin-top: 25px;
  margin-right: 325px;
  font-size: ${styles.fontSize.subTitle};
  font-weight: ${styles.fontWeight.thin};
`;
