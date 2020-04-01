import React from 'react';
import SideBar from 'src/component/sideBar/SideBar';
import Header from 'src/component/common/Header';
import styled from 'styled-components';

const Layout = props => {
  return (
    <>
      <Header />
      <MainContentWrapper>
        <SideBar />
        {props.children}
      </MainContentWrapper>
    </>
  );
};

export default Layout;

const MainContentWrapper = styled.div`
  display: flex;
`;
