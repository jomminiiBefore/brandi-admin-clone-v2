import React from "react";
import Header from "src/component/common/Header";
import SideBar from "src/component/sideBar/SideBar";
import Footer from "src/component/common/Footer";
import styled from "styled-components";

const Layout = props => {
  return (
    <>
      <Header />
      <MainContentWrapper>
        <SideBar />
        <PageContainer>{props.children}</PageContainer>
      </MainContentWrapper>
      <Footer />
    </>
  );
};

export default Layout;

const MainContentWrapper = styled.div`
  display: flex;
  width: 100vw;
`;

const PageContainer = styled.div`
  width: calc(100% - 215px);
`;
