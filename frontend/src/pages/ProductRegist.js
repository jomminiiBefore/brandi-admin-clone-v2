import React, { useState } from "react";
import { withRouter } from "react-router-dom";
// import CKEditor from "@ckeditor/ckeditor5-react";
// import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
// import Essentials from "@ckeditor/ckeditor5-essentials/src/essentials";
// import Paragraph from "@ckeditor/ckeditor5-paragraph/src/paragraph";
// import Bold from "@ckeditor/ckeditor5-basic-styles/src/bold";
// import Italic from "@ckeditor/ckeditor5-basic-styles/src/italic";
// import Heading from "@ckeditor/ckeditor5-heading/src/heading";
import styled from "styled-components";
import Layout from "src/component/common/Layout";
import TableBox from "src/component/common/TableBox";
import TableItem from "src/component/common/TableItem";
import InputContainer from "src/component/common/InputContainer";
import CustomButton from "src/component/common/CustomButton";
import styles from "src/utils/styles";
import { Warning } from "@styled-icons/entypo";
import { Home } from "@styled-icons/fa-solid";

const ProductRegist = () => {
  // const [serchSeller, setSerchSeller] = useState(false);
  // const handleSerchSeller = () => {
  //   setSerchSeller(true);
  // };

  const [sellerTypeId, setSellerTypeId] = useState("");
  const onChangeRadio = (e) => {
    setSellerTypeId(e.target.value);
    console.log(e.target.value);
  };

  // const [price, setPrice] = useState(0);
  // const handlePrice = (price, sale) => {
  //   setPrice(price - price / sale);
  //   return price;
  // };

  const [textUpload, setTextUpload] = useState(true);
  const handleTextUpload = (e) => {
    e.prevwntDefault();
    setTextUpload(!textUpload);
  };

  return (
    <Layout>
      <Container>
        <TitleBox>
          <MainTitle>상품 등록</MainTitle>
          <SubTitle>상품 정보 등록</SubTitle>
        </TitleBox>
        <PageBarBox>
          <HomeIcon>
            <Home />
          </HomeIcon>
          상품 관리 > 상품 관리 > 상품 등록
        </PageBarBox>
        <BasicInfoContainer>
          <TableBox title={"기본 정보"}>
            <TableItem title={"셀러 선택"} isRequired={true}>
              <InnerBox>
                <InputContainer
                  width="393"
                  height="34"
                  placeholder="셀러검색을 해주세요."
                />
                <CustomButton
                  name="셀러검색"
                  textColor="white"
                  color={styles.color.buttonGreen}
                  // onClickEvent={handleSerchSeller}
                />
              </InnerBox>
            </TableItem>
            <TableItem title={"판매 여부"} isRequired={false}>
              <RadioButtonContainer>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="saleYes"
                    name="sale"
                    value="saleYes"
                    defaultChecked="checked"
                    onChange={onChangeRadio}
                  />
                  <label>판매</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="saleNo"
                    name="sale"
                    value="saleNo"
                    onChange={onChangeRadio}
                  />
                  <label>미판매</label>
                </InputButtonBox>
              </RadioButtonContainer>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                미판매 선택시 앱에서 Sold Out으로 표시됩니다.
              </InfoText>
            </TableItem>
            <TableItem title={"진열 여부"} isRequired={false}>
              <RadioButtonContainer>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="shownYes"
                    name="shown"
                    value="shownYes"
                    defaultChecked="checked"
                    onChange={onChangeRadio}
                  />
                  <label>진열</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="shownNo"
                    name="shown"
                    value="shownNo"
                    onChange={onChangeRadio}
                  />
                  <label>미진열</label>
                </InputButtonBox>
              </RadioButtonContainer>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                미진열 선택시 앱에서 노출되지 않습니다.
              </InfoText>
            </TableItem>
            <TableItem title={"카테고리"} isRequired={true}>
              <CategoryTable>
                <tbody>
                  <CategoryTableTr>
                    <CategoryTableTh>1차 카테고리</CategoryTableTh>
                    <CategoryTableTh>2차 카테고리</CategoryTableTh>
                  </CategoryTableTr>
                  <CategoryTableTr>
                    <CategoryTableTd>
                      <CategoryTableSelect id="category1">
                        <option value="1차 카테고리를 선택해주세요.">
                          1차 카테고리를 선택해주세요.
                        </option>
                        <option value="아우터">아우터</option>
                        <option value="상의">상의</option>
                        <option value="스커트">스커트</option>
                        <option value="바지.">바지</option>
                        <option value="원피스">원피스</option>
                        <option value="신발">신발</option>
                        <option value="가방">가방</option>
                        <option value="잡화">잡화</option>
                        <option value="주얼리">주얼리</option>
                        <option value="라이프웨어">라이프웨어</option>
                        <option value="빅사이즈">빅사이즈</option>
                      </CategoryTableSelect>
                    </CategoryTableTd>
                    <CategoryTableTd>
                      <CategoryTableSelect id="category2">
                        <option value="1차 카테고리를 먼저 선택해주세요.">
                          1차 카테고리를 먼저 선택해주세요.
                        </option>
                      </CategoryTableSelect>
                    </CategoryTableTd>
                  </CategoryTableTr>
                </tbody>
              </CategoryTable>
            </TableItem>
            <TableItem title={"상품 정보 고시"} isRequired={true}>
              <RadioButtonContainer>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="productInfoYes"
                    name="productInfo"
                    value="productInfoYes"
                    defaultChecked="checked"
                    onChange={onChangeRadio}
                  />
                  <label>상품상세 참조</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="productInfoNo"
                    name="productInfo"
                    value="productInfoNo"
                    onChange={onChangeRadio}
                  />
                  <label>직접입력</label>
                </InputButtonBox>
              </RadioButtonContainer>
            </TableItem>
            <TableItem title={"상품명"} isRequired={true}>
              <InputContainer width="1000" height="34" />
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                상품명에는 쌍따옴표(") 또는 홑따옴표(')를 포함할 수 없습니다.
              </InfoText>
            </TableItem>
            <TableItem title={"한줄 상품 설명"} isRequired={false}>
              <InputContainer width="1000" height="34" />
            </TableItem>
            <TableItem title={"이미지 등록"} isRequired={true}>
              <InnerBox>
                <ImgInnerBox>
                  <ImgBox />
                  <CustomButton name="*대표 이미지 선택" />
                </ImgInnerBox>
                <ImgInnerBox>
                  <ImgBox />
                  <CustomButton name="이미지 선택" />
                </ImgInnerBox>
                <ImgInnerBox>
                  <ImgBox />
                  <CustomButton name="이미지 선택" />
                </ImgInnerBox>
                <ImgInnerBox>
                  <ImgBox />
                  <CustomButton name="이미지 선택" />
                </ImgInnerBox>
                <ImgInnerBox>
                  <ImgBox />
                  <CustomButton name="이미지 선택" />
                </ImgInnerBox>
              </InnerBox>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                640 * 720 사이즈 이상 등록 가능하며 확장자는 jpg 만 등록
                가능합니다.
              </InfoText>
            </TableItem>
            <TableItem title={"색상 필터 (썸네일 이미지)"} isRequired={true}>
              <InnerBox>
                <RadioButtonContainer>
                  <InputButtonBox>
                    <input
                      type="radio"
                      id="colorFilterNo"
                      name="colorFilter"
                      value="colorFilterNo"
                      defaultChecked="checked"
                      onChange={onChangeRadio}
                    />
                    <label>사용안함</label>
                  </InputButtonBox>
                  <InputButtonBox>
                    <input
                      type="radio"
                      id="colorFilterYes"
                      name="colorFilter"
                      value="colorFilterYes"
                      onChange={onChangeRadio}
                    />
                    <label>사용함</label>
                  </InputButtonBox>
                </RadioButtonContainer>
                <InputContainer width="204" height="34" />
                <CustomButton
                  name="적용할 색상 찾기"
                  textColor="white"
                  color={styles.color.buttonGreen}
                />
              </InnerBox>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                베스트 탭, 카테고리 페이지 및 검색페이지의 필터에 적용되며,
                선택하지 않으실 경우 색상필터를 사용한 검색결과에 노출되지
                않습니다.
              </InfoText>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                썸네일 이미지의 1개 색상만 선택 가능하며, 뷰티 및 다이어트
                카테고리의 상품의 경우 선택하실 수 없습니다.
              </InfoText>
            </TableItem>
            <TableItem title={"스타일 필터"} isRequired={true}>
              <RadioButtonContainer>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="styleFilterNone"
                    name="styleFilter"
                    value="styleFilterNone"
                    defaultChecked="checked"
                    onChange={onChangeRadio}
                  />
                  <label>선택안함</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="simpleBasic"
                    name="styleFilter"
                    value="simpleBasic"
                    onChange={onChangeRadio}
                  />
                  <label>심플베이직</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="lovely"
                    name="styleFilter"
                    value="lovely"
                    onChange={onChangeRadio}
                  />
                  <label>러블리</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="feminine"
                    name="styleFilter"
                    value="feminine"
                    onChange={onChangeRadio}
                  />
                  <label>페미닌</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="casual"
                    name="styleFilter"
                    value="casual"
                    onChange={onChangeRadio}
                  />
                  <label>캐주얼</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="sexyGlam"
                    name="styleFilter"
                    value="sexyGlam"
                    onChange={onChangeRadio}
                  />
                  <label>섹시글램</label>
                </InputButtonBox>
              </RadioButtonContainer>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                베스트 탭, 카테고리 페이지 및 검색페이지의 필터에 적용되며,
                선택하지 않으실 경우 색상필터를 사용한 검색결과에 노출되지
                않습니다.
              </InfoText>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                1개 스타일만 선택 가능하며, 브랜드 및 뷰티&다이어트 카테고리
                상품의 경우 선택하실 수 없습니다.
              </InfoText>
            </TableItem>
            <TableItem title={"연령 필터"} isRequired={true}>
              <CustomButton />
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                베스트 탭, 카테고리 페이지 및 검색페이지의 필터에 적용되며, 셀러
                정보 > 셀러태그정보의 연령대가 자동으로 적용됩니다.
              </InfoText>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                브랜드 및 뷰티&다이어트 카테고리 상품의 경우 적용되지 않습니다.
              </InfoText>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                해당 정보는 상품단위로 적용이 불가능하며(셀러 단위로만 가능),
                수정을 원하실 경우 카카오 플러스친구 '브랜디셀러'로 연락
                부탁드립니다.
              </InfoText>
            </TableItem>
            <TableItem title={"상세 상품 정보"} isRequired={true}>
              <RadioButtonContainer>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="easyUpload"
                    name="upload"
                    value="easyUpload"
                    defaultChecked="checked"
                    onChange={onChangeRadio}
                  />
                  <label>간편업로드</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="editor"
                    name="upload"
                    value="editor"
                    onChange={onChangeRadio}
                  />
                  <label>에디터 사용 (html 가능)</label>
                  <EditorInfoText>
                    ( 에디터에 따라서 상세 내용 화면에 다소 차이가 있을 수
                    있습니다. )
                  </EditorInfoText>
                </InputButtonBox>
              </RadioButtonContainer>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                상품상세이미지의 권장 사이즈는 가로사이즈 1000px 이상입니다.
              </InfoText>
              <Border />
              <EasyUploadBox>
                <EasyUploadInnerBox>
                  <CustomButton name="사진삽입" />
                  <ImgInfoText>
                    이미지 확장자는 JPG, PNG만 등록 가능합니다.
                  </ImgInfoText>
                </EasyUploadInnerBox>
                <DetailTextareaBox>
                  <textarea
                    style={{
                      width: "100%",
                      height: "350px",
                      padding: "10px",
                      border: "2px solid #eeeeee",
                      borderRadius: "5px",
                      fontSize: "13px",
                    }}
                  />
                </DetailTextareaBox>
              </EasyUploadBox>
              <WysiwygEditorBox>
                {/* <CKEditor
                  editor={ClassicEditor}
                  data="<p>Hello from CKEditor 5!</p>"
                  onInit={(editor) => {
                    // You can store the "editor" and use when it is needed.
                    console.log("Editor is ready to use!", editor);
                  }}
                  onChange={(event, editor) => {
                    const data = editor.getData();
                    console.log({ event, editor, data });
                  }}
                  config={{
                    plugins: [Essentials, Paragraph, Bold, Italic, Heading],
                    toolbar: [
                      "heading",
                      "|",
                      "bold",
                      "italic",
                      "|",
                      "undo",
                      "redo",
                    ],
                  }}
                /> */}
              </WysiwygEditorBox>
            </TableItem>
            <TableItem title={"유튜브 영상 URL"} isRequired={true}>
              <InnerBox>
                <InputContainer width="1000" height="34" />
                <CustomButton
                  name="미리보기"
                  textColor="white"
                  color={styles.color.buttonRed}
                />
              </InnerBox>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                https://www.youtube.com 또는 https://youtu.be로 시작하는 URL만
                등록 가능합니다.
              </InfoText>
            </TableItem>
          </TableBox>
        </BasicInfoContainer>
        <OptionInfoContainer>
          <TableBox title={"옵션 정보"}>
            <TableItem title={"옵션 설정"} isRequired={true}>
              <RadioButtonContainer>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="noOption"
                    name="option"
                    value="noOption"
                    defaultChecked="checked"
                  />
                  <label>옵션없음</label>
                </InputButtonBox>
              </RadioButtonContainer>
            </TableItem>
            <TableItem title={"옵션 정보"} isRequired={false}>
              <OptionTable>
                <tbody>
                  <OptionTableTr>
                    <OptionTableTh>도매처옵션명</OptionTableTh>
                    <OptionTableTh>일반재고</OptionTableTh>
                  </OptionTableTr>
                  <OptionTableTr>
                    <OptionTableTd>
                      <InputContainer width="300" height="34" />
                    </OptionTableTd>
                    <OptionTableTd>
                      <RadioButtonContainer>
                        <InputButtonBox>
                          <input
                            type="radio"
                            id="stockNo"
                            name="stock"
                            value="stockNo"
                            defaultChecked="checked"
                            onChange={onChangeRadio}
                          />
                          <label>재고관리 안함</label>
                        </InputButtonBox>
                        <InputButtonBox
                          style={{ display: "flex", alignItems: "center" }}
                        >
                          <input
                            type="radio"
                            id="stockYes"
                            name="stock"
                            value="stockYes"
                            onChange={onChangeRadio}
                          />
                          <InputContainer width="100" height="34" />
                          <label>개</label>
                        </InputButtonBox>
                      </RadioButtonContainer>
                    </OptionTableTd>
                  </OptionTableTr>
                </tbody>
              </OptionTable>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                컬러 - None, 사이즈 - Free로 노출됩니다.
              </InfoText>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                도매처옵션명 조합은 최대 100자까지 표시됩니다.
              </InfoText>
            </TableItem>
          </TableBox>
        </OptionInfoContainer>
        <SaleInfoContainer>
          <TableBox title={"판매 정보"}>
            <TableItem title={"도매 원가"} isRequired={false}>
              <InputContainer width="200" height="34" />
            </TableItem>
            <TableItem title={"판매가"} isRequired={true}>
              <InputContainer width="200" height="34" />
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                판매가는 원화기준 10원 이상이며 가격 입력 시 10원 단위로 입력해
                주세요.
              </InfoText>
            </TableItem>
            <TableItem title={"할인 정보"} isRequired={false}>
              <DiscountTable>
                <tbody>
                  <DiscountTr>
                    <DiscountTh>할인율</DiscountTh>
                    <DiscountTh>할인가</DiscountTh>
                  </DiscountTr>
                  <DiscountTr>
                    <DiscountTd>
                      <InputContainer width="80" height="34" />
                    </DiscountTd>
                    <DiscountTd>
                      <CustomButton
                        name="할인판매가적용"
                        textColor="white"
                        color={styles.color.buttonBlue}
                      />
                      원
                    </DiscountTd>
                  </DiscountTr>
                  <DiscountTr>
                    <DiscountTh>할인 판매가</DiscountTh>
                    <DiscountTd>원</DiscountTd>
                  </DiscountTr>
                  <DiscountTr>
                    <DiscountTh>할인 기간</DiscountTh>
                    <DiscountTd>
                      <RadioButtonContainer>
                        <InputButtonBox>
                          <input
                            type="radio"
                            id="noDeadline"
                            name="saleDeadline"
                            value="noDeadline"
                            defaultChecked="checked"
                            onChange={onChangeRadio}
                          />
                          <label>무기한</label>
                        </InputButtonBox>
                        <InputButtonBox>
                          <input
                            type="radio"
                            id="selectDate"
                            name="saleDeadline"
                            value="selectDate"
                            onChange={onChangeRadio}
                          />
                          <label>기간설정</label>
                        </InputButtonBox>
                      </RadioButtonContainer>
                    </DiscountTd>
                  </DiscountTr>
                </tbody>
              </DiscountTable>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                할인판매가 = 판매가 * 할인율
              </InfoText>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                할인 판매가 적용 버튼을 클릭 하시면 판매가 정보가 자동
                계산되어집니다.
              </InfoText>
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                할인 판매가는 원화기준 10원 단위로 자동 절사됩니다.
              </InfoText>
            </TableItem>
            <TableItem title={"최소 판매 수량"} isRequired={false}>
              <InnerBox>
                <RadioButtonContainer>
                  <InputButtonBox>
                    <input
                      type="radio"
                      id="oneOrMore"
                      name="minimumSales"
                      value="oneOrMore"
                      defaultChecked="checked"
                      onChange={onChangeRadio}
                    />
                    <label>1개 이상</label>
                  </InputButtonBox>
                  <InputButtonBox
                    style={{ display: "flex", alignItems: "center" }}
                  >
                    <input
                      type="radio"
                      id="nOrMore"
                      name="minimumSales"
                      value="nOrMore"
                      onChange={onChangeRadio}
                    />
                    <InputContainer width="100" height="34" />
                    <label>개 이상</label>
                  </InputButtonBox>
                </RadioButtonContainer>
                <InfoText>( 20개를 초과하여 설정하실 수 없습니다 )</InfoText>
              </InnerBox>
            </TableItem>
            <TableItem title={"최대 판매 수량"} isRequired={false}>
              <InnerBox>
                <RadioButtonContainer>
                  <InputButtonBox>
                    <input
                      type="radio"
                      id="twenty"
                      name="maximumSales"
                      value="twenty"
                      defaultChecked="checked"
                      onChange={onChangeRadio}
                    />
                    <label>20개</label>
                  </InputButtonBox>
                  <InputButtonBox
                    style={{ display: "flex", alignItems: "center" }}
                  >
                    <input
                      type="radio"
                      id="nOrLess"
                      name="maximumSales"
                      value="nOrLess"
                      onChange={onChangeRadio}
                    />
                    <InputContainer width="100" height="34" />
                    <label>개 이하</label>
                  </InputButtonBox>
                </RadioButtonContainer>
                <InfoText>( 20개를 초과하여 설정하실 수 없습니다 )</InfoText>
              </InnerBox>
            </TableItem>
            <TableItem title={"안전 인증 정보"} isRequired={false}>
              <RadioButtonContainer>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="safetyProductDetail"
                    name="safety"
                    value="safetyProductDetail"
                    defaultChecked="checked"
                    onChange={onChangeRadio}
                  />
                  <label>상품상세 참조</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="certificationTarget"
                    name="safety"
                    value="certificationTarget"
                    onChange={onChangeRadio}
                  />
                  <label>인증대상</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="NoneSafety"
                    name="safety"
                    value="NoneSafety"
                    onChange={onChangeRadio}
                  />
                  <label>해당사항 없음</label>
                </InputButtonBox>
              </RadioButtonContainer>
              <Border />
              <SafetyText>
                <p>
                  <RequiredIcon>*</RequiredIcon>
                  <MustRead>[필독]</MustRead>
                  정상적인 안전인증정보를 입력하지 않고 허위로 작성하신 경우
                  관계법령에 의거 처벌받으실 수 있습니다.
                </p>
                <p>
                  <RequiredIcon>*</RequiredIcon>
                  <MustRead>[필독]</MustRead>
                  상품상세 참조를 선택하신 경우 상품상세 페이지에 인증번호와
                  모델명, KC번호를 반드시 기재 부탁드립니다.
                </p>
                <p>
                  <RequiredIcon>*</RequiredIcon>
                  <MustRead>[필독]</MustRead>
                  (주)브랜디는 전기용품 및 생활용품안전관리법에 의거하여,
                  안전인증정보가 미기재 혹은 허위기재 된 상품에 대해 판매제한
                  조취를 취할 수 있습니다.
                </p>
              </SafetyText>
            </TableItem>
            <TableItem title={"상품 태그 관리"} isRequired={true}>
              <InputContainer
                width="1000"
                height="34"
                placeholder="해시태그(#) 를 제외한 상품 태그를 입력해주세요."
              />
            </TableItem>
          </TableBox>
        </SaleInfoContainer>
        <BottomButtoBox>
          <CustomButton
            name="등록"
            textColor="white"
            color={styles.color.buttonGreen}
          />
          <CustomButton
            name="취소"
            textColor="white"
            color={styles.color.buttonRed}
          />
        </BottomButtoBox>
      </Container>
    </Layout>
  );
};

export default withRouter(ProductRegist);

// Container
const Container = styled.div``;

const BasicInfoContainer = styled.div`
  padding: 15px 20px;
`;

const OptionInfoContainer = styled.div`
  padding: 0px 20px 15px 20px;
`;

const SaleInfoContainer = styled.div`
  padding: 0px 20px 15px 20px;
`;

const RadioButtonContainer = styled.div`
  display: felx;
  align-items: center;
`;

// Box
const InnerBox = styled.div`
  display: felx;
  align-items: center;
`;

const DetailTextareaBox = styled.div`
  padding: 10px;
`;

const TitleBox = styled.div`
  padding: 25px 20px 20px 20px;
  display: flex;
  align-items: flex-end;
`;

const PageBarBox = styled.div`
  width: 100vw-215px;
  height: 34px;
  padding-left: 20px;
  display: flex;
  align-items: center;
  color: #222222;
  font-size: 13px;
  background-color: #eee;
`;

const InputButtonBox = styled.div`
  margin-right: 30px;
  font-size: 13px;
`;

const ImgInnerBox = styled.div`
  display: flex;
  flex-direction: column;
`;

const ImgBox = styled.img`
  width: 150px;
  height: 150px;
  margin: 5px;
  background-size: cover;
  background-repeat: no-repeat;
  background-image: url("http://sadmin.brandi.co.kr/include/img/no_image.png");
`;

const EasyUploadBox = styled.div``;

const EasyUploadInnerBox = styled.div`
  display: flex;
  align-items: center;
`;

const WysiwygEditorBox = styled.div``;

const BottomButtoBox = styled.div`
  margin-bottom: 40px;
  display: flex;
  justify-content: center;
`;

// Icons & common
const HomeIcon = styled.div`
  width: 13px;
  margin-right: 5px;
  color: gray;
`;

const WarningIcon = styled.div`
  width: 13px;
  margin-right: 5px;
`;

const RequiredIcon = styled.span`
  margin-right: 5px;
  color: ${styles.color.requiredRed};
  font-size: 17px;
`;

const Border = styled.div`
  width: 100%;
  margin: 15px 0px;
  border: 1px solid #e5e5e5;
`;

const MustRead = styled.span`
  margin-right: 3px;
  font-size: 13px;
  font-weight: bold;
`;

// Title
const MainTitle = styled.div`
  color: #666;
  font-size: 26px;
  font-weight: ${styles.fontWeight.thin};
`;

const SubTitle = styled.div`
  padding: 0px 0px 3px 3px;
  color: #888;
  font-size: 14px;
  font-weight: ${styles.fontWeight.thin};
`;

// Text
const InfoText = styled.div`
  display: flex;
  align-items: flex-end;
  margin-top: 5px;
  color: ${styles.color.infoBlue};
  font-size: 12px;
`;

const EditorInfoText = styled.span`
  margin-left: 50px;
`;

const ImgInfoText = styled.div`
  margin-left: 15px;
  color: ${styles.color.requiredRed};
  font-size: 12px;
  font-weight: bold;
`;

const SafetyText = styled.div`
  margin-top: 10px;
  padding-top: 7px;
  line-height: 20px;
  font-size: 13px;
`;

// Table
const CategoryTable = styled.table`
  width: 100%;
  margin-bottom: 20px;
  border: 1px solid #e5e5e5;
`;

const CategoryTableTr = styled.tr`
  border: 1px solid #e5e5e5;
`;

const CategoryTableTh = styled.th`
  padding: 8px;
  border: 1px solid #e5e5e5;
  text-align: left;
  font-size: ${styles.fontSize.generalFont};
`;

const CategoryTableTd = styled.td`
  padding: 8px;
  border: 1px solid #e5e5e5;
`;

const CategoryTableSelect = styled.select`
  width: 100%;
  height: 34px;
  font-size: 13px;
`;

const OptionTable = styled.table`
  width: 100%;
  margin-bottom: 20px;
  border: 1px solid #e5e5e5;
`;

const OptionTableTr = styled.tr`
  border: 1px solid #e5e5e5;
`;

const OptionTableTh = styled.th`
  padding: 8px;
  border: 1px solid #e5e5e5;
  text-align: left;
  font-size: ${styles.fontSize.generalFont};
`;

const OptionTableTd = styled.td`
  padding: 8px;
  border: 1px solid #e5e5e5;
`;

const DiscountTable = styled.table`
  width: 50%;
  margin-bottom: 20px;
  border: 1px solid #e5e5e5;
`;

const DiscountTr = styled.tr`
  border: 1px solid #e5e5e5;
`;

const DiscountTh = styled.th`
  padding: 8px;
  border: 1px solid #e5e5e5;
  text-align: left;
  font-size: ${styles.fontSize.generalFont};
`;

const DiscountTd = styled.td`
  padding: 8px;
  border: 1px solid #e5e5e5;
  font-size: 13px;
`;
