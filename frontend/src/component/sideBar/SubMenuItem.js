import React, { useState } from 'react';
import styled from 'styled-components';
import { withRouter } from 'react-router-dom';

const SubMenuItem = props => {
  // 메뉴 클릭 여부
  const [isClicked, setIsClicked] = useState(false);

  return (
    <Container>
      <SubMenuItemTitle onClick={() => props.history.push(`/seller`)}>
        {props.name}
      </SubMenuItemTitle>
    </Container>
  );
};

export default withRouter(SubMenuItem);

const Container = styled.li`
  cursor: pointer;
`;

const SubMenuItemTitle = styled.div`
  padding: 5px 0 5px 35px;
  color: #fff;
  font-weight: 300;
  font-size: 14px;
`;
