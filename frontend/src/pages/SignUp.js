import React, { useState } from "react";
import styled from "styled-components";
import TitleText from "src/component/common/TitleText";
import Input from "src/component/common/Input";
import Validation from "src/component/common/Validation";

const SignUp = () => {
  const [vali, setVali] = useState("");

  return (
    <Container>
      <BgBox>
        <BgImage />
      </BgBox>
      <SignUpBox>
        <TitleText title="셀러 회원 가입" fontSize="24" />
        <Border></Border>
        <Img></Img>
        <InputBox>
          <TitleText
            title="가입 정보"
            fontSize="18"
            style={{ marginRight: "330px" }}
          />
          <div>
            <Input
              width="410"
              height="34"
              placeholder="아이디"
              setVali={setVali}
            />
            <Validation ValidationText="아이디의 최소 길이는 5글자입니다." />
          </div>
          <div>
            <Input width="410" height="34" placeholder="비밀번호" />
            <Validation ValidationText="비밀번호의 최소 길이는 4글자입니다." />
          </div>
          <div>
            <Input width="410" height="34" placeholder="비밀번호 재입력" />
            <Validation ValidationText="비밀번호가 일치하지 않습니다." />
          </div>
          <TitleText
            title="담당자 정보"
            fontSize="18"
            style={{ marginRight: "320px" }}
          />
          <div>
            <Input width="410" height="34" placeholder="핸드폰번호" />
            <Validation ValidationText="올바른 정보를 입력해주세요." />
            <Validation
              ValidationText=" 입점 신청 후 브랜디 담당자가 연락을 드릴 수 있으니 정확한 정보를 기입해주세요."
              style={{ color: "#1e8fff", fontSize: "12px" }}
            />
          </div>
          <TitleText
            title="셀러 정보"
            fontSize="18"
            style={{ marginRight: "330px" }}
          />
          <div>
            <Input width="410" height="34" placeholder="샐러명 (상호)" />
            <Validation ValidationText="한글, 영문, 숫자만 입력해주세요." />
          </div>
          <div>
            <Input
              width="410"
              height="34"
              placeholder="영문 셀러명 (영문상호)"
            />
            <Validation ValidationText="셀러 영문명은 소문자만 입력가능합니다." />
          </div>
          <div>
            <Input width="410" height="34" placeholder="고객센터 전화번호" />
            <Validation ValidationText="고객선터 전화번호는 숫자와 하이픈만 입력가능합니다." />
          </div>
          <div>
            <Input width="410" height="34" placeholder="사이트 URL" />
            <Validation ValidationText="올바른 주소를 입력해주세요. (ex. http://www.brandi.co.kr)" />
          </div>
          <div>
            <Input width="410" height="34" placeholder="카카오톡 아이디" />
          </div>
          <div>
            <Input width="410" height="34" placeholder="인스타그램 아이디" />
            <Validation ValidationText="올바른 인스타그램 아이디를 입력해주세요." />
          </div>
        </InputBox>
      </SignUpBox>
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
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff;
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

const LeftBox = styled.div`
  text-align: left;
`;
