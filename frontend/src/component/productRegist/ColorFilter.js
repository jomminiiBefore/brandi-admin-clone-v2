import React, { useState } from "react";
import styled, { keyframes, css } from "styled-components";
import CustomButton from "src/component/common/CustomButton";
import styles from "src/utils/styles";

const ColorFilter = ({ showColorFilter, getColorData, colors }) => {
  // const colors = [
  //   {
  //     color_filter_no: 1,
  //     name_kr: "빨강",
  //     name_en: "Red",
  //     image_url: "http://sadmin.brandi.co.kr/include/img/product/color/red.png"
  //   },
  //   {
  //     color_filter_no: 2,
  //     name_kr: "주황",
  //     name_en: "Orange",
  //     image_url:
  //       "http://sadmin.brandi.co.kr/include/img/product/color/orange.png"
  //   },
  //   {
  //     color_filter_no: 3,
  //     name_kr: "노랑",
  //     name_en: "Yellow",
  //     image_url:
  //       "http://sadmin.brandi.co.kr/include/img/product/color/yellow.png"
  //   },
  //   {
  //     color_filter_no: 4,
  //     name_kr: "베이지",
  //     name_en: "Beige",
  //     image_url:
  //       "http://sadmin.brandi.co.kr/include/img/product/color/beige.png"
  //   },
  //   {
  //     color_filter_no: 5,
  //     name_kr: "갈색",
  //     name_en: "Brown",
  //     image_url:
  //       "http://sadmin.brandi.co.kr/include/img/product/color/brown.png"
  //   },
  //   {
  //     color_filter_no: 6,
  //     name_kr: "초록",
  //     name_en: "Green",
  //     image_url:
  //       "http://sadmin.brandi.co.kr/include/img/product/color/green.png"
  //   },
  //   {
  //     color_filter_no: 7,
  //     name_kr: "민트",
  //     name_en: "Mint",
  //     image_url: "http://sadmin.brandi.co.kr/include/img/product/color/mint.png"
  //   },
  //   {
  //     color_filter_no: 8,
  //     name_kr: "하늘",
  //     name_en: "Skyblue",
  //     image_url:
  //       "http://sadmin.brandi.co.kr/include/img/product/color/skyblue.png"
  //   },
  //   {
  //     color_filter_no: 9,
  //     name_kr: "파랑",
  //     name_en: "Blue",
  //     image_url: "http://sadmin.brandi.co.kr/include/img/product/color/blue.png"
  //   },
  //   {
  //     color_filter_no: 10,
  //     name_kr: "남색",
  //     name_en: "Navy",
  //     image_url: "http://sadmin.brandi.co.kr/include/img/product/color/navy.png"
  //   },
  //   {
  //     color_filter_no: 11,
  //     name_kr: "보라",
  //     name_en: "Violet",
  //     image_url:
  //       "http://sadmin.brandi.co.kr/include/img/product/color/violet.png"
  //   },
  //   {
  //     color_filter_no: 12,
  //     name_kr: "분홍",
  //     name_en: "Pink",
  //     image_url: "http://sadmin.brandi.co.kr/include/img/product/color/pink.png"
  //   },
  //   {
  //     color_filter_no: 13,
  //     name_kr: "골드",
  //     name_en: "Gold",
  //     image_url: "http://sadmin.brandi.co.kr/include/img/product/color/gold.png"
  //   },
  //   {
  //     color_filter_no: 14,
  //     name_kr: "로즈골드",
  //     name_en: "Rosegold",
  //     image_url:
  //       "http://sadmin.brandi.co.kr/include/img/product/color/rosegold.png"
  //   },
  //   {
  //     color_filter_no: 15,
  //     name_kr: "실버",
  //     name_en: "Sliver",
  //     image_url:
  //       "http://sadmin.brandi.co.kr/include/img/product/color/silver.png"
  //   }
  // ];

  const [selectedColorId, setSelectedColorId] = useState("");

  return (
    <Container>
      <Box>
        <Title>
          색상선택
          <TitleInfo>* 썸네일 이미지의 1개 색상만 선택 가능합니다.</TitleInfo>
        </Title>
        <Main>
          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              padding: "15px",
              marginLeft: "10px"
            }}
          >
            {colors.map((el, index) => {
              return (
                <ColorBox key={index} onClick={() => setSelectedColorId(el)}>
                  <ColorImg src={el.image_url} />
                  <ColorName>{el.name_kr}</ColorName>
                  <ColorEngName>({el.name_en})</ColorEngName>
                </ColorBox>
              );
            })}
          </div>
        </Main>
        <Button>
          <CustomButton
            name="적용"
            textColor="white"
            color={styles.color.buttonBlue}
            onClickEvent={() => getColorData(selectedColorId)}
          />
          <CustomButton name="취소" onClickEvent={showColorFilter} />
        </Button>
      </Box>
    </Container>
  );
};

export default ColorFilter;

const Container = styled.div`
  width: 100vw;
  height: 100vh;
  /* display: flex;
  justify-content: center;
  align-items: center; */
  position: fixed;
  top: 0%;
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
  height: 550px;
  position: absolute;
  left: 500px;
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
    top: 250px;
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

const TitleInfo = styled.span`
  margin-left: 15px;
  color: ${styles.color.infoBlue};
  font-size: 13px;
`;

const Main = styled.div`
  width: 100%;
  height: 427px;
  border-bottom: 1px solid gray;
`;

const ColorBox = styled.div`
  padding: 5px 0;
  width: 90px;
  height: 95px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  &:hover {
    background-color: rgba(0, 0, 0, 0.2);
  }
`;

const ColorImg = styled.img`
  width: 40px;
  border-radius: 100%;
`;

const ColorName = styled.div`
  font-size: 13px;
`;
const ColorEngName = styled.div`
  font-size: 13px;
`;

const Button = styled.div`
  display: flex;
  justify-content: center;
  padding-top: 18px;
`;
