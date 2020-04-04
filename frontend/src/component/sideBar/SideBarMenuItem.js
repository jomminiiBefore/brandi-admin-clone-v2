import React, { useState } from 'react';
import styled from 'styled-components';
import SubMenuItem from './SubMenuItem';

const SideBarMenuItem = props => {
  // 메뉴 클릭 여부
  const [isClicked, setIsClicked] = useState(false);
  // name: 메뉴 이름, list: 메뉴 상세 리스트
  const { name, list } = props;

  // console.log('list:', list);
  return (
    <Container>
      {isClicked ? (
        <>
          <SubMenuTitleWrapper onClick={() => setIsClicked(!isClicked)}>
            <MenuItemText>{name}</MenuItemText>
            <BottomArrow />
          </SubMenuTitleWrapper>

          {list.length > 0 && (
            <SubMenuItemWrapper>
              {list.map((item, i) => (
                <SubMenuItem key={i} name={item} />
              ))}
            </SubMenuItemWrapper>
          )}
        </>
      ) : (
        <SubMenuTitleWrapper onClick={() => setIsClicked(!isClicked)}>
          <MenuItemText>{name}</MenuItemText>
          <LeftArrow />
        </SubMenuTitleWrapper>
      )}
    </Container>
  );
};

export default SideBarMenuItem;

const Container = styled.li`
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border-bottom: 1px solid #414247;
  cursor: pointer;
  &:hover {
    background-color: #27272b;
  }
`;

const SubMenuTitleWrapper = styled.div`
  width: 215px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 15px 13px 15px 15px;
`;

const SubMenuItemWrapper = styled.ul`
  margin: 8px;
`;

const MenuItemText = styled.span`
  color: #fff;
  font-weight: 300;
  font-size: 14px;
`;

const LeftArrow = styled.div`
  width: 7px;
  height: 7px;
  border-top: 2px solid #666;
  border-left: 2px solid #666;
  transform: rotate(-45deg);
`;

const BottomArrow = styled.div`
  width: 7px;
  height: 7px;
  border-top: 2px solid #a6a8ae;
  border-left: 2px solid #a6a8ae;
  transform: rotate(-135deg);
`;
