import React from 'react';
import styled from 'styled-components';
import Layout from 'src/component/common/Layout';
import style from 'src/utils/styles';

const SellerAccountManagement = () => {
  return (
    <Layout>
      <Container>
        <Title>SellerAccountManagement</Title>
      </Container>
    </Layout>
  );
};

export default SellerAccountManagement;

const Container = styled.div`
  display: flex;
  justify-content: center;
`;

const Title = styled.div`
  font-size: 30px;
  font-weight: 600;
  color: ${style.color.infoColor};
  filter: ${style.filter.brightness};
`;
