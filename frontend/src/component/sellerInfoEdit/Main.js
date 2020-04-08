import React, { useState, useEffect } from 'react';
import {
  check_email,
  korean_english_number,
  lower_case,
  number_case,
  ten_number_case,
  korean_number_hypen_case,
  lower_number_underline_dot_case,
  number_hypen_case,
  two_length_case,
  only_number_case,
} from 'src/utils/regexp';
import TableBox from 'src/component/common/TableBox';
import TableItem from 'src/component/common/TableItem';
import SellerProperty from 'src/component/sellerInfoEdit//SellerProperty';
import ImageUploader from 'src/component/common/ImageUploader';
import InfoText from 'src/component/common/InfoText';
import SmallButton from 'src/component/common/SmallButton';
import Input from 'src/component/common/Input';
import CustomButton from 'src/component/common/CustomButton';
import ManagerRemoveButton from 'src/component/sellerInfoEdit/ManagerRemoveButton';
import InputContainer from '../common/InputContainer';
import ManagerInfoItem from './ManagerInfoItem';
import BusinessHour from './BusinessHour';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import { JMURL } from 'src/utils/config';
import style from 'src/utils/styles';
import styled from 'styled-components';
import PasswordModal from 'src/component/sellerInfoEdit/PasswordModal';

// TimePicker
const useStyles = makeStyles((theme) => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    width: 110,
  },
}));

const Main = () => {
  // 비밀번호 변경 Modal
  const [passwordModal, setPasswordModal] = useState(false);
  const showPasswordModal = () => {
    setPasswordModal(!passwordModal);
    console.log('showshow');
  };

  // 정보 입력 폼
  const [input, setInput] = useState({
    // 기본 정보
    profileImage: null,
    status: '',
    property: '',
    koreanName: '',
    englishName: '',
    sellerAccount: '',
    brandiAppId: '',
    // 사업자 정보
    ceoName: '',
    businessName: '',
    businessNumber: '',
    businessRegistration: null,
    telecommunicationsSalesNumber: '',
    telecommunicationsSalesReport: '',
    // 상세 정보
    sellerPageBackgroundImage: null,
    sellerIntroduction: '',
    sellerDetailIntroduction: '',
    siteUrl: '',
    // managerInfo: [{ managerName: '', managerPhone: '', managerEmail: '' }],
    instagramId: '',
    serviceCenterPhoneNumber: '',
    kakaoId: '',
    yellowId: '',
    postNumber: '',
    parcelAddress: '',
    parcelDetailAddress: '',
    openingWeekdayTime: '',
    closingWeekdayTime: '',
    openingWeekendTime: '',
    closingWeekendTime: '',
    weekendBusinessHour: '',
    bankName: '',
    accountHolder: '',
    accountNumber: '',
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
    telecommunicationsSalesNumber,
    sellerPageBackgroundImage,
    sellerIntroduction,
    sellerDetailIntroduction,
    siteUrl,
    // managerInfo,
    instagramId,
    serviceCenterPhoneNumber,
    kakaoId,
    yellowId,
    postNumber,
    parcelAddress,
    parcelDetailAddress,
    openingWeekdayTime,
    closingWeekdayTime,
    openingWeekendTime,
    closingWeekendTime,
    weekendBusinessHour,
    bankName,
    accountHolder,
    accountNumber,
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
    sellerIntroduction: false,
    siteUrl: false,
    // managerInfo: [],
    instagramId: false,
    serviceCenterPhoneNumber: false,
    kakaoId: false,
    yellowId: false,
    postNumber: false,
    parcelAddress: false,
    parcelDetailAddress: false,
    weekendBusinessHour: false,
    bankName: false,
    accountHolder: false,
    accountNumber: false,
  });

  // input창의 포커스가 아웃됐을 경우 true
  const [isBlurred, setIsBlurred] = useState({
    koreanName: false,
    englishName: false,
    ceoName: false,
    businessName: false,
    businessNumber: false,
    telecommunicationsSalesNumber: false,
    sellerIntroduction: false,
    siteUrl: false,
    // managerInfo: [],
    instagramId: false,
    serviceCenterPhoneNumber: false,
    kakaoId: false,
    yellowId: false,
    postNumber: false,
    parcelAddress: false,
    parcelDetailAddress: false,
    weekendBusinessHour: false,
    bankName: false,
    accountHolder: false,
    accountNumber: false,
  });

  // input 값이 바뀌었을 때 호출되는 함수
  const setValue = (e) => {
    const { name, value } = e.target;
    setInput({ ...input, [name]: value });
    setIsTyped({ ...isTyped, [name]: true });

    if (name === 'koreanName') {
      // 한글, 영문, 숫자 정규식
      if (korean_english_number.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
      // 소문자 정규식
    } else if (name === 'englishName') {
      if (lower_case.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === 'businessNumber') {
      if (ten_number_case.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === 'telecommunicationsSalesNumber') {
      if (korean_number_hypen_case.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === 'serviceCenterPhoneNumber') {
      if (number_hypen_case.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (
      name === 'instagramId' ||
      name === 'kakaoId' ||
      name === 'yellowId'
    ) {
      if (lower_number_underline_dot_case.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === 'parcelDetailAddress') {
      if (two_length_case.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    } else if (name === 'accountNumber') {
      if (only_number_case.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    }
  };

  const setBlur = (e) => {
    setIsBlurred({ ...isBlurred, [e.target.name]: true });
  };

  // 담당자 state
  const [managerInfo, setManagerInfo] = useState([
    {
      managerName: '',
      managerPhone: '',
      managerEmail: '',
    },
  ]);

  const setManagerValue = (e) => {
    console.log(e.target.name);
    console.log(e.target.value);
    let name = e.target.name.split('.')[0];
    let index = e.target.name.split('.')[1];

    const newlist = [].concat(managerInfo); // Clone array with concat or slice(0)
    newlist[index][name] = e.target.value;
    // console.log(newlist[index]);
    setManagerInfo(newlist);
  };

  // 담당자 추가
  const addManager = (e) => {
    setManagerInfo((state) => [
      ...state,
      {
        managerName: '',
        managerPhone: '',
        managerEmail: '',
      },
    ]);
  };

  // 담당자 제거
  const removeManager = (e, index) => {
    const newlist = [].concat(managerInfo); // Clone array with concat or slice(0)
    newlist.splice(index, 1);

    setManagerInfo(newlist);
  };

  // isTyped와 isBlurred가 true 이면 정규식 검사 시작
  // 정보 입력 폼
  const [isValid, setIsValid] = useState({
    koreanName: false,
    englishName: false,
  });

  const setImg = (name, imageResult) => {
    console.log('imageResult::', name, imageResult);
    // setInput({ ...input, [name]: value });
  };

  // 주소 찾기
  const openPostcode = () => {
    new daum.Postcode({
      oncomplete: function (data) {
        setInput({
          ...input,
          postNumber: data.zonecode,
          parcelAddress: `${data.address} (${data.bname}, ${data.buildingName})`,
        });
      },
    }).open();
  };

  // 운영 시간
  const [weekend, setWeekend] = useState(false);

  // 주말 시간표 체크박스 클릭
  const onCheckWeekend = () => {
    // 체크박스 누를때 주말 시간표 초기화
    setInput({
      ...input,
      openingWeekendTime: null,
      closingWeekendTime: null,
    });

    if (weekend) {
      setWeekend(false);
    } else {
      setWeekend(true);
    }
  };

  const onChangeBusinessHour = (e) => {
    const { id, value } = e.target;
    setInput({ ...input, [id]: value });
  };

  const [sellerTypes, setSellerTypes] = useState([]);
  useEffect(() => {
    fetch(`${JMURL}/seller/5`, {
      headers: {
        Authorization:
          'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
      },
    })
      .then((res) => res.json())
      .then((res) => {
        setInput({
          ...input,
          profileImage: res.profile_image_url,
          status: res.seller_status_no,
          property: res.seller_type_no,
        });
        setSellerTypes({ ...sellerTypes, sellerTypes: res.seller_types });
      });
  }, []);

  // 셀러 상태
  let seller_status;
  switch (status) {
    case 1:
      seller_status = '입점대기';
      break;
    case 2:
      seller_status = '입점';
      break;
    case 3:
      seller_status = '퇴점대기';
      break;
    case 4:
      seller_status = '퇴점';
      break;
    case 5:
      seller_status = '휴점';
      break;
    default:
    // code block
  }
  console.log('managerInfo: ', managerInfo);
  return (
    <>
      <Container>
        {/* 기본 정보 */}
        <TableBox title="기본 정보">
          <TableItem title="셀러 프로필" isRequired={true}>
            <ImageUploader
              name="profileImage"
              setImg={setImg}
              img={profileImage}
            />
            <InfoText content="셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
          </TableItem>
          <TableItem title="셀러 상태" isRequired={false}>
            {seller_status}
          </TableItem>
          <TableItem title="셀러 속성" isRequired={true}>
            <SellerProperty sellerTypes={sellerTypes.sellerTypes} />
          </TableItem>
          <TableItem title="셀러 한글명" isRequired={true}>
            <InputContainer
              width={345}
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
              isRequired={true}
            />
          </TableItem>
          <TableItem title="셀러 영문명" isRequired={true}>
            <InputContainer
              width={345}
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
              isRequired={true}
            />
          </TableItem>
          <TableItem title="셀러 계정" isRequired={false}>
            id
            <SmallButton
              name="비밀번호 변경하기"
              color={style.color.validationRed}
              textColor="red"
              onClickEvent={showPasswordModal}
            />
          </TableItem>
          <TableItem title="브랜디 어플 아이디" isRequired={true}>
            <Input
              name="brandiAppId"
              width={345}
              height={34}
              placeholder="브랜디 어플 아이디"
              name="brandiAppId"
              setText={setValue}
            />
          </TableItem>
        </TableBox>

        {/* 사업자 정보 */}
        <TableBox title="사업자 정보">
          <TableItem title="대표자명" isRequired={true}>
            <InputContainer
              width={345}
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
              isRequired={true}
            />
          </TableItem>
          <TableItem title="사업자명" isRequired={true}>
            <InputContainer
              width={345}
              height={34}
              placeholder="사업자명"
              name="businessName"
              setText={setValue}
              setBlur={setBlur}
              typed={isTyped.businessName}
              blurred={isBlurred.businessName}
              valid={isValid.businessName}
              validationText="none"
              inputText={businessName}
              isRequired={true}
            />
          </TableItem>
          <TableItem title="사업자번호" isRequired={true}>
            <InputContainer
              width={345}
              height={34}
              placeholder="사업자번호"
              name="businessNumber"
              setText={setValue}
              setBlur={setBlur}
              typed={isTyped.businessNumber}
              blurred={isBlurred.businessNumber}
              valid={isValid.businessNumber}
              validationText="올바른 정보를 입력해주세요."
              inputText={businessNumber}
              isRequired={true}
            />
          </TableItem>
          <TableItem title="사업자등록증" isRequired={true}>
            <ImageUploader name="businessRegistration" setImg={setImg} />
            <InfoText content="사업자등록증 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
          </TableItem>
          <TableItem title="통신판매업번호" isRequired={true}>
            <InputContainer
              width={345}
              height={34}
              placeholder="통신판매업번호"
              name="telecommunicationsSalesNumber"
              setText={setValue}
              setBlur={setBlur}
              typed={isTyped.telecommunicationsSalesNumber}
              blurred={isBlurred.telecommunicationsSalesNumber}
              valid={isValid.telecommunicationsSalesNumber}
              validationText="통신판매번호는 한글, 숫자, 하이픈만 가능합니다."
              inputText={telecommunicationsSalesNumber}
              isRequired={true}
            />
          </TableItem>
          <TableItem title="통신판매업신고필증" isRequired={true}>
            <ImageUploader
              name="telecommunicationsSalesReport"
              setImg={setImg}
            />
            <InfoText content="통신판매업신고필증 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
          </TableItem>
        </TableBox>

        {/* 상세 정보 */}
        <TableBox title="상세 정보">
          <TableItem title="셀러페이지 배경이미지" isRequired={false}>
            <ImageUploader name="profileImage" setImg={setImg} />
            <InfoText content="셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
            <InfoText content="배경이미지는 1200 * 850 사이즈 이상으로 등록해주세요." />
            <InfoText content="확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
          </TableItem>
          <TableItem title="셀러 한줄 소개" isRequired={true}>
            <InputContainer
              width={345}
              height={34}
              placeholder="셀러 한줄 소개"
              name="sellerIntroduction"
              setText={setValue}
              setBlur={setBlur}
              typed={isTyped.sellerIntroduction}
              blurred={isBlurred.sellerIntroduction}
              valid={isValid.sellerIntroduction}
              validationText="none"
              inputText={sellerIntroduction}
              isRequired={true}
            />
          </TableItem>
          <TableItem title="셀러 상세 소개" isRequired={true}>
            <textarea name="" id="" cols="30" rows="10"></textarea>
            <InfoText content="셀러 상세 소개 글은 최소10자 이상 입니다." />
          </TableItem>
          <TableItem title="사이트 URL" isRequired={true}>
            <InputContainer
              width={345}
              height={34}
              placeholder="사이트 URL"
              name="siteUrl"
              setText={setValue}
              setBlur={setBlur}
              typed={isTyped.siteUrl}
              blurred={isBlurred.siteUrl}
              valid={isValid.siteUrl}
              validationText="none"
              inputText={siteUrl}
              isRequired={true}
            />
          </TableItem>
          <TableItem title="담당자 정보" isRequired={true}>
            {managerInfo.map((e, key) => {
              return (
                <div key={key}>
                  {key === 1 && <ManagerLine />}
                  {key === 2 && <ManagerLine />}
                  <InputContainer
                    width={287}
                    height={34}
                    placeholder="담당자명"
                    name={`managerName.${key}`}
                    setText={setManagerValue}
                    setBlur={setBlur}
                    // typed={isTyped.koreanName}
                    // blurred={isBlurred.koreanName}
                    valid={isValid.koreanName}
                    validationText="none"
                    inputText={koreanName}
                    isRequired={true}
                  />
                  <InputWrapper>
                    <InputContainer
                      width={287}
                      height={34}
                      placeholder="담당자 핸드폰번호"
                      name={`managerPhone.${key}`}
                      setText={setManagerValue}
                      setBlur={setBlur}
                      // typed={isTyped.koreanName}
                      // blurred={isBlurred.koreanName}
                      valid={isValid.koreanName}
                      validationText="한글, 영문, 숫자만 입력해주세요."
                      inputText={koreanName}
                      isRequired={true}
                    />
                  </InputWrapper>
                  <InputWrapper>
                    <InputContainer
                      width={287}
                      height={34}
                      placeholder="담당자 이메일"
                      name={`managerEmail.${key}`}
                      setText={setManagerValue}
                      setBlur={setBlur}
                      // typed={isTyped.koreanName}
                      // blurred={isBlurred.koreanName}
                      valid={isValid.koreanName}
                      validationText="한글, 영문, 숫자만 입력해주세요."
                      inputText={koreanName}
                      isRequired={true}
                    />
                  </InputWrapper>
                </div>
              );
            })}

            <InputWrapper>
              {console.log('managerInfo??: ', managerInfo.length)}
              {managerInfo.length === 1 || managerInfo.length === 2 ? (
                <CustomButton
                  name="+"
                  color="#5cb85b"
                  textColor="#fff"
                  onClickEvent={addManager}
                />
              ) : (
                ''
              )}
              {managerInfo.length === 2 || managerInfo.length === 3 ? (
                <ManagerRemoveButton
                  name="-"
                  color="#d9534f"
                  textColor="#fff"
                  onClickEvent={removeManager}
                  index={managerInfo.length - 1}
                />
              ) : (
                ''
              )}
            </InputWrapper>
          </TableItem>
          <TableItem title="인스타그램 아이디" isRequired={true}>
            <InputContainer
              width={345}
              height={34}
              placeholder="인스타그램 아이디"
              name="instagramId"
              setText={setValue}
              setBlur={setBlur}
              typed={isTyped.instagramId}
              blurred={isBlurred.instagramId}
              valid={isValid.instagramId}
              validationText="인스타그램 아이디는 영어 소문자, 숫자, 밑줄, 마침표만 사용가능합니다."
              inputText={instagramId}
              isRequired={false}
            />
            <InfoText content="인스타그램 아이디는 선택사항입니다." />
          </TableItem>
          <TableItem title="고객센터" isRequired={true}>
            <InputContainer
              width={345}
              height={34}
              placeholder="고객센터 전화번호"
              name="serviceCenterPhoneNumber"
              setText={setValue}
              setBlur={setBlur}
              typed={isTyped.serviceCenterPhoneNumber}
              blurred={isBlurred.serviceCenterPhoneNumber}
              valid={isValid.serviceCenterPhoneNumber}
              validationText="고객센터 전화번호는 숫자와 하이픈만 입력가능합니다."
              inputText={serviceCenterPhoneNumber}
              isRequired={true}
            />
            <InputWrapper>
              <InputContainer
                width={345}
                height={34}
                placeholder="카카오톡 아이디"
                name="kakaoId"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.kakaoId}
                blurred={isBlurred.kakaoId}
                valid={isValid.kakaoId}
                validationText="올바른 아이디를 입력해주세요."
                inputText={kakaoId}
                isRequired={false}
              />
            </InputWrapper>

            <InputWrapper>
              <InputContainer
                width={345}
                height={34}
                placeholder="옐로우 아이디"
                name="yellowId"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.yellowId}
                blurred={isBlurred.yellowId}
                valid={isValid.yellowId}
                validationText="올바른 아이디를 입력해주세요."
                inputText={yellowId}
                isRequired={false}
              />
            </InputWrapper>

            <InfoText content="카카오톡 아이디와 옐로우 아이디는 선택 사항입니다." />
          </TableItem>
          <TableItem title="택배 주소" isRequired={true}>
            <InputButtonWrapper>
              <InputContainer
                width={195}
                height={34}
                placeholder="우편번호"
                name="instagramId"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.instagramId}
                blurred={isBlurred.instagramId}
                valid={isValid.instagramId}
                validationText="none"
                inputText={postNumber}
                isRequired={false}
                type="text"
                disabled={true}
              />
              <CustomButtonWrapper>
                <CustomButton
                  name="우편번호 찾기"
                  color="#5cb85b"
                  textColor="#fff"
                  onClickEvent={openPostcode}
                />
              </CustomButtonWrapper>
            </InputButtonWrapper>

            <InputWrapper>
              <InputContainer
                width={345}
                height={34}
                placeholder="주소 (택배 수령지)"
                name="instagramId"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.instagramId}
                blurred={isBlurred.instagramId}
                valid={isValid.instagramId}
                validationText="none"
                inputText={parcelAddress}
                isRequired={false}
                disabled={true}
              />
            </InputWrapper>
            <InputWrapper>
              <InputContainer
                width={345}
                height={34}
                placeholder="상세주소 (택배 수령지)"
                name="parcelDetailAddress"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.parcelDetailAddress}
                blurred={isBlurred.parcelDetailAddress}
                valid={isValid.parcelDetailAddress}
                validationText="올바른 주소를 입력해주세요."
                inputText={parcelDetailAddress}
                isRequired={true}
              />
            </InputWrapper>
          </TableItem>
          <TableItem title="고객센터 운영시간(주중)" isRequired={true}>
            <BusinessHour
              onCheckWeekend={onCheckWeekend}
              onChangeBusinessHour={onChangeBusinessHour}
              openingName="openingWeekdayTime"
              closingName="closingWeekdayTime"
            />
          </TableItem>
          {weekend && (
            <TableItem title="고객센터 운영시간(주말)" isRequired={false}>
              <BusinessHour
                onCheckWeekend={onCheckWeekend}
                onChangeBusinessHour={onChangeBusinessHour}
                openingName="openingWeekendTime"
                closingName="closingWeekendTime"
              />
            </TableItem>
          )}
          <TableItem title="정산정보 입력" isRequired={true}>
            <InputContainer
              width={167}
              height={34}
              placeholder="정산은행"
              name="bankName"
              setText={setValue}
              setBlur={setBlur}
              typed={isTyped.bankName}
              blurred={isBlurred.bankName}
              valid={isValid.bankName}
              validationText="none"
              inputText={bankName}
              isRequired={true}
            />
            <InputWrapper>
              <InputContainer
                width={101}
                height={34}
                placeholder="계좌주"
                name="accountHolder"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.accountHolder}
                blurred={isBlurred.accountHolder}
                valid={isValid.accountHolder}
                validationText="none"
                inputText={accountHolder}
                isRequired={true}
              />
            </InputWrapper>

            <InputWrapper>
              <InputContainer
                width={167}
                height={34}
                placeholder="계좌번호"
                name="accountNumber"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.accountNumber}
                blurred={isBlurred.accountNumber}
                valid={isValid.accountNumber}
                validationText="숫자만 입력해주세요."
                inputText={accountNumber}
                isRequired={true}
              />
            </InputWrapper>
          </TableItem>
        </TableBox>
      </Container>
      {passwordModal && <PasswordModal showPasswordModal={showPasswordModal} />}
    </>
  );
};

export default Main;

const Container = styled.div`
  padding: 10px 20px 20px 20px;
`;

const InputWrapper = styled.div`
  margin-top: 5px;
`;

const InputButtonWrapper = styled.div`
  display: flex;
`;

const CustomButtonWrapper = styled.div`
  margin-left: 45px;
`;

const WeekendCheckBox = styled.input`
  align-self: flex-end;
`;

const ManagerLine = styled.div`
  width: 100%;
  height: 1px;
  background-color: #bdbdbd;
  margin: 25px 0px;
`;
