import React, { useState } from 'react';
import TableBox from 'src/component/common/TableBox';
import TableItem from 'src/component/common/TableItem';
import SellerProperty from 'src/component/sellerInfoEdit//SellerProperty';
import ImageUploader from 'src/component/common/ImageUploader';
import InfoText from '../common/InfoText';
import SmallButton from '../common/SmallButton';
import style from 'src/utils/styles';
import styled from 'styled-components';

const Main = () => {
  // -- 기본 정보 --
  // 셀러 프로필 사진
  const [profileImage, setProfileImage] = useState(null);
  // 셀러 상태
  const [status, setStatus] = useState();
  // 셀러 속성
  const [property, setProperty] = useState();
  // 셀러 한글명
  const [koreanName, setKoreanName] = useState();
  // 셀러 영문명
  const [englishName, setEnglishName] = useState();
  // 셀러 계정
  const [account, setAccount] = useState();

  // 비밀번호 변경 Modal
  const [changePasswordModal, setChangePasswordModal] = useState(false);

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
        <TableItem title="셀러 헬피 여부" isRequired={false}>
          2222
        </TableItem>
        <TableItem title="셀러 한글명" isRequired={false}>
          222
        </TableItem>
        <TableItem title="셀러 영문명" isRequired={false}>
          222
        </TableItem>
        <TableItem title="셀러 계정" isRequired={false}>
          id{' '}
          <SmallButton
            name="비밀번호 변경하기"
            color={style.color.validationRed}
            textColor="#fff"
            onClickEvent={123}
          />
        </TableItem>
        <TableItem title="브랜디 어플 아이디" isRequired={true}>
          222
        </TableItem>
      </TableBox>

      <TableBox title="사업자 정보">
        <TableItem title="대표자명" isRequired={true}>
          1
        </TableItem>
        <TableItem title="사업자명" isRequired={true}>
          2
        </TableItem>
        <TableItem title="사업자번호" isRequired={true}>
          3
        </TableItem>
        <TableItem title="사업자등록증" isRequired={true}>
          <ImageUploader />
          <InfoText content="사업자등록증 확장자는 jpg, jpeg, png 만 가능하며, 허용 가능한 최대 파일사이즈 크기는 5MB 입니다." />
        </TableItem>
        <TableItem title="통신판매업번호" isRequired={true}>
          4
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
