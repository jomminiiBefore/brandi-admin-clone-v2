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
  four_length_case,
  only_number_case,
  check_url,
  business_number_case,
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
import InputContainer from 'src/component/common/InputContainer';
import PasswordModal from 'src/component/sellerInfoEdit/PasswordModal';
import BusinessHour from './BusinessHour';
import { makeStyles } from '@material-ui/core/styles';
import { JMURL, YJURL } from 'src/utils/config';
import { withRouter } from 'react-router-dom';
import style from 'src/utils/styles';
import styled, { keyframes, css } from 'styled-components';

const Main = (props) => {
  // 비밀번호 변경 Modal
  const [passwordModal, setPasswordModal] = useState(false);
  const showPasswordModal = () => {
    setPasswordModal(!passwordModal);
    console.log('showshow');
  };

  const [isLoading, setIsLoading] = React.useState(false);

  // 정보 입력 폼
  const [input, setInput] = useState({
    // 기본 정보
    profileImage: null,
    profileImageFile: null,
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
    businessRegistrationFile: null,
    telecommunicationsSalesNumber: '',
    telecommunicationsSalesReport: null,
    telecommunicationsSalesReportFile: null,
    // 상세 정보
    sellerPageBackgroundImage: null,
    sellerPageBackgroundImageFile: null,
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
    sellerStatusChangeHistories: [],
  });

  const {
    profileImage,
    profileImageFile,
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
    businessRegistrationFile,
    telecommunicationsSalesNumber,
    telecommunicationsSalesReport,
    telecommunicationsSalesReportFile,
    sellerPageBackgroundImage,
    sellerPageBackgroundImageFile,
    sellerIntroduction,
    sellerDetailIntroduction,
    siteUrl,
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
    sellerStatusChangeHistories,
  } = input;

  // 담당자 정보
  const [managerInfo, setManagerInfo] = useState([
    {
      name: '',
      contact_number: '',
      email: '',
      ranking: '',
    },
  ]);

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

  // isTyped와 isBlurred가 true 이면 정규식 검사 시작
  // 정보 입력 폼
  const [isValid, setIsValid] = useState({
    koreanName: false,
    englishName: false,
  });

  const setAppId = (e) => {
    console.log('app: ', e.target.name);
    console.log('appvalue: ', e.target.value);
    const { name, value } = e.target;
    setInput({ ...input, [name]: value });
  };

  const checkAppIdOverlap = (e) => {};

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
      if (business_number_case.test(value)) {
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
    } else if (name === 'siteUrl') {
      if (check_url.test(value)) {
        setIsValid({ ...isValid, [name]: true });
      } else {
        setIsValid({ ...isValid, [name]: false });
      }
    }
  };

  const setBlur = (e) => {
    setIsBlurred({ ...isBlurred, [e.target.name]: true });
  };

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
        name: '',
        contact_number: '',
        email: '',
        ranking: managerInfo.length + 1,
      },
    ]);
  };

  // 담당자 제거
  const removeManager = (e, index) => {
    const newlist = [].concat(managerInfo); // Clone array with concat or slice(0)
    newlist.splice(index, 1);

    setManagerInfo(newlist);
  };

  const setImg = (name, imageResult) => {
    console.log('imageResult::', name, imageResult);
    // imageResult가 null일 경우 이미지 삭제
    if (name === 'profileImage' && imageResult === null) {
      setInput({ ...input, [name]: null, profileImageFile: null });
    } else if (name === 'businessRegistrationFile' && imageResult === null) {
      setInput({
        ...input,
        [name]: null,
        businessRegistrationFile: null,
      });
    } else if (
      name === 'telecommunicationsSalesReport' &&
      imageResult === null
    ) {
      setInput({
        ...input,
        [name]: null,
        telecommunicationsSalesReportFile: null,
      });
    } else if (name === 'sellerPageBackgroundImage' && imageResult === null) {
      setInput({
        ...input,
        [name]: null,
        sellerPageBackgroundImageFile: null,
      });
    } else {
      // 이미지 삭제가 아닐 경우
      setInput({ ...input, [name]: imageResult });
    }
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

    setInput({ ...input, openingWeekendTime: null, closingWeekendTime: null });

    if (weekend) {
      setWeekend(false);
    } else {
      setWeekend(true);
    }
  };

  const onChangeBusinessHour = (id, value) => {
    console.log('id:: ', id);
    console.log('value:: ', value);
    setInput({ ...input, [id]: `${value}:00` });
  };

  const [sellerTypes, setSellerTypes] = useState([]);
  useEffect(() => {
    // 쿼리파라미터로 받은 셀러 id값
    const query = props.location.search.split('&');
    const sellerId = query[0].split('=')[1];
    console.log('useEffect() type: ', sellerId);

    fetch(`${JMURL}/seller/${sellerId}`, {
      headers: {
        Authorization:
          'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
      },
    })
      .then((res) => res.json())
      .then((res) => {
        console.log('res: ', res);
        if (res.weekday_start_time.split(':')[0].length === 1) {
          // openingWeekdayTime = '0' + openingWeekdayTime;
          res.weekday_start_time = '0'.concat(res.weekday_start_time);
        }
        if (res.weekday_end_time.split(':')[0].length === 1) {
          // openingWeekdayTime = '0' + openingWeekdayTime;
          res.weekday_end_time = '0'.concat(res.weekday_end_time);
        }
        if (
          res.weekend_start_time &&
          res.weekend_start_time.split(':')[0].length === 1
        ) {
          // openingWeekdayTime = '0' + openingWeekdayTime;
          res.weekend_start_time = '0'.concat(res.weekend_start_time);
        }
        if (
          res.weekend_end_time &&
          res.weekend_end_time.split(':')[0].length === 1
        ) {
          // openingWeekdayTime = '0' + openingWeekdayTime;
          res.weekend_end_time = '0'.concat(res.weekend_end_time);
        }
        setInput({
          ...input,
          profileImage: res.profile_image_url,
          status: res.seller_status_no,
          property: res.seller_type_no,
          koreanName: res.name_kr,
          englishName: res.name_en,
          brandiAppId: res.brandi_app_user_app_id,
          ceoName: res.ceo_name,
          businessName: res.company_name,
          businessNumber: res.business_number,
          businessRegistration: res.certificate_image_url,
          telecommunicationsSalesNumber: res.online_business_number,
          telecommunicationsSalesReport: res.online_business_image_url,
          sellerPageBackgroundImage: res.background_image_url,
          sellerIntroduction: res.short_description,
          sellerDetailIntroduction: res.long_description,
          siteUrl: res.site_url,
          instagramId: res.insta_id,
          serviceCenterPhoneNumber: res.center_number,
          kakaoId: res.kakao_id,
          yellowId: res.yellow_id,
          postNumber: res.zip_code,
          parcelAddress: res.address,
          parcelDetailAddress: res.detail_address,
          bankName: res.bank_name,
          accountHolder: res.bank_holder_name,
          accountNumber: res.account_number,
          openingWeekdayTime: res.weekday_start_time,
          closingWeekdayTime: res.weekday_end_time,
          openingWeekendTime: res.weekend_start_time,
          closingWeekendTime: res.weekend_end_time,
          sellerStatusChangeHistories: res.seller_status_change_histories,
        });
        setManagerInfo(res.manager_infos);
        setSellerTypes({ ...sellerTypes, sellerTypes: res.seller_types });
      })
      .catch((e) => {
        console.log('catch: ', e);
      });
  }, []);

  const onCheckBrandiAppId = (e) => {};

  useEffect(() => {
    openingWeekendTime && setWeekend(true);
  }, [openingWeekendTime]);

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

  const onChangeRadio = (e) => {
    console.log('radio: ', e.target.value);
    setInput({ ...input, [e.target.id]: e.target.value });
  };

  const onClickUpdate = (e) => {
    onSubmitInfo();
  };

  const onSubmitInfo = () => {
    setIsLoading(true);
    const query = props.location.search.split('&');
    const sellerId = query[0].split('=')[1];

    const objParam = {
      profile_image_url: profileImage,
      seller_profile_image: profileImageFile,
      seller_status_no: status,
      seller_type_no: parseInt(property),
      name_kr: koreanName,
      name_en: englishName,
      account_no: sellerAccount,
      brandi_app_user_app_id: brandiAppId,
      ceo_name: ceoName,
      company_name: businessName,
      business_number: businessNumber,
      online_business_number: telecommunicationsSalesNumber,
      certificate_image_url: businessRegistration,
      certificate_image: businessRegistrationFile,
      online_business_image_url: telecommunicationsSalesReport,
      online_business_image: telecommunicationsSalesReportFile,
      background_image_url: sellerPageBackgroundImage,
      background_image: sellerPageBackgroundImageFile,
      short_description: sellerIntroduction,
      long_description: sellerDetailIntroduction,
      site_url: siteUrl,
      manager_infos: managerInfo,
      insta_id: instagramId,
      center_number: serviceCenterPhoneNumber,
      kakao_id: kakaoId,
      yellow_id: yellowId,
      zip_code: postNumber,
      address: parcelAddress,
      detail_address: parcelDetailAddress,
      weekday_start_time: openingWeekdayTime,
      weekday_end_time: closingWeekdayTime,
      weekend_start_time: openingWeekendTime,
      weekend_end_time: closingWeekendTime,
      bank_name: bankName,
      bank_holder_name: accountHolder,
      account_number: accountNumber,
    };

    let formData = new FormData();
    for (let key in objParam) {
      if (key === 'manager_infos') {
        let managerInfos = JSON.stringify(objParam[key]);
        formData.append(key, managerInfos);
        console.log('manager_infos:: ', managerInfos);
      } else if (key === 'profile_image_url') {
        if (profileImage !== null) {
          formData.append(key, objParam[key]);
          console.log('data: ', key, objParam[key]);
        }
      } else if (key === 'certificate_image_url') {
        if (businessRegistration !== null) {
          formData.append(key, objParam[key]);
          console.log('data: ', key, objParam[key]);
        }
      } else if (key === 'online_business_image_url') {
        if (telecommunicationsSalesReport !== null) {
          formData.append(key, objParam[key]);
          console.log('data: ', key, objParam[key]);
        }
      } else if (key === 'background_image_url') {
        if (sellerPageBackgroundImage !== null) {
          // let backgroundUrl = JSON.stringify(objParam[key]);
          formData.append(key, objParam[key]);
          console.log('data: ', key, objParam[key]);
        }
      } else if (key === 'weekend_start_time') {
        if (openingWeekendTime !== null) {
          formData.append(key, objParam[key]);
          console.log('openingWeekendTime: ', key, objParam[key]);
        }
      } else if (key === 'weekend_end_time') {
        if (closingWeekendTime !== null) {
          formData.append(key, objParam[key]);
          console.log('closingWeekendTime: ', key, objParam[key]);
        }
      } else {
        formData.append(key, objParam[key]);
        console.log('data: ', key, objParam[key]);
      }
    }
    console.log('type:::', parseInt(sellerId));

    fetch(`${JMURL}/seller/${sellerId}`, {
      method: 'PUT',
      headers: {
        Authorization:
          // localStorage.getItem("token");
          'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
        // 'Content-Type': 'multipart/form-data',
        // 'Access-Control-Allow-Origin': '*',
      },
      body: formData,
    })
      .then((res) => {
        console.log('put res: ', res);
        return res.json();
        // if (res.ok) {
        //   return res.json();
        // } else {
        //   alert('네트워크 에러');
        // }
      })
      .then((res) => {
        console.log('onActionClick() res:', res);
        setIsLoading(false);
        if (res.message === 'SUCCESS') {
          alert('정상 처리 되었습니다.');

          props.history.push(`/seller`);
        } else {
          let errorMessage;
          for (let key in res) {
            console.log(res[key]);
            errorMessage = errorMessage + res[key];
          }
          alert(errorMessage);
        }
      })
      .catch((err) => console.log('catch():', err));
  };

  console.log('managerInfo: ', managerInfo);
  console.log('input: ', input);

  console.log('openingWeekdayTime:', openingWeekdayTime);
  console.log('closingWeekdayTime:', closingWeekdayTime);
  console.log('openingWeekendTime:', openingWeekendTime);
  console.log('closingWeekendTime:', closingWeekendTime);
  // 시:분:초 형태에서 시간이 한자리일 경우 맨앞에 0이 붙지 않기 때문에 0을 붙여주기 위한 코드
  if (openingWeekdayTime) {
  }
  if (closingWeekdayTime) {
  }
  if (openingWeekendTime) {
  }
  if (closingWeekendTime) {
  }
  return (
    <>
      <Container>
        {isLoading && (
          <>
            <Heart>
              <HeartDiv></HeartDiv>
            </Heart>
            <LoadingPage />
          </>
        )}

        {/* 기본 정보 */}
        <TableBox title="기본 정보">
          <TableItem title="셀러 프로필" isRequired={true}>
            <ImageUploader
              name="profileImage"
              fileName="profileImageFile"
              setImg={setImg}
              img={profileImage}
            />
            <InfoText content="셀러 프로필 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
          </TableItem>
          <TableItem title="셀러 상태" isRequired={false}>
            {seller_status}
          </TableItem>
          <TableItem title="셀러 속성" isRequired={true}>
            <SellerProperty
              sellerTypes={sellerTypes.sellerTypes}
              type={property}
              onChangeRadio={onChangeRadio}
            />
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
              textColor="#fff"
              onClickEvent={showPasswordModal}
            />
          </TableItem>
          {!brandiAppId && (
            <TableItem title="브랜디 어플 아이디" isRequired={true}>
              <InputContainer
                width={345}
                height={34}
                placeholder="브랜디 어플 아이디"
                name="brandiAppId"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.ceoName}
                blurred={isBlurred.ceoName}
                valid={isValid.ceoName}
                validationText="존재하지 않는 어플 아이디입니다."
                inputText={brandiAppId}
                isRequired={true}
              />
              <InfoText content="'브랜디' 어플을 설치하여 회원가입하고, 브랜디 어플 아이디를 입력해 주세요. 어플 아이디는 어플 > MY > 설정 > 프로필 편집에서 확인 가능합니다." />
            </TableItem>
          )}
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
            <ImageUploader
              name="businessRegistration"
              fileName="businessRegistrationFile"
              setImg={setImg}
              img={businessRegistration}
            />
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
              fileName="telecommunicationsSalesReportFile"
              setImg={setImg}
              img={telecommunicationsSalesReport}
            />
            <InfoText content="통신판매업신고필증 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
          </TableItem>
        </TableBox>

        {/* 상세 정보 */}
        <TableBox title="상세 정보">
          <TableItem title="셀러페이지 배경이미지" isRequired={false}>
            <ImageUploader
              name="sellerPageBackgroundImage"
              fileName="sellerPageBackgroundImageFile"
              setImg={setImg}
              img={sellerPageBackgroundImage}
            />
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
            <textarea
              name=""
              id=""
              cols="30"
              rows="10"
              value={sellerDetailIntroduction}
              onChange={(e) => setValue(e)}
              name="sellerDetailIntroduction"
            ></textarea>
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
              validationText="올바른 주소를 입력해주세요. (ex. http://www.brandi.co.kr)"
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
                    name={`name.${key}`}
                    setText={setManagerValue}
                    setBlur={setBlur}
                    // typed={isTyped.koreanName}
                    // blurred={isBlurred.koreanName}
                    valid={isValid.koreanName}
                    validationText="none"
                    inputText={e.name}
                    isRequired={true}
                  />
                  <InputWrapper>
                    <InputContainer
                      width={287}
                      height={34}
                      placeholder="담당자 핸드폰번호"
                      name={`contact_number.${key}`}
                      setText={setManagerValue}
                      setBlur={setBlur}
                      // typed={isTyped.koreanName}
                      // blurred={isBlurred.koreanName}
                      valid={isValid.koreanName}
                      validationText="한글, 영문, 숫자만 입력해주세요."
                      inputText={e.contact_number}
                      isRequired={true}
                    />
                  </InputWrapper>
                  <InputWrapper>
                    <InputContainer
                      width={287}
                      height={34}
                      placeholder="담당자 이메일"
                      name={`email.${key}`}
                      setText={setManagerValue}
                      setBlur={setBlur}
                      // typed={isTyped.koreanName}
                      // blurred={isBlurred.koreanName}
                      valid={isValid.koreanName}
                      validationText="한글, 영문, 숫자만 입력해주세요."
                      inputText={e.email}
                      isRequired={true}
                    />
                  </InputWrapper>
                </div>
              );
            })}

            <InputWrapper>
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
                name="postNumber"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.postNumber}
                blurred={isBlurred.postNumber}
                valid={isValid.postNumber}
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
                name="parcelAddress"
                setText={setValue}
                setBlur={setBlur}
                typed={isTyped.parcelAddress}
                blurred={isBlurred.parcelAddress}
                valid={isValid.parcelAddress}
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
              defaultOpeningTime={openingWeekdayTime}
              defaultClosingTime={closingWeekdayTime}
              isWeekendChecked={weekend}
            />
          </TableItem>
          {weekend && (
            <TableItem title="고객센터 운영시간(주말)" isRequired={false}>
              <BusinessHour
                onCheckWeekend={onCheckWeekend}
                openingName="openingWeekendTime"
                closingName="closingWeekendTime"
                onChangeBusinessHour={onChangeBusinessHour}
                defaultOpeningTime={openingWeekendTime}
                defaultClosingTime={closingWeekendTime}
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
          <TableItem title="셀러상태 변경기록" isRequired={true}>
            <SellerStateContainer>
              <SellerStateContentContainer>
                <SellerStateApplyDate>
                  셀러상태 변경 적용일시
                </SellerStateApplyDate>
                <SellerState>셀러 상태</SellerState>
                <SellerStateChangeUser>변경 실행자</SellerStateChangeUser>
              </SellerStateContentContainer>
              {/* changed_time: "Tue, 31 Mar 2020 23:59:59 GMT"
                  modifier: "seller"
                  seller_status_name: "입점대기" */}
              {sellerStatusChangeHistories.map((item) => {
                return (
                  <SellerStateContentContainer>
                    <SellerStateApplyDate>
                      {item.changed_time}
                    </SellerStateApplyDate>
                    <SellerState>{item.seller_status_name}</SellerState>
                    <SellerStateChangeUser>
                      {item.modifier}
                    </SellerStateChangeUser>
                  </SellerStateContentContainer>
                );
              })}
            </SellerStateContainer>
          </TableItem>
        </TableBox>
        <ButtonsContainer>
          <CustomButton
            name="수정"
            color="#5cb85b"
            textColor="#fff"
            onClickEvent={onSubmitInfo}
          />
          <CustomButton
            name="취소"
            color="#fff"
            textColor="#000"
            // onClickEvent={onClick}
          />
        </ButtonsContainer>
      </Container>
      {passwordModal && <PasswordModal showPasswordModal={showPasswordModal} />}
    </>
  );
};

export default withRouter(Main);

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

const SellerStateContainer = styled.div``;

const SellerStateContentContainer = styled.div`
  display: flex;
  width: 100%;
  height: 35px;
  border: 1px solid #bdbdbd;
  margin-top: -1px;
`;

const SellerStateApplyDate = styled.div`
  flex: 2;
  font-size: 13px;
  padding: 8px;
  align-self: center;
`;

const SellerState = styled.div`
  flex: 1;
  font-size: 13px;
  padding: 8px;
  height: 100%;
  align-self: center;
  border-left: 1px solid #bdbdbd;
  border-right: 1px solid #bdbdbd;
`;

const SellerStateChangeUser = styled.div`
  flex: 2;
  font-size: 13px;
  padding: 8px;
  align-self: center;
`;

const ButtonsContainer = styled.div`
  display: flex;
  justify-content: center;
`;

// 로딩
const LoadingPage = styled.div`
  position: absolute; /* Stay in place */
  z-index: 1; /* Sit on top */
  top: 80;
  width: 2000xp; /* Full width */
  height: 4000xp; /* Full height */
  background-color: #000;
  opacity: 0.5;
`;

const Heart = styled.div`
  display: inline-block;
  position: absolute;
  width: 80px;
  height: 80px;
  transform: rotate(45deg);
  transform-origin: 40px 40px;
`;

const HeartDiv = styled.div`
  & {
    top: 112px;
    left: 500px;
    position: absolute;
    width: 32px;
    height: 32px;
    background: #fe34c3;

    ${(props) => {
      return css`
        animation: ${HeartKeyFrames} 1.2s infinite
          cubic-bezier(0.215, 0.61, 0.355, 1);
      `;
    }}
  }
  &:after,
  &:before {
    content: ' ';
    position: absolute;
    display: block;
    width: 32px;
    height: 32px;
    background: #fe34c3;
  }
  &:before {
    left: -24px;
    border-radius: 50% 0 0 50%;
  }
  &:after {
    top: -24px;
    border-radius: 50% 50% 0 0;
  }
`;

const HeartKeyFrames = keyframes`
   0% {
    transform: scale(0.95);
  }
  5% {
    transform: scale(1.1);
  }
  39% {
    transform: scale(0.85);
  }
  45% {
    transform: scale(1);
  }
  60% {
    transform: scale(0.95);
  }
  100% {
    transform: scale(0.9);
  }
`;
