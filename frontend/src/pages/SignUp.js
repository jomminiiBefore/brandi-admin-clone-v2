import React, { useState } from "react";
import { withRouter } from "react-router-dom";
import styled from "styled-components";
import { JMURL, YJURL } from "src/utils/config";
import InputContainer from "src/component/common/InputContainer";
import CustomButton from "src/component/common/CustomButton";
import Footer from "src/component/common/Footer";
import {
  id_start,
  check_id,
  len_four,
  cellphone_num,
  check_num,
  korean_english_number,
  lower_case,
  check_url
} from "src/utils/regexp";
import styles from "src/utils/styles";

const SignUp = props => {
  const [inputs, setInputs] = useState({
    id: "",
    password: "",
    rePassword: "",
    cellphoneNumber: "",
    sellerName: "",
    sellerEngName: "",
    servicecenterNumber: "",
    siteUrl: "",
    kakaoId: "",
    instaId: ""
  });

  const {
    id,
    password,
    rePassword,
    cellphoneNumber,
    sellerName,
    sellerEngName,
    servicecenterNumber,
    siteUrl,
    kakaoId,
    instaId
  } = inputs;

  // input안에 값이 한 개라도 들어왔을 경우 true로 변경
  const [isTyped, setIsTyped] = useState({
    id: false,
    password: false,
    rePassword: false,
    cellphoneNumber: false,
    sellerName: false,
    sellerEngName: false,
    servicecenterNumber: false,
    siteUrl: false
  });

  // input에 focus가 한 번이라도 됐을 경우 true로 변경
  const [isBlurred, setIsBlurred] = useState({
    id: false,
    password: false,
    rePassword: false,
    cellphoneNumber: false,
    sellerName: false,
    sellerEngName: false,
    servicecenterNumber: false,
    siteUrl: false
  });

  // 정규식 검사 결과에 따라 true로 변경
  const [isValid, setIsValid] = useState({
    id: false,
    password: false,
    rePassword: false,
    cellphoneNumber: false,
    sellerName: false,
    sellerEngName: false,
    servicecenterNumber: false,
    siteUrl: false
  });

  // 정규식 검사하는 함수
  const setValue = e => {
    const { name, value } = e.target;
    setInputs({ ...inputs, [name]: value });
    setIsTyped({ ...inputs, [name]: true });

    if (name === "id") {
      if (id_start.test(value) && check_id.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === "password") {
      if (len_four.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === "rePassword") {
      if (len_four.test(value)) {
        setIsValid({
          ...isValid,
          [name]: password === value ? true : false
        });
      }
    } else if (name === "cellphoneNumber") {
      if (cellphone_num.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === "sellerName") {
      if (korean_english_number.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === "sellerEngName") {
      if (lower_case.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === "servicecenterNumber") {
      if (check_num.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === "siteUrl") {
      if (check_url.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    }
  };

  const setBlur = e => {
    setIsBlurred({ ...isBlurred, [e.target.name]: true });
  };

  // RadioButton
  const [sellerTypeId, setSellerTypeId] = useState("");

  const onChangeRadio = e => {
    setSellerTypeId(e.target.value);
    console.log(e.target.value);
  };

  const goToLogin = () => {
    if (confirm("브랜디 가입을 취소하시겠습니까?")) {
      props.history.push("/login");
    } else {
    }
  };

  // const infoModified = () => {
  //   console.log("isValid:: ", Object.values(isValid).includes(false));
  //   if (Object.values(isValid).includes(false)) {
  //     alert("작성하신 정보를 다시 확인해주세요.");
  //   }
  // };

  // signUp fetch 함수
  const handleSignUp = () => {
    fetch(`${JMURL}/seller`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        login_id: id,
        password: password,
        contact_number: cellphoneNumber,
        seller_type_id: sellerTypeId,
        name_kr: sellerName,
        name_en: sellerEngName,
        center_number: servicecenterNumber,
        site_url: siteUrl,
        kakao_id: kakaoId ? kakaoId : null,
        insta_id: instaId ? instaId : null
      })
    })
      .then(res => res.json())
      .then(res => {
        console.log("signup-res:: ", res);
        if (confirm("입력하신 정보로 셀러신청을 하시겠습니까?")) {
          alert(
            "신청이 완료되었습니다. 검토 후 연락 드리겠습니다. 감사합니다."
          );
          props.history.push("/login");
        } else {
        }
      })
      .catch(error => console.log("error::: ", error));
  };

  return (
    <Container>
      <BgBox>
        <BgImage />
      </BgBox>
      <SignUpBox>
        <MainTitle>셀러 회원 가입</MainTitle>
        <Border />
        <Img></Img>
        <InputBox>
          <SubTitle>가입정보</SubTitle>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="아이디"
              name="id"
              isRequired={true}
              setText={setValue}
              setBlur={setBlur}
              inputText={id}
              typed={isTyped.id}
              blurred={isBlurred.id}
              valid={isValid.id}
              validationText="아이디는 5~20글자의 영문, 숫자, 언더바, 하이픈만 사용 가능하며 시작 문자는 영문 또는 숫자입니다."
            />
          </Wrapper>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="비밀번호"
              name="password"
              isRequired={true}
              setText={setValue}
              setBlur={setBlur}
              inputText={password}
              typed={isTyped.password}
              blurred={isBlurred.password}
              valid={isValid.password}
              validationText="비밀번호의 최소 길이는 4글자입니다."
            />
          </Wrapper>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="비밀번호 재입력"
              name="rePassword"
              isRequired={false}
              setText={setValue}
              setBlur={setBlur}
              inputText={rePassword}
              typed={isTyped.rePassword}
              blurred={isBlurred.rePassword}
              valid={isValid.rePassword}
              validationText="비밀번호가 일치하지 않습니다."
            />
          </Wrapper>
          <SubTitle>담당자 정보</SubTitle>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="핸드폰번호"
              name="cellphoneNumber"
              isRequired={true}
              setText={setValue}
              setBlur={setBlur}
              inputText={cellphoneNumber}
              typed={isTyped.cellphoneNumber}
              blurred={isBlurred.cellphoneNumber}
              valid={isValid.cellphoneNumber}
              validationText="올바른 정보를 입력해주세요."
            />
            <ManagerText>
              입점 신청 후 브랜디 담당자가 연락을 드릴 수 있으니 정확한 정보를
              기입해주세요.
            </ManagerText>
          </Wrapper>
          <SubTitle>셀러 정보</SubTitle>
          <RadioButtonContainer>
            <TopInnerBox>
              <InputButtonBox>
                <input
                  type="radio"
                  id="designer"
                  name="brand"
                  value="1"
                  onChange={onChangeRadio}
                />
                <label>쇼핑몰</label>
              </InputButtonBox>
              <InputButtonBox>
                <input
                  type="radio"
                  id="designer"
                  name="brand"
                  value="2"
                  onChange={onChangeRadio}
                />
                <label>마켓</label>
              </InputButtonBox>
              <InputButtonBox>
                <input
                  type="radio"
                  id="designer"
                  name="brand"
                  value="3"
                  onChange={onChangeRadio}
                />
                <label>로드샵</label>
              </InputButtonBox>
              <InputButtonBox>
                <input
                  type="radio"
                  id="designer"
                  name="brand"
                  value="4"
                  onChange={onChangeRadio}
                />
                <label>디자이너브랜드</label>
              </InputButtonBox>
            </TopInnerBox>
            <BottomInnerBox>
              <InputButtonBox>
                <input
                  type="radio"
                  id="designer"
                  name="brand"
                  value="5"
                  onChange={onChangeRadio}
                />
                <label>제너럴브랜드</label>
              </InputButtonBox>
              <InputButtonBox>
                <input
                  type="radio"
                  id="designer"
                  name="brand"
                  value="6"
                  onChange={onChangeRadio}
                />
                <label>내셔널브랜드</label>
              </InputButtonBox>
              <InputButtonBox>
                <input
                  type="radio"
                  id="designer"
                  name="brand"
                  value="7"
                  onChange={onChangeRadio}
                />
                <label>뷰티</label>
              </InputButtonBox>
            </BottomInnerBox>
          </RadioButtonContainer>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="셀러명 (상호)"
              name="sellerName"
              isRequired={true}
              setText={setValue}
              setBlur={setBlur}
              inputText={sellerName}
              typed={isTyped.sellerName}
              blurred={isBlurred.sellerName}
              valid={isValid.sellerName}
              validationText="한글, 영문 ,숫자만 입력해주세요."
            />
          </Wrapper>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="영문 셀러명 (영문상호)"
              name="sellerEngName"
              isRequired={true}
              setText={setValue}
              setBlur={setBlur}
              inputText={sellerEngName}
              typed={isTyped.sellerEngName}
              blurred={isBlurred.sellerEngName}
              valid={isValid.sellerEngName}
              validationText="셀러 영문명은 소문자만 입력가능합니다."
            />
          </Wrapper>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="고객센터 전화번호"
              name="servicecenterNumber"
              isRequired={true}
              setText={setValue}
              setBlur={setBlur}
              inputText={servicecenterNumber}
              typed={isTyped.servicecenterNumber}
              blurred={isBlurred.servicecenterNumber}
              valid={isValid.servicecenterNumber}
              validationText="고객센터 전화번호는 숫자와 하이픈만 입력가능합니다."
            />
          </Wrapper>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="사이트 URL"
              name="siteUrl"
              isRequired={true}
              setText={setValue}
              setBlur={setBlur}
              inputText={siteUrl}
              typed={isTyped.siteUrl}
              blurred={isBlurred.siteUrl}
              valid={isValid.siteUrl}
              validationText="올바른 주소를 입력해주세요. (ex. http://www.brandi.co.kr)"
            />
          </Wrapper>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="카카오톡 아이디"
              name="kakaoId"
              isRequired={false}
              setText={setValue}
              setBlur={setBlur}
              inputText={kakaoId}
              validationText="none"
            />
          </Wrapper>
          <Wrapper>
            <InputContainer
              width="410"
              height="34"
              placeholder="인스타그램 아이디"
              name="instaId"
              isRequired={false}
              setText={setValue}
              setBlur={setBlur}
              inputText={instaId}
              validationText="none"
            />
          </Wrapper>
        </InputBox>
        <ButtonBox>
          <CustomButton
            name={"신청"}
            textColor={"white"}
            color={styles.color.buttonBlue}
            onClickEvent={handleSignUp}
          />
          <CustomButton
            name={"취소"}
            textColor={"white"}
            color={styles.color.buttonRed}
            onClickEvent={goToLogin}
          />
        </ButtonBox>
      </SignUpBox>
      <BottomEmpty />

      <Footer />
    </Container>
  );
};

export default withRouter(SignUp);

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

const ManagerText = styled.p`
  margin-top: 10px;
  padding-left: 5px;
  color: ${styles.color.infoBlue};
  font-size: 12px;
  letter-spacing: 0px;
`;

const Wrapper = styled.div`
  margin-top: 10px;
`;

const RadioButtonContainer = styled.div`
  width: 410px;
  margin-top: 10px;
`;

const TopInnerBox = styled.div`
  display: flex;
`;

const BottomInnerBox = styled.div`
  display: flex;
`;

const InputButtonBox = styled.div`
  margin: 0px 10px;
  font-size: 13px;
`;

const ButtonBox = styled.div`
  margin-top: 30px;
  display: flex;
`;

const BottomEmpty = styled.div`
  padding: 25px;
`;
