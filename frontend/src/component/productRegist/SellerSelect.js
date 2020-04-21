import React, { useState, useEffect } from "react";
import styled, { keyframes, css } from "styled-components";
import { SHURL, YJURL, JMURL } from "src/utils/config";
import styles from "src/utils/styles";
import { InfoCircle } from "@styled-icons/fa-solid";

const SellerSelect = ({
  showSellerSelect,
  getCategoryOne,
  postData,
  setPostData
}) => {
  const [input, setInput] = useState("");

  const [seller, setSeller] = useState([]);

  const [selectedSeller, setSelectedSeller] = useState({
    id: "",
    name: ""
  });

  // 셀러검색 GET 함수
  const getSearchSeller = e => {
    setInput(e.target.value);
    const token = localStorage.getItem("token");
    fetch(`${JMURL}/seller?name_kr=${input}`, {
      method: "GET",
      headers: {
        Authorization: token
        // "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw"
      }
    })
      .then(res => res.json())
      .then(res => res && setSeller(res.seller_list))
      .catch(e => console.log("셀러검색 에러 이거!!", e));
  };

  useEffect(() => {
    console.log("셀러 아이디 이거!!", selectedSeller.id);
    if (selectedSeller.id !== "" && selectedSeller.name !== "") {
      setSeller([]);
      setInput(selectedSeller.name);
      setPostData({
        ...postData,
        selected_account_no: Number(selectedSeller.id)
      });
    }
  }, [selectedSeller]);
  console.log("셀러 이거!!", seller);
  const handleSeller = () => {
    getCategoryOne(selectedSeller);
    showSellerSelect();
  };

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
              value={input}
              onChange={getSearchSeller}
            />
          </Search>
          <SellersBox>
            {seller
              ? seller.map((el, index) => {
                  console.log("프로필 이미지 이거!!", el.profile_image_url);
                  if (el.profile_image_url) {
                    return (
                      <SellersMapBox
                        key={index}
                        onClick={() =>
                          setSelectedSeller({
                            ...selectedSeller,
                            id: el.account_no,
                            name: el.name_kr
                          })
                        }
                      >
                        <SellersMapImg src={el.profile_image_url} />
                        <div>{el.name_kr}</div>
                      </SellersMapBox>
                    );
                  }
                })
              : none}
          </SellersBox>
          {/* <SellersMapImg src="https://brandi-intern.s3.ap-northeast-2.amazonaws.com/2a7f8d1b-7c26-49c6-a252-15b3613568f0" /> */}
        </Main>
        <Button>
          <Close onClick={showSellerSelect}>닫기</Close>
          <ChooseSeller onClick={handleSeller}>셀러 선택하기</ChooseSeller>
        </Button>
      </Box>
    </Container>
  );
};

export default SellerSelect;

const Container = styled.div`
  width: 100vw;
  height: 100vh;
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
  position: relative;
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

const SellersBox = styled.div`
  width: 238px;
  position: absolute;
  left: 210px;
  background-color: white;
`;

const SellersMapBox = styled.div`
  width: 238px;
  height: 25px;
  display: flex;
  align-items: center;
  border: 1px solid #e5e5e5;
  padding: 5px;
  font-size: 13px;
  cursor: pointer;
  &:hover {
    background-color: #ccf1ff;
  }
`;

const SellersMapImg = styled.img`
  width: 20px;
  height: 20px;
  margin-right: 5px;
  border: 1px solid #ffcce1;
  border-radius: 3px;
  /* background-size: cover;
  background-repeat: no-repeat; */
  /* background-image: url("${props => props.url}"); */
`;

const Button = styled.div`
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  padding: 10px;
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
