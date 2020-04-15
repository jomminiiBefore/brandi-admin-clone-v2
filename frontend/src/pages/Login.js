import React, { useState } from 'react';
import { withRouter } from 'react-router-dom';
import styled from 'styled-components';
import { YJURL, JMURL } from 'src/utils/config';
import InputContainer from 'src/component/common/InputContainer';
import CustomButton from 'src/component/common/CustomButton';
import Footer from 'src/component/common/Footer';
import styles from 'src/utils/styles';

const Login = (props) => {
  const [inputs, setInputs] = useState({
    login_id: '',
    password: '',
  });

  const onChange = (e) => {
    console.log('e.target.value: ', e.target.value);
    setInputs({ ...inputs, [e.target.name]: e.target.value });
  };

  const goToSignUp = () => {
    props.history.push('/signup');
  };

  // login fetch 함수
  const handleLogin = () => {
    console.log('password:: ', inputs.password);
    fetch(`${JMURL}/seller/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        login_id: inputs.login_id,
        password: inputs.password,
      }),
    })
      .then((res) => res.json())
      .then((res) => {
        console.log('login-res:: ', res);
        if (res.token) {
          localStorage.setItem('token', res.token);
          props.history.push('/loginOk');
        } else {
          alert('아이디 또는 패스워드를 확인해주세요.');
        }
        return res;
      })
      .catch((error) => console.log('error::: ', error));
  };

  return (
    <Container>
      <BgBox>
        <BgImage />
      </BgBox>
      <LoginBox>
        <InputBox>
          <MainTitle>셀러 로그인</MainTitle>
          <Wrapper>
            <InputContainer
              width="300"
              height="34"
              placeholder="셀러 아이디"
              name="login_id"
              setText={onChange}
              setBlur={onChange}
            />
          </Wrapper>
          <Wrapper>
            {/* <InputContainer
              width="300"
              height="34"
              placeholder="호"
              name="password"
              setText={onChange}
              setBlur={onChange}
            /> */}
            <PasswordInput
              type="password"
              name="password"
              placeholder="셀러 비밀번호"
              onChange={onChange}
            />
          </Wrapper>
        </InputBox>
        <SellerInfoBox>
          <InputCheckbox type="checkbox" />
          <RememberInfo>아이디/비밀번호 기억하기</RememberInfo>
          <FindPw>비밀번호 찾기</FindPw>
        </SellerInfoBox>
        <ButtonBox>
          <CustomButton name={'셀러가입'} onClickEvent={goToSignUp} />
          <CustomButton
            name={'로그인'}
            textColor={'white'}
            color={styles.color.buttonBlue}
            onClickEvent={handleLogin}
          />
        </ButtonBox>
        <HelpiLink
          href="https://www.notion.so/HELPI-f24864d9056c4d2a8b988a07814d5c7f"
          target="_blank"
        >
          <HelpiImg />
        </HelpiLink>
        <BottomInfoBox>
          <InfoText>
            입점안내{' '}
            <ShowInfo href="http://www.brandiinc.com/brandi/" target="_blank">
              보러가기
            </ShowInfo>
          </InfoText>
          <ServiceCenterNumber>고객센터</ServiceCenterNumber>
          <RepNumber>| 대표번호 : 1566-1910</RepNumber>
          <Kakaofriend>
            | 카카오톡 플러스친구 :{' '}
            <KakaoBrandi href="https://pf.kakao.com/_pSxoZu" target="_blank">
              @브랜디셀러
            </KakaoBrandi>
          </Kakaofriend>
        </BottomInfoBox>
      </LoginBox>
      <BottomEmpty />
      <Footer />
    </Container>
  );
};

export default withRouter(Login);

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
  background-image: url('http://sadmin.brandi.co.kr/include/img/logo_seller_admin_1.png');
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

const Wrapper = styled.div`
  margin-top: 10px;
`;

const PasswordInput = styled.input`
  width: 300px;
  height: 34px;
  padding: 10px;
  border: 1px solid #e5e5e5;
  border-radius: 4px;
  color: #333333;
  font-size: ${styles.fontSize.generalFont};
  &:focus {
    border: 1px solid #e5e5e5;
  }
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

const ButtonBox = styled.div`
  margin: 20px 0px 15px 0px;
  display: flex;
`;

const HelpiLink = styled.a``;

const HelpiImg = styled.img`
  width: 360px;
  height: 120px;
  margin: 15px 0px;
  background-size: cover;
  background-image: url('http://sadmin.brandi.co.kr/include/img/admin_mainbn_helpi.png');
`;

const BottomInfoBox = styled.div`
  margin-right: 70px;
  line-height: 25px;
`;

const InfoText = styled.div`
  font-weight: ${styles.fontWeight.thin};
`;

const ShowInfo = styled.a`
  color: ${styles.color.buttonBlue};
  font-weight: ${styles.fontWeight.thin};
  &:hover {
    border-bottom: 1px solid ${styles.color.buttonBlue};
  }
`;

const ServiceCenterNumber = styled.div`
  font-size: ${styles.fontWeight.thin};
  font-weight: ${styles.fontWeight.thin};
`;

const RepNumber = styled.div`
  font-size: ${styles.fontSize.generalFont};
`;

const Kakaofriend = styled.div`
  font-size: ${styles.fontSize.generalFont};
`;

const KakaoBrandi = styled.a`
  color: ${styles.color.buttonBlue};
  &:hover {
    border-bottom: 1px solid ${styles.color.buttonBlue};
  }
`;

const BottomEmpty = styled.div`
  padding: 25px;
`;
