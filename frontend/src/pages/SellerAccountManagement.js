import React from 'react';
import Layout from 'src/component/common/Layout';
import Main from 'src/component/sellerAccountManagement/Main';
import style from 'src/utils/styles';
import styled from 'styled-components';

const SellerAccountManagement = () => {
  return (
    <Layout>
      <Container>
        {/* header */}
        <HeaderWrapper>
          <Title>셀러 계정 관리</Title>
          <SubTitle>셀러 회원 목록 / 관리</SubTitle>
        </HeaderWrapper>
        {/* page bar */}
        <PageBar>
          <CategoryText>
            회원 관리 > 셀러 계정 관리 > 셀러 회원 리스트
          </CategoryText>
        </PageBar>
        {/* main */}
        <Main />
      </Container>
    </Layout>
  );
};

export default SellerAccountManagement;

const Container = styled.div``;

const Title = styled.div`
  font-size: 30px;
  font-weight: 600;
  color: ${style.color.infoColor};
  filter: ${style.filter.brightness};
`;

// 셀러정보 수정페이지, 셀러 정보 조회 / 수정

const HeaderWrapper = styled.div`
  display: flex;
  margin-bottom: 15px;
  padding: 25px 20px 0 20px;
`;

const SubTitle = styled.div`
  font-size: ${style.fontSize.generalFont};
  font-weight: ${style.fontWeight.thin};
  align-self: flex-end;
  margin-bottom: 3px;
`;

const PageBar = styled.div`
  background-color: ${style.color.titleGray};
  padding-left: 12px;
`;

const CategoryText = styled.div`
  font-size: ${style.fontSize.generalFont};
  padding: 8px;
`;
