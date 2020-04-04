import React from "react";
import styled from "styled-components";
import styles from "src/utils/styles";

const Footer = () => {
  return (
    <Container>
      <p>
        | 상호 : (주)브랜디 | 주소 : (06223) 서울특별시 강남구 테헤란로 32길 26
        청송빌딩 | 사업자등록번호 : 220-88-93187 | 통신판매업신고 :
        2016-서울강남-00359호 | 이메일 : help@brandi.co.kr
      </p>
      <p>2018 © brandi inc. </p>
    </Container>
  );
};

export default Footer;

const Container = styled.div`
  width: 100vw;
  padding: 20px;
  color: #999ba2;
  font-size: ${styles.fontSize.generalFont};
  text-align: center;
  line-height: 20px;
  background-color: #35363a;
`;
