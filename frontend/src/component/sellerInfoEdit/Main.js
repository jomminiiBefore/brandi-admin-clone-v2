import React, { useState, useEffect } from 'react';
import TableBox from 'src/component/common/TableBox';
import TableItem from 'src/component/common/TableItem';
import SellerProperty from 'src/component/sellerInfoEdit//SellerProperty';
import ImageUploader from 'src/component/common/ImageUploader';
import InfoText from '../common/InfoText';
import SmallButton from '../common/SmallButton';
import Input from 'src/component/common/Input';
import Validation from 'src/component/common/Validation';
import { korean_english_number, lower_case } from 'src/utils/regexp';
import style from 'src/utils/styles';
import styled from 'styled-components';
import InputContainer from '../common/InputContainer';

const Main = () => {
  // 비밀번호 변경 Modal
  const [changePasswordModal, setChangePasswordModal] = useState(false);

  // 정보 입력 폼
  const [input, setInput] = useState({
    profileImage: null,
    status: '',
    property: '',
    koreanName: '',
    englishName: '',
    sellerAccount: '',
    brandiAppId: '',
    ceoName: '',
    businessName: '',
    businessNumber: '',
    businessRegistration: null,
    telecommunicationsSalesNumber: '',
    telecommunicationsSalesReport: '',
  });

  const {
    profileImage,
    status,
    property,
    koreanName,
    englishName,
    sellerAccount,
    brandiAppId,
    ceoName,
    businessName,
    businessNumber,
    businessRegistration,
  } = input;

  // input 안에 값이 한번이라도 들어오면 true로 변경
  const [isTyped, setIsTyped] = useState({
    koreanName: false,
    englishName: false,
    account: false,
    brandiAppId: false,
    ceoName: false,
    businessName: false,
    businessNumber: false,
    telecommunicationsSalesNumber: false,
  });

  const [isBlurred, setIsBlurred] = useState({
    koreanName: false,
    englishName: false,
    ceoName: false,
    businessName: false,
    businessNumber: false,
    telecommunicationsSalesNumber: false,
  });

  // input 값이 바뀌었을 때 호출되는 함수
  const setValue = (e) => {
    const { name, value } = e.target;
    setInput({ ...input, [name]: value });
    setIsTyped({ ...isTyped, [name]: true });

    if (name === 'koreanName') {
      if (korean_english_number.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === 'englishName') {
      if (lower_case.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    }
  };

  const setBlur = (e) => {
    setIsBlurred({ ...isBlurred, [e.target.name]: true });
  };

  // isTyped와 isBlurred가 true 이면 정규식 검사 시작
  // 정보 입력 폼
  const [isValid, setIsValid] = useState({
    koreanName: false,
    englishName: false,
  });

  // useEffect(() => {
  //   console.log(lower_case.test(koreanName));
  //   if (korean_english_number.test(koreanName)) {
  //     setIsValid({ ...isValid, koreanName: true });
  //   } else {
  //     setIsValid({ ...isValid, koreanName: false });
  //   }

  //   if (lower_case.test(englishName)) {
  //     setIsValid({ ...isValid, englishName: true });
  //   } else {
  //     setIsValid({ ...isValid, englishName: false });
  //   }
  // }, [koreanName, englishName]);
  console.log('isValid.koreanName: ', isValid.koreanName);
  return (
    <Container>
      <TableBox title="기본 정보">
        <TableItem title="셀러 프로필" isRequired={true}>
          <ImageUploader />
          <InfoText content="셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
        </TableItem>
        <TableItem title="셀러 상태" isRequired={false}>
          입점
        </TableItem>
        <TableItem title="셀러 속성" isRequired={true}>
          <SellerProperty />
        </TableItem>
        <TableItem title="셀러 한글명" isRequired={false}>
          <InputContainer
            width={287}
            height={34}
            placeholder="셀러 한글명"
            name="koreanName"
            setText={setValue}
            setBlur={setBlur}
            typed={isTyped.koreanName}
            blurred={isBlurred.koreanName}
            valid={isValid.koreanName}
            validationText="한글, 영문, 숫자만 입력해주세요."
            inputText={koreanName}
          />
        </TableItem>
        <TableItem title="셀러 영문명" isRequired={false}>
          <InputContainer
            width={287}
            height={34}
            placeholder="셀러 영문명"
            name="englishName"
            setText={setValue}
            setBlur={setBlur}
            typed={isTyped.englishName}
            blurred={isBlurred.englishName}
            valid={isValid.englishName}
            validationText="셀러 영문명은 소문자만 가능합니다."
            inputText={englishName}
          />
        </TableItem>
        <TableItem title="셀러 계정" isRequired={false}>
          id
          <SmallButton
            name="비밀번호 변경하기"
            color={style.color.validationRed}
            textColor="red"
            // onClickEvent={}
          />
        </TableItem>
        <TableItem title="브랜디 어플 아이디" isRequired={true}>
          <Input
            name="brandiAppId"
            width={287}
            height={34}
            placeholder="브랜디 어플 아이디"
            name="brandiAppId"
            setText={setValue}
          />
        </TableItem>
      </TableBox>

      <TableBox title="사업자 정보">
        <TableItem title="대표자명" isRequired={true}>
          <InputContainer
            width={287}
            height={34}
            placeholder="대표자명"
            name="ceoName"
            setText={setValue}
            setBlur={setBlur}
            typed={isTyped.ceoName}
            blurred={isBlurred.ceoName}
            valid={isValid.ceoName}
            validationText="none"
            inputText={ceoName}
          />
        </TableItem>
        <TableItem title="사업자명" isRequired={true}>
          <Input
            width={287}
            height={34}
            placeholder="사업자명"
            name="englishName"
            setText={setValue}
            setBlur={setBlur}
            typed={isTyped.englishName}
            blurred={isBlurred.englishName}
            valid={isValid.englishName}
          />
          <Validation
            validationText="셀러 영문명은 소문자만 가능합니다."
            inputText={englishName}
            typed={isTyped.englishName}
            blurred={isBlurred.englishName}
            valid={isValid.englishName}
          />
        </TableItem>
        <TableItem title="사업자번호" isRequired={true}>
          <Input
            width={287}
            height={34}
            placeholder="사업자번호"
            name="englishName"
            setText={setValue}
            setBlur={setBlur}
            typed={isTyped.englishName}
            blurred={isBlurred.englishName}
            valid={isValid.englishName}
          />
          <Validation
            validationText="셀러 영문명은 소문자만 가능합니다."
            inputText={englishName}
            typed={isTyped.englishName}
            blurred={isBlurred.englishName}
            valid={isValid.englishName}
          />
        </TableItem>
        <TableItem title="사업자등록증" isRequired={true}>
          <ImageUploader />
          <InfoText content="사업자등록증 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
        </TableItem>
        <TableItem title="통신판매업번호" isRequired={true}>
          <InputContainer
            width={287}
            height={34}
            placeholder="셀러 영문명"
            name="englishName"
            setText={setValue}
            setBlur={setBlur}
            typed={isTyped.englishName}
            blurred={isBlurred.englishName}
            valid={isValid.englishName}
            validationText="셀러 영문명은 소문자만 가능합니다."
            inputText={englishName}
          />
        </TableItem>
        <TableItem title="통신판매업신고필증" isRequired={true}>
          <ImageUploader />
          <InfoText content="통신판매업신고필증 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
        </TableItem>
      </TableBox>
    </Container>
  );
};

export default Main;

const Container = styled.div`
  padding: 10px 20px 20px 20px;
`;
