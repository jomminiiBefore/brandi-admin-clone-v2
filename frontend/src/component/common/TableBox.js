import React from 'react';
import style from 'src/utils/styles';
import styled from 'styled-components';

/*
 * 테이블 컨테이너
 * props: title (헤더 제목)
 */

const TableBox = props => {
  return (
    <Container>
      {/* 테이블 헤더  */}
      <TitleWrapper>
        <TitleText>{props.title}</TitleText>
      </TitleWrapper>
      {/* 테이블 메인 */}
      <ContentContainer>
        <ContentWrapper>{props.children}</ContentWrapper>
      </ContentContainer>
    </Container>
  );
};

export default TableBox;

const Container = styled.div`
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-bottom: 25px;
`;

const TitleWrapper = styled.div`
  background-color: ${style.color.titleGray};
  padding: 10px;
  font-weight: 400;
`;

const TitleText = styled.div`
  font-size: ${style.fontSize.subTitle};
`;

const ContentContainer = styled.div`
  padding: 10px;
`;

const ContentWrapper = styled.div``;
