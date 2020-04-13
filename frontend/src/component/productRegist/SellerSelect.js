import React, { useState, useEffect } from "react";
import styled, { keyframes, css } from "styled-components";
import { SHURL } from "src/utils/config";
import styles from "src/utils/styles";
import { InfoCircle } from "@styled-icons/fa-solid";

const SellerSelect = ({ showSellerSelect, getCategoryOne }) => {
  const [input, setInput] = useState("");

  const [seller, setSeller] = useState([]);

  const [currentSeller, setCurrentSeller] = useState("");

  // 셀러검색 GET 함수
  const getSearchSeller = e => {
    setInput(e.target.value);
    fetch(`${SHURL}/seller?name_kr=${input}`, {
      method: "GET",
      headers: {
        Authorization:
          "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw"
      }
    })
      .then(res => res.json())
      .then(res => res && setSeller(res.seller_list))
      .catch(e => console.log("셀러검색 에러 이거!!", e));
  };

  console.log("셀러검색 셀러 이거!!", seller);

  return (
    <Container>
      <Box>
        <Title>셀러 선택</Title>
        <Main>
          <InfoText>
            <InfoIcon>
              <InfoCircle />
            </InfoIcon>
            상품을 등록할 셀러를 선택해주세요. (검색 10건)
          </InfoText>
          <Search>
            <SearchText>셀러검색</SearchText>
            <SearchInput
              type="text"
              name="serchSlect"
              placeholder="Select..."
              onChange={getSearchSeller}
            />
            {seller
              ? seller.map((el, index) => {
                  return (
                    <Sellers key={index}>
                      <SellerName>{el.name_kr}</SellerName>
                    </Sellers>
                  );
                })
              : null}
          </Search>
        </Main>
        <Button>
          <Close onClick={showSellerSelect}>닫기</Close>

          <ChooseSeller
            onClick={() => getCategoryOne(seller.account_no, seller.name_kr)}
          >
            셀러 선택하기
          </ChooseSeller>
        </Button>
      </Box>
    </Container>
  );
};

export default SellerSelect;

const Container = styled.div`
  width: 100vw;
  height: 100vh;
  /* display: flex;
  justify-content: center;
  align-items: center; */
  position: fixed;
  top: 0;
  z-index: 1;
  background-color: rgba(0, 0, 0, 0.4);
  animation-fill-mode: both;
  ${props => {
    return css`
      animation: ${darken} 0.2s linear;
    `;
  }}
`;

const darken = keyframes`
from{
  opacity: 0;
}
to{
  opacity: 0.5;
}
`;

const Box = styled.div`
  width: 500px;
  /* height: 220px; */
  position: absolute;
  left: 450px;
  z-index: 5;
  border-radius: 5px;
  box-shadow: 2px 2px 2px 2px #333;
  background-color: #ffffff;
  ${() => {
    return css`
      animation: ${downModal} 0.3s linear;
      animation-delay: 0.3s;
      animation-fill-mode: forwards;
    `;
  }}
`;

const downModal = keyframes`
  from{
    top: -100px;
  }
  to{
    top: 394px;
  }
`;

const Title = styled.div`
  width: 100%;
  height: 57px;
  padding: 20px 0px 20px 10px;
  font-size: 18px;
  font-weight: ${styles.fontWeight.thin};
  border-bottom: 1px solid gray;
`;

const Main = styled.div`
  width: 100%;
  height: 97px;
  border-bottom: 1px solid gray;
`;

const InfoText = styled.div`
  display: flex;
  padding: 15px 0px 10px 15px;
  color: ${styles.color.infoBlue};
  font-size: 13px;
`;

const InfoIcon = styled.div`
  width: 13px;
  margin-right: 5px;
`;

const Search = styled.div`
  padding-top: 10px;
  display: flex;
  justify-content: space-around;
  align-items: center;
`;

const SearchText = styled.div`
  font-size: ${styles.fontSize.generalFont};
`;

const SearchInput = styled.input`
  width: 242px;
  height: 25px;
  border: 1px solid #e5e5e5;
  border-radius: 3px;
  padding: 12px;
  &:focus {
    border: 1px solid #e5e5e5;
  }
  font-size: 13px;
`;

const Sellers = styled.div`
  display: flex;
  flex-direction: column;
  width: 270px;
  height: 34px;
  border: 1px solid #e5e5e5;
  border-radius: 3px;
  padding: 10px;
`;

const SellerName = styled.p`
  width: 270px;
  height: 34px;
  font-size: 12px;
`;

const Button = styled.div`
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: 15px 10px 0px 0px;
`;

const Close = styled.div`
  border: 1px solid #e5e5e5;
  border-radius: 3px;
  padding: 10px;
  font-size: 13px;
  &:hover {
    filter: ${styles.filter.brightness};
  }
  cursor: pointer;
`;

const ChooseSeller = styled.button`
  margin-left: 10px;
  border-radius: 3px;
  padding: 10px;
  color: white;
  font-size: 13px;
  background-color: ${styles.color.buttonBlue};
  &:hover {
    filter: ${styles.filter.brightness};
  }
  cursor: pointer;
`;
