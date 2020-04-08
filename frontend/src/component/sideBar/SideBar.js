import React from 'react';
import styled from 'styled-components';
import SideBarMenuItem from 'src/component/sideBar/SideBarMenuItem';

const SideBar = () => {
  return (
    <Container>
      <SideBarMenu>
        <SideBarToggleWrapper></SideBarToggleWrapper>
        {menu.map((item, i) => (
          <SideBarMenuItem key={i} name={item.name} list={item.list} />
        ))}
      </SideBarMenu>
    </Container>
  );
};

export default SideBar;

const Container = styled.div`
  /* height: 100vh; */
  background-color: #35353a;
`;

const SideBarMenu = styled.ul``;

const SideBarToggleWrapper = styled.li`
  height: 50px;
`;

const menu = [
  {
    name: '홈',
    list: [],
  },
  {
    name: '공지사항',
    list: [],
  },
  {
    name: '통계',
    list: [],
  },
  {
    name: '주문관리',
    list: [],
  },
  {
    name: '취소/환불 관리',
    list: [],
  },
  {
    name: '상품관리',
    list: ['상품 관리', '상품 등록'],
  },
  {
    name: '외부채널연동상품 관리',
    list: [],
  },
  {
    name: '고객응대관리',
    list: [],
  },
  {
    name: '정산관리',
    list: [],
  },
  {
    name: '진열관리',
    list: [],
  },
  {
    name: '기획전/쿠폰관리',
    list: ['기획전 관리'],
  },
  {
    name: '푸시',
    list: [],
  },
  {
    name: '회원 관리',
    list: ['셀러 계정 관리'],
  },
  {
    name: '기타',
    list: [],
  },
  {
    name: '이전 버전 관리',
    list: [],
  },
];
