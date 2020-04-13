import React from "react";
import { withRouter } from "react-router-dom";
import styled from "styled-components";
import CustomButton from "src/component/common/CustomButton";
import styles from "src/utils/styles";

const LoginOk = props => {
  const handleMain = () => {
    props.history.push("/seller");
  };

  return (
    <Container>
      <BgBox>
        <BgImage />
      </BgBox>
      <TitleBox>
        <Border />
        <MainTitle>로그인이 정상적으로 완료되었습니다!</MainTitle>
        <Border />
        <ButtonBox>
          <CustomButton
            name={"메인페이지로 이동하기"}
            textColor={"white"}
            color={styles.color.buttonGreen}
            onClickEvent={handleMain}
          />
        </ButtonBox>
      </TitleBox>
    </Container>
  );
};

export default withRouter(LoginOk);

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

const TitleBox = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;
const MainTitle = styled.div`
  margin-top: 15px;
  color: ${styles.color.buttonGreen};
  font-size: ${styles.fontSize.mainTitle};
  font-weight: ${styles.fontWeight.bold};
`;

const Border = styled.div`
  width: 440px;
  margin-top: 15px;
  border: 1px solid #eee;
  text-align: center;
`;

const ButtonBox = styled.div`
  margin-top: 45px;
`;
