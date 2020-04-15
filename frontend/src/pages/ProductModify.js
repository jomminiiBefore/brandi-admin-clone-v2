import React, { useState, useEffect } from "react";
import { render } from "react-dom";
import { withRouter } from "react-router-dom";
import styled from "styled-components";
import { SHURL, YJURL } from "src/utils/config";
import Layout from "src/component/common/Layout";
import TableBox from "src/component/common/TableBox";
import TableItem from "src/component/common/TableItem";
import CustomButton from "src/component/common/CustomButton";
import ColorFilter from "src/component/productRegist/ColorFilter";
import SellerSelect from "src/component/productRegist/SellerSelect";
import styles from "src/utils/styles";
import { Warning } from "@styled-icons/entypo";
import { Home } from "@styled-icons/fa-solid";
import "date-fns";
import DateFnsUtils from "@date-io/date-fns";
import Grid from "@material-ui/core/Grid";
import {
  MuiPickersUtilsProvider,
  KeyboardTimePicker,
  KeyboardDatePicker,
  DateTimePicker,
  KeyboardDateTimePicker
} from "@material-ui/pickers";
import { WithContext as ReactTags } from "react-tag-input";
// import { EditorState } from "draft-js";
// import { Editor } from "react-draft-wysiwyg";
import Wysiwyg from "src/component/productRegist/Wysiwyg";
import { setSeconds } from "date-fns";
// import CKEditor from "@ckeditor/ckeditor5-react";
// import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
// import Essentials from "@ckeditor/ckeditor5-essentials/src/essentials";
// import Paragraph from "@ckeditor/ckeditor5-paragraph/src/paragraph";
// import Bold from "@ckeditor/ckeditor5-basic-styles/src/bold";
// import Italic from "@ckeditor/ckeditor5-basic-styles/src/italic";
// import Heading from "@ckeditor/ckeditor5-heading/src/heading";

const KeyCodes = {
  comma: 188,
  enter: 13
};

const delimiters = [KeyCodes.comma, KeyCodes.enter];

const ProductRegist = () => {
  const [sellerName, setSellerName] = useState("");

  const [sellerSelect, setSellerSelect] = useState(false);

  const [colorFilter, setColorFilter] = useState(false);

  const [categoryOne, setCategoryOne] = useState([]);

  const [categoryTwo, setCategoryTwo] = useState([]);

  const [images, setImages] = useState({
    first: null,
    seconds: [null, null, null, null]
  });

  const [radioSelect, setRadioSelect] = useState({
    productInfo: false,
    colorFilter: false,
    stock: false,
    deadline: false,
    more: false,
    less: false,
    safety: 0
  });

  const [editorMode, setEditorMode] = useState(false);

  const [colorData, setColorData] = useState("");

  const productInfoText = e => {
    setEditorMode(false);
    setPostData({ ...postData, long_description: e.target.value });
  };

  const [postData, setPostData] = useState({
    is_available: 1,
    is_on_display: 1,
    first_category_id: null,
    second_category_id: null,
    name: "",
    color_filter_id: 19,
    style_filter_id: null,
    long_description: null,
    stock: 0,
    price: null,
    discount_rate: null,
    discount_start_time: null,
    discount_end_time: null,
    min_unit: 1,
    max_unit: 20,
    tags: [null, null],
    short_description: "",
    selected_account_no: 0,
    youtube_url: null,
    image_file_1: null,
    image_file_2: null,
    image_file_3: null,
    image_file_4: null,
    image_file_5: null
  });

  const [preview, setPreview] = useState({
    image_file_1: null,
    image_file_2: null,
    image_file_3: null,
    image_file_4: null,
    image_file_5: null
  });

  const [stockCount, setStockCount] = useState("");

  const [currentPrice, setCurrentPrice] = useState({
    offPrice: "",
    finalPrice: ""
  });

  const [moreQuantityCount, setMoreQuantityCount] = useState("");

  const [lessQuantityCount, setLessQuantityCount] = useState("");

  const [selectedDate, setSelectedDate] = React.useState(new Date());

  const [offDate, setOffDate] = useState({
    start: new Date(),
    end: new Date()
  });

  const [tags, setTags] = useState([]);

  // const [editorState, setEditorState] = useState(EditorState.createEmpty());
  // onEditorStateChange: Function = (editorState) => {
  //   // console.log(editorState)
  //   this.setState({
  //     editorState,
  //   });
  // };
  // const uploadImageCallBack = file => {
  //   return new Promise((resolve, reject) => {
  //     const xhr = new XMLHttpRequest();
  //     xhr.open("POST", "https://api.imgur.com/3/image");
  //     xhr.setRequestHeader("Authorization", "Client-ID XXXXX");
  //     const data = new FormData();
  //     data.append("image", file);
  //     xhr.send(data);
  //     xhr.addEventListener("load", () => {
  //       const response = JSON.parse(xhr.responseText);
  //       resolve(response);
  //     });
  //     xhr.addEventListener("error", () => {
  //       const error = JSON.parse(xhr.responseText);
  //       reject(error);
  //     });
  //   });
  // };
  // const onEditorStateChange = editorState => {
  //   // console.log(editorState)
  //   tsetEditorState(editorState);
  // };

  // 카테고리 1 GET 함수
  const getCategoryOne = seller => {
    setSellerName(seller.name);
    fetch(`${YJURL}/product/category?account_no=${seller.id}`, {
      method: "GET",
      headers: {
        Authorization:
          "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw"
      }
    })
      .then(res => res.json())
      .then(res => res && setCategoryOne(res))
      .catch(e => console.log("카테고리1 에러 이거", e));
  };

  // 1차 카테고리가 state에 담기면 2차 카테고리 GET
  useEffect(() => {
    if (postData.first_category_id !== null) {
      console.log("2차");
      // const token = localStorage.getItem("token");
      fetch(`${YJURL}/product/category/${postData.first_category_id}`, {
        method: "GET",
        headers: {
          Authorization:
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw"
        }
      })
        .then(res => res.json())
        .then(res => setCategoryTwo(res.second_categories));
    }
    // .catch(e => console.log("카테고리2 에러 이거", e));}
  }, [postData.first_category_id]);

  // 색상필터 색상 데이터
  const getColorData = data => {
    setPostData({ ...postData, color_filter_id: Number(data.color_filter_no) });
    setColorData(data);
    setColorFilter(false);
  };

  const handleDelete = i => {
    setTags(tags.filter((tag, index) => index !== i));
  };

  const handleAddition = tag => {
    setTags([...tags, tag]);
  };

  const handleDrag = (tag, currPos, newPos) => {
    // const tags = [...tags];
    // const newTags = tags.slice();
    // newTags.splice(currPos, 1);
    // newTags.splice(newPos, 0, tag);
    // // re-render
    // setTags(newTags);
  };

  const handleDateChange = date => {
    setSelectedDate(date);
  };

  // 셀러검색 modal
  const showSellerSelect = () => {
    setSellerSelect(!sellerSelect);
  };
  // const selectCategory = e => {
  //   setPostData({
  //     ...postData,
  //     first_category_id: e.target.value
  //   });
  // };
  // 색상필터 modal
  const [colors, setColors] = useState([]);
  const showColorFilter = () => {
    if (postData.color_filter_id !== 19) {
      fetch(`${YJURL}/product/color`)
        .then(res => res.json())
        .then(res => {
          if (res) {
            setColors(res.colors);
            setColorFilter(!colorFilter);
          }
        });
    } else {
      alert("사용함에 체크 해주세요.");
    }
  };

  // 대표 이미지 업로드
  const handleUploadImage = (e, number) => {
    console.dir(e.target);
    const file = e.target.files[0];
    console.log(file, "file");
    setPostData({ ...postData, [`image_file_${number}`]: file });
    const reader = new FileReader();
    reader.readAsDataURL(file);
    console.log(reader);
    reader.onloadend = () => {
      setPreview({ ...preview, [`image_file_${number}`]: reader.result });
    };
  };

  // 이미지 업로드
  // const handleUploadImages = (e, index) => {
  //   console.dir(e.target);
  //   const file = e.target.files[0];
  //   const reader = new FileReader();
  //   reader.readAsDataURL(file);
  //   console.log(reader);
  //   reader.onloadend = () => {
  //     let newImages = images;
  //     newImages[index] = reader.result;
  //     setImages({ ...images, seconds: newImages });
  //   };
  // };

  // 이미지 삭제
  const deleteImages = number => {
    setPostData({ ...postData, [`image_file_${number}`]: "" });
    setPreview({ ...preview, [`image_file_${number}`]: "" });
  };

  // 재고
  const handleStock = boolean => {
    if (!boolean) {
      setPostData({ ...postData, stock: -1 });
      setRadioSelect({ ...radioSelect, stock: false });
    } else if (boolean) {
      setPostData({ ...postData, stock: Number(stockCount) });
      setRadioSelect({ ...radioSelect, stock: true });
    }
  };
  useEffect(() => {
    handleStock(radioSelect.stock);
  }, [stockCount]);

  // 할인가격 계산
  const handlePrice = (offPrice, finalPrice) => {
    setCurrentPrice({
      ...currentPrice,
      offPrice: offPrice,
      finalPrice: finalPrice
    });
  };

  // 최소 판매 수량
  const handleMoreQuantity = boolean => {
    if (!boolean) {
      setPostData({ ...postData, min_unit: 1 });
      setRadioSelect({ ...radioSelect, more: false });
    } else if (boolean) {
      setPostData({ ...postData, min_unit: moreQuantityCount });
      setRadioSelect({ ...radioSelect, more: true });
    }
  };
  useEffect(() => {
    handleMoreQuantity(radioSelect.more);
  }, [moreQuantityCount]);

  // POST Data (formData)
  const SubmitData = () => {
    // const jsonData = JSON.stringify(postData);
    // const formData = new FormData();
    // formData.append("data", jsonData);
    let formData = new FormData();
    for (let key in postData) {
      console.log("data: ", key, postData[key]);
      formData.append(key, postData[key]);
    }
    fetch(`${YJURL}/product`, {
      method: "POST",
      headers: {
        Authorization:
          "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw"
        // "Content-Type": "multipart/form-data"
      },
      body: formData
    });
  };

  // 최대 판매 수량
  const handleLessQuantity = boolean => {
    if (!boolean) {
      setPostData({ ...postData, max_unit: 20 });
      setRadioSelect({ ...radioSelect, less: false });
    } else if (boolean) {
      setPostData({ ...postData, max_unit: lessQuantityCount });
      setRadioSelect({ ...radioSelect, less: true });
    }
  };
  useEffect(() => {
    handleLessQuantity(radioSelect.less);
  }, [lessQuantityCount]);

  // tags
  useEffect(() => {
    let newTags = [];
    tags.forEach(el => {
      newTags.push(el.text);
    });
    setPostData({ ...postData, tags: newTags });
  }, [tags]);

  console.log("포스트데이터 이거!!", postData);

  return (
    <Layout>
      <Container>
        <TitleBox>
          <MainTitle>상품 수정</MainTitle>
          <SubTitle>상품 정보 수정</SubTitle>
        </TitleBox>
        <PageBarBox>
          <HomeIcon>
            <Home />
          </HomeIcon>
          상품 관리 > 상품 관리 > 상품 수정
        </PageBarBox>
        <BasicInfoContainer>
          <TableBox title={"기본 정보"}>
            <TableItem title={"판매 여부"} isRequired={false}>
              <RadioButtonContainer>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="saleYes"
                    name="sale"
                    value="saleYes"
                    defaultChecked="checked"
                    onChange={() =>
                      setPostData({
                        ...postData,
                        is_available: 1
                      })
                    }
                  />
                  <label>판매</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="saleNo"
                    name="sale"
                    value="saleNo"
                    onChange={() =>
                      setPostData({
                        ...postData,
                        is_available: 0
                      })
                    }
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
                    onChange={() =>
                      setPostData({ ...postData, is_on_display: 1 })
                    }
                  />
                  <label>진열</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="shownNo"
                    name="shown"
                    value="shownNo"
                    onChange={() =>
                      setPostData({ ...postData, is_on_display: 0 })
                    }
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
                      <CategorySelect
                        id="category1"
                        onChange={e =>
                          setPostData({
                            ...postData,
                            first_category_id: Number(e.target.value)
                          })
                        }
                      >
                        <option>1차 카테고리를 선택해주세요.</option>
                        {categoryOne
                          ? categoryOne.map((el, index) => {
                              return (
                                <option
                                  key={index}
                                  value={el.first_category_no}
                                  // onChange={() => getCategoryTwo()}
                                >
                                  {el.name}
                                </option>
                              );
                            })
                          : null}
                      </CategorySelect>
                    </CategoryTableTd>
                    <CategoryTableTd>
                      <CategorySelect
                        id="category2"
                        onChange={e =>
                          setPostData({
                            ...postData,
                            second_category_id: Number(e.target.value)
                          })
                        }
                      >
                        <option>1차 카테고리를 먼저 선택해주세요.</option>
                        {categoryTwo
                          ? categoryTwo.map((el, index) => {
                              return (
                                <option
                                  key={index}
                                  value={el.second_category_no}
                                >
                                  {el.name}
                                </option>
                              );
                            })
                          : null}
                      </CategorySelect>
                    </CategoryTableTd>
                  </CategoryTableTr>
                </tbody>
              </CategoryTable>
            </TableItem>
            <TableItem title={"상품 정보 고시"} isRequired={true}>
              <div>
                <RadioButtonContainer>
                  <InputButtonBox>
                    <input
                      type="radio"
                      id="productInfoReference"
                      name="productInfo"
                      value="productInfoReference"
                      checked={!radioSelect.productInfo}
                      onChange={() => {
                        setRadioSelect({ ...radioSelect, productInfo: false });
                      }}
                    />
                    <label>상품상세 참조</label>
                  </InputButtonBox>
                  <InputButtonBox>
                    <input
                      type="radio"
                      id="productInfoSelf"
                      name="productInfo"
                      value="productInfoSelf"
                      checked={radioSelect.productInfo}
                      onChange={() => {
                        setRadioSelect({ ...radioSelect, productInfo: true });
                      }}
                    />
                    <label>직접입력</label>
                  </InputButtonBox>
                </RadioButtonContainer>
                {radioSelect.productInfo ? (
                  <SelfWriteContainer>
                    <Manufacturer>
                      <ManufacturerText>제조사(수입사) : </ManufacturerText>
                      <ManufacturerInput />
                    </Manufacturer>
                    <ManufacturerDate>
                      <ManufacturerDateText>제조일자 : </ManufacturerDateText>
                      <Calendar>
                        <MuiPickersUtilsProvider utils={DateFnsUtils}>
                          <Grid container justify="space-around">
                            <KeyboardDatePicker
                              disableToolbar
                              variant="inline"
                              format="MM/dd/yyyy"
                              margin="normal"
                              id="date-picker-inline"
                              label="Date picker inline"
                              value={selectedDate}
                              onChange={handleDateChange}
                              KeyboardButtonProps={{
                                "aria-label": "change date"
                              }}
                            />
                          </Grid>
                        </MuiPickersUtilsProvider>
                      </Calendar>
                    </ManufacturerDate>
                    <Oigin>
                      <OiginText>원산지 :</OiginText>
                      <OiginSelect>
                        <option defaultValue="한국">한국</option>
                        <option value="기타">기타</option>
                        <option value="중국">중국</option>
                        <option value="베트남">베트남</option>
                      </OiginSelect>
                    </Oigin>
                  </SelfWriteContainer>
                ) : null}
              </div>
            </TableItem>
            <TableItem title={"상품명"} isRequired={true}>
              <NormalInput
                defaultValue={postData.name}
                onChange={e => {
                  setPostData({ ...postData, name: e.target.value });
                }}
                width="390"
                height="34"
              />
              <InfoText>
                <WarningIcon>
                  <Warning />
                </WarningIcon>
                상품명에는 쌍따옴표(") 또는 홑따옴표(')를 포함할 수 없습니다.
              </InfoText>
            </TableItem>
            <TableItem title={"한줄 상품 설명"} isRequired={false}>
              <NormalInput
                value={postData.short_description}
                onChange={e => {
                  setPostData({
                    ...postData,
                    short_description: e.target.value
                  });
                }}
                width="390"
                height="34"
              />
            </TableItem>
            <TableItem title={"이미지 등록"} isRequired={true}>
              <InnerBox>
                <ImgInnerBox>
                  <ImgBox
                    style={
                      preview.image_file_1
                        ? { backgroundImage: `url(${preview.image_file_1})` }
                        : null
                    }
                  />
                  {preview.image_file_1 ? (
                    <ButtonWrapper>
                      * 대표 이미지 변경
                      <UploadButton
                        accept="image/*"
                        onChange={e => handleUploadImage(e, 1)}
                        type="file"
                      />
                    </ButtonWrapper>
                  ) : (
                    <ButtonWrapper>
                      * 대표 이미지 선택
                      <UploadButton
                        accept="image/*"
                        style={{ width: "140px" }}
                        onChange={e => handleUploadImage(e, 1)}
                        type="file"
                      />
                    </ButtonWrapper>
                  )}
                </ImgInnerBox>
                <ImgInnerBox>
                  <ImgBox
                    style={
                      preview.image_file_2
                        ? { backgroundImage: `url(${preview.image_file_2})` }
                        : null
                    }
                  />
                  {preview.image_file_2 ? (
                    <div style={{ display: "flex" }}>
                      <ButtonWrapper style={{ width: "106px" }}>
                        이미지 변경
                        <UploadButton
                          accept="image/*"
                          style={{ width: "106px" }}
                          onChange={e => handleUploadImage(e, 2)}
                          type="file"
                        />
                      </ButtonWrapper>
                      <DeleteButton onClick={() => deleteImages(2)}>
                        삭제
                      </DeleteButton>
                    </div>
                  ) : (
                    <ButtonWrapper>
                      이미지 선택
                      <UploadButton
                        accept="image/*"
                        style={{ width: "140px" }}
                        onChange={e => handleUploadImage(e, 2)}
                        type="file"
                      />
                    </ButtonWrapper>
                  )}
                </ImgInnerBox>
                <ImgInnerBox>
                  <ImgBox
                    style={
                      preview.image_file_3
                        ? { backgroundImage: `url(${preview.image_file_3})` }
                        : null
                    }
                  />
                  {preview.image_file_3 ? (
                    <div style={{ display: "flex" }}>
                      <ButtonWrapper style={{ width: "106px" }}>
                        이미지 변경
                        <UploadButton
                          accept="image/*"
                          style={{ width: "106px" }}
                          onChange={e => handleUploadImage(e, 3)}
                          type="file"
                        />
                      </ButtonWrapper>
                      <DeleteButton onClick={() => deleteImages(3)}>
                        삭제
                      </DeleteButton>
                    </div>
                  ) : (
                    <ButtonWrapper>
                      이미지 선택
                      <UploadButton
                        accept="image/*"
                        style={{ width: "140px" }}
                        onChange={e => handleUploadImage(e, 3)}
                        type="file"
                      />
                    </ButtonWrapper>
                  )}
                </ImgInnerBox>
                <ImgInnerBox>
                  <ImgBox
                    style={
                      preview.image_file_4
                        ? { backgroundImage: `url(${preview.image_file_4})` }
                        : null
                    }
                  />
                  {preview.image_file_4 ? (
                    <div style={{ display: "flex" }}>
                      <ButtonWrapper style={{ width: "106px" }}>
                        이미지 변경
                        <UploadButton
                          accept="image/*"
                          style={{ width: "106px" }}
                          onChange={e => handleUploadImage(e, 4)}
                          type="file"
                        />
                      </ButtonWrapper>
                      <DeleteButton onClick={() => deleteImages(4)}>
                        삭제
                      </DeleteButton>
                    </div>
                  ) : (
                    <ButtonWrapper>
                      이미지 선택
                      <UploadButton
                        accept="image/*"
                        style={{ width: "140px" }}
                        onChange={e => handleUploadImage(e, 4)}
                        type="file"
                      />
                    </ButtonWrapper>
                  )}
                </ImgInnerBox>
                <ImgInnerBox>
                  <ImgBox
                    style={
                      preview.image_file_5
                        ? { backgroundImage: `url(${preview.image_file_5})` }
                        : null
                    }
                  />
                  {preview.image_file_5 ? (
                    <div style={{ display: "flex" }}>
                      <ButtonWrapper style={{ width: "106px" }}>
                        이미지 변경
                        <UploadButton
                          accept="image/*"
                          style={{ width: "106px" }}
                          onChange={e => handleUploadImage(e, 5)}
                          type="file"
                        />
                      </ButtonWrapper>
                      <DeleteButton onClick={() => deleteImages(5)}>
                        삭제
                      </DeleteButton>
                    </div>
                  ) : (
                    <ButtonWrapper>
                      이미지 선택
                      <UploadButton
                        accept="image/*"
                        style={{ width: "140px" }}
                        onChange={e => handleUploadImage(e, 5)}
                        type="file"
                      />
                    </ButtonWrapper>
                  )}
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
                      onChange={() =>
                        setPostData({ ...postData, color_filter_id: 19 })
                      }
                    />
                    <label>사용안함</label>
                  </InputButtonBox>
                  <InputButtonBox>
                    <input
                      type="radio"
                      id="colorFilterYes"
                      name="colorFilter"
                      value="colorFilterYes"
                      onChange={() =>
                        setPostData({
                          ...postData,
                          color_filter_id: colors.color_filter_no
                        })
                      }
                    />
                    <label>사용함</label>
                  </InputButtonBox>
                </RadioButtonContainer>
                <ColorSelected disabled>
                  {colorData ? (
                    <div style={{ display: "flex", alignItems: "center" }}>
                      <Color src={colorData.image_url} />
                      <ColorName>
                        {colorData.name_kr}({colorData.name_en})
                      </ColorName>
                    </div>
                  ) : null}
                </ColorSelected>

                <ColorButton onClick={showColorFilter}>
                  적용할 색상 찾기
                </ColorButton>
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
                    onChange={() =>
                      setPostData({ ...postData, style_filter_id: 1 })
                    }
                  />
                  <label>선택안함</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="simpleBasic"
                    name="styleFilter"
                    value="simpleBasic"
                    onChange={() =>
                      setPostData({ ...postData, style_filter_id: 2 })
                    }
                  />
                  <label>심플베이직</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="lovely"
                    name="styleFilter"
                    value="lovely"
                    onChange={() =>
                      setPostData({ ...postData, style_filter_id: 3 })
                    }
                  />
                  <label>러블리</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="feminine"
                    name="styleFilter"
                    value="feminine"
                    onChange={() =>
                      setPostData({ ...postData, style_filter_id: 4 })
                    }
                  />
                  <label>페미닌</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="casual"
                    name="styleFilter"
                    value="casual"
                    onChange={() =>
                      setPostData({ ...postData, style_filter_id: 5 })
                    }
                  />
                  <label>캐주얼</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="sexyGlam"
                    name="styleFilter"
                    value="sexyGlam"
                    onChange={() =>
                      setPostData({ ...postData, style_filter_id: 6 })
                    }
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
                    onChange={() => setEditorMode(false)}
                  />
                  <label>간편업로드</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="editor"
                    name="upload"
                    value="editor"
                    onChange={() => setEditorMode(true)}
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
              {editorMode ? (
                <Wysiwyg setPostData={setPostData} postData={postData} />
              ) : (
                <EasyUploadBox>
                  {/* <EasyUploadInnerBox>
                    <CustomButton name="사진삽입" />
                    <ImgInfoText>
                      이미지 확장자는 JPG, PNG만 등록 가능합니다.
                    </ImgInfoText>
                  </EasyUploadInnerBox> */}
                  <DetailTextareaBox>
                    <textarea
                      onChange={e => productInfoText(e)}
                      style={{
                        width: "100%",
                        height: "350px",
                        padding: "10px",
                        border: "2px solid #eeeeee",
                        borderRadius: "5px",
                        fontSize: "13px"
                      }}
                    />
                  </DetailTextareaBox>
                </EasyUploadBox>
              )}
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
            <TableItem title={"유튜브 영상 URL"} isRequired={false}>
              <InnerBox>
                <NormalInput
                  onChange={e => {
                    setPostData({ ...postData, youtube_url: e.target.value });
                  }}
                  width="390"
                  height="34"
                />
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
                    disabled
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
                      <NormalInput width="300" height="34" />
                    </OptionTableTd>
                    <OptionTableTd>
                      <RadioButtonContainer>
                        <InputButtonBox>
                          <input
                            type="radio"
                            id="stockNo"
                            name="stock"
                            value="stockNo"
                            checked={!radioSelect.stock}
                            onChange={() => handleStock(false)}
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
                            checked={radioSelect.stock}
                            onChange={() => handleStock(true)}
                          />
                          <NormalInput
                            width="100"
                            height="34"
                            disabled={radioSelect.stock ? false : true}
                            value={stockCount}
                            onChange={e => {
                              setStockCount(e.target.value);
                            }}
                          />
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
            <TableItem title={"도매 원가"} isRequired={true}>
              <NormalInput width="200" height="34" />
            </TableItem>
            <TableItem title={"판매가"} isRequired={true}>
              <NormalInput
                onChange={e =>
                  setPostData({ ...postData, price: Number(e.target.value) })
                }
                width="200"
                height="34"
              />
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
                      <NormalInput
                        onChange={e => {
                          setPostData({
                            ...postData,
                            discount_rate: Number(e.target.value)
                          });
                        }}
                        width="80"
                        height="34"
                      />
                    </DiscountTd>
                    <DiscountTd>
                      {currentPrice.offPrice}원
                      <ClacButton
                        onClick={() => {
                          handlePrice(
                            postData.price * (postData.discount_rate / 100),
                            postData.price -
                              postData.price * (postData.discount_rate / 100)
                          );
                        }}
                      >
                        할인판매가적용
                      </ClacButton>
                    </DiscountTd>
                  </DiscountTr>
                  <DiscountTr>
                    <DiscountTh>할인 판매가</DiscountTh>
                    <DiscountTd>{currentPrice.finalPrice}원</DiscountTd>
                  </DiscountTr>
                  <DiscountTr>
                    <DiscountTh>할인 기간</DiscountTh>
                    <DiscountTd>
                      <div>
                        <RadioButtonContainer>
                          <InputButtonBox>
                            <input
                              type="radio"
                              id="noDeadline"
                              name="saleDeadline"
                              value="noDeadline"
                              checked={!radioSelect.deadline}
                              onChange={() =>
                                setRadioSelect({
                                  ...radioSelect,
                                  deadline: false
                                })
                              }
                            />
                            <label>무기한</label>
                          </InputButtonBox>
                          <InputButtonBox>
                            <input
                              type="radio"
                              id="selectDate"
                              name="saleDeadline"
                              value="selectDate"
                              checked={radioSelect.deadline}
                              onChange={() =>
                                setRadioSelect({
                                  ...radioSelect,
                                  deadline: true
                                })
                              }
                            />
                            <label>기간설정</label>
                          </InputButtonBox>
                        </RadioButtonContainer>
                        {radioSelect.deadline ? (
                          <DeadlineBox>
                            <Calendar>
                              <MuiPickersUtilsProvider utils={DateFnsUtils}>
                                <Grid container justify="space-around">
                                  <KeyboardDateTimePicker
                                    disableToolbar
                                    variant="inline"
                                    format="yyyy/MM/dd HH:mm"
                                    margin="normal"
                                    id="date-picker-inline"
                                    label="시작"
                                    value={postData.discount_start_time}
                                    onChange={date =>
                                      setPostData({
                                        ...postData,
                                        discount_start_time: date
                                      })
                                    }
                                    KeyboardButtonProps={{
                                      "aria-label": "change date"
                                    }}
                                  />

                                  <KeyboardDateTimePicker
                                    disableToolbar
                                    variant="inline"
                                    format="yyyy/MM/dd HH:mm"
                                    margin="normal"
                                    id="date-picker-inline"
                                    label="끝"
                                    value={postData.discount_end_time}
                                    onChange={date =>
                                      setPostData({
                                        ...postData,
                                        discount_end_time: date
                                      })
                                    }
                                    KeyboardButtonProps={{
                                      "aria-label": "change date"
                                    }}
                                  />
                                </Grid>
                              </MuiPickersUtilsProvider>
                            </Calendar>
                            <p style={{ color: "red" }}>
                              * 할인기간을 설정시 기간만료되면 자동으로 정상가로
                              변경 됩니다.
                            </p>
                          </DeadlineBox>
                        ) : null}
                      </div>
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
                      id="one"
                      name="minimumSales"
                      value="one"
                      checked={!radioSelect.more}
                      onChange={() => handleMoreQuantity(false)}
                    />
                    <label>1개 이상</label>
                  </InputButtonBox>
                  <InputButtonBox
                    style={{ display: "flex", alignItems: "center" }}
                  >
                    <input
                      type="radio"
                      id="more"
                      name="minimumSales"
                      value="more"
                      checked={radioSelect.more}
                      onChange={() => handleMoreQuantity(true)}
                    />
                    <NormalInput
                      width="100"
                      height="34"
                      disabled={radioSelect.more ? false : true}
                      value={moreQuantityCount}
                      onChange={e => setMoreQuantityCount(e.target.value)}
                    />
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
                      checked={!radioSelect.less}
                      onChange={() => {
                        handleLessQuantity(false);
                      }}
                    />
                    <label>20개</label>
                  </InputButtonBox>
                  <InputButtonBox
                    style={{ display: "flex", alignItems: "center" }}
                  >
                    <input
                      type="radio"
                      id="less"
                      name="maximumSales"
                      value="less"
                      checked={radioSelect.less}
                      onChange={() => {
                        handleLessQuantity(true);
                      }}
                    />
                    <NormalInput
                      width="100"
                      height="34"
                      disabled={radioSelect.less ? false : true}
                      onChange={e => {
                        setLessQuantityCount(e.target.value);
                      }}
                    />
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
                    id="detailReference"
                    name="safety"
                    value="detailReference"
                    checked={radioSelect.safety === 0}
                    onChange={() =>
                      setRadioSelect({ ...radioSelect, safety: 0 })
                    }
                  />
                  <label>상품상세 참조</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="certificationTarget"
                    name="safety"
                    value="certificationTarget"
                    checked={radioSelect.safety === 1}
                    onChange={() =>
                      setRadioSelect({ ...radioSelect, safety: 1 })
                    }
                  />
                  <label>인증대상</label>
                </InputButtonBox>
                <InputButtonBox>
                  <input
                    type="radio"
                    id="NoneSafety"
                    name="safety"
                    value="NoneSafety"
                    checked={radioSelect.safety === 2}
                    onChange={() =>
                      setRadioSelect({ ...radioSelect, safety: 2 })
                    }
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
              <div>
                <HashTags
                  tags={tags}
                  handleDelete={handleDelete}
                  handleAddition={handleAddition}
                  handleDrag={() => {}}
                  delimiters={delimiters}
                  inputFieldPosition="inline"
                  placeholder="해시태그(#) 를 제외한 상품 태그를 입력해주세요."
                />
              </div>
            </TableItem>
          </TableBox>
        </SaleInfoContainer>
        <form encType="multipart/form-data" method="post">
          <BottomButtoBox>
            <CustomButton
              name="수정"
              textColor="white"
              color={styles.color.buttonGreen}
              onClickEvent={SubmitData}
            />
            <CustomButton
              name="취소"
              textColor="white"
              color={styles.color.buttonRed}
            />
          </BottomButtoBox>
        </form>
      </Container>
      {colorFilter && (
        <ColorFilter
          showColorFilter={showColorFilter}
          getColorData={getColorData}
          colors={colors}
        />
      )}
      {sellerSelect && (
        <SellerSelect
          showSellerSelect={showSellerSelect}
          getCategoryOne={getCategoryOne}
          setPostData={setPostData}
          postData={postData}
        />
      )}
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

const SelfWriteContainer = styled.div`
  margin-top: 5px;
  border-radius: 3px;
  padding: 10px;
  font-size: 13px;
  background-color: #eeeeee;
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
  display: flex;
  align-items: flex-end;
  padding: 25px 20px 20px 20px;
`;

const PageBarBox = styled.div`
  width: 100vw-215px;
  height: 34px;
  display: flex;
  align-items: center;
  padding-left: 20px;
  color: #222222;
  font-size: 13px;
  background-color: #eee;
`;

const SearchButton = styled.div`
  padding: 10px;
  color: white;
  border-radius: 5px;
  font-size: 13px;
  background-color: ${styles.color.buttonGreen};
  cursor: pointer;
  &:hover {
    filter: ${styles.filter.brightness};
  }
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

const DeadlineBox = styled.div``;

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

const NormalInput = styled.input`
  width: ${props => props.width}px;
  height: ${props => props.height}px;
  margin-right: 5px;
  border: 1px solid #e5e5e5;
  border-radius: 3px;
  padding: 10px;
  font-size: 13px;
  &:focus {
    border: 1px solid #e5e5e5;
  }
`;

// disabled input
const JustBox = styled.input`
  width: ${props => props.width};
  height: ${props => props.height};
  margin-right: 10px;
  border: 1px solid #e5e5e5;
  border-radius: 3px;
  padding: 10px;
  font-size: 12px;
  background-color: #eeeeee;
  cursor: not-allowed;
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
  margin-top: 10px;
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
  border: 1px solid #e5e5e5;
  padding: 8px;
  text-align: left;
  font-size: ${styles.fontSize.generalFont};
`;

const CategoryTableTd = styled.td`
  padding: 8px;
  border: 1px solid #e5e5e5;
`;

const CategorySelect = styled.select`
  width: 80%;
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
  border: 1px solid #e5e5e5;
  padding: 8px;
  text-align: left;
  font-size: ${styles.fontSize.generalFont};
`;

const OptionTableTd = styled.td`
  border: 1px solid #e5e5e5;
  padding: 8px;
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
  border: 1px solid #e5e5e5;
  padding: 8px;
  text-align: left;
  font-size: ${styles.fontSize.generalFont};
`;

const DiscountTd = styled.td`
  border: 1px solid #e5e5e5;
  padding: 8px;
  font-size: 13px;
`;

// 상품 정보 고시 ( 직접 입력 )
const Manufacturer = styled.div`
  display: flex;
  align-items: center;
`;

const ManufacturerText = styled.p``;

const ManufacturerInput = styled.input`
  width: 240px;
  height: 34px;
  margin-left: 5px;
  border: 1px solid #878787;
  border-radius: 5px;
  padding: 5px;
  font-size: 13px;
  &:focus {
    border: 1px solid #878787;
  }
`;

const ManufacturerDate = styled.div`
  margin-top: 8px;
  display: flex;
`;

const ManufacturerDateText = styled.p``;

const Calendar = styled.div`
  padding: 5px;
`;

const Oigin = styled.div`
  margin-top: 8px;
  display: flex;
  align-items: center;
`;

const OiginText = styled.p``;

const OiginSelect = styled.select`
  width: 240px;
  height: 34px;
  margin-left: 5px;
  padding: 10px;
`;

// 이미지 버튼
const ButtonWrapper = styled.span`
  width: 150px;
  position: relative;
  display: inline-block;
  margin-left: 5px;
  border: 1px solid #e5e5e5;
  border-radius: 5px;
  padding: 5px;
  text-align: center;
  font-size: 13px;
  background-color: white;
  cursor: pointer;
  &:hover {
    filter: ${styles.filter.brightness};
  }
`;

const UploadButton = styled.input`
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
  opacity: 0;
`;

const DeleteButton = styled.div`
  width: 40px;
  margin-left: 5px;
  padding: 5px;
  text-align: center;
  color: white;
  font-size: 12px;
  border-radius: 5px;
  background-color: ${styles.color.buttonRed};
  cursor: pointer;
  &:hover {
    filter: ${styles.filter.brightness};
  }
`;

const ClacButton = styled.div`
  width: 110px;
  border: 1px solid gray;
  border-radius: 5px;
  padding: 10px;
  color: white;
  background-color: ${styles.color.buttonBlue};
  cursor: pointer;
  &:hover {
    filter: ${styles.filter.brightness};
  }
`;

// 색상필터
const Color = styled.img`
  width: 18px;
  height: 18px;
  border-radius: 100%;
`;

const ColorName = styled.p`
  margin-left: 5px;
  font-size: 13px;
`;

const ColorButton = styled.button`
  padding: 7px;
  border-radius: 5px;
  color: white;
  font-size: 13px;
  background-color: ${styles.color.buttonGreen};
  cursor: pointer;
  &:hover {
    filter: ${styles.filter.brightness};
  }
`;

const ColorSelected = styled.div`
  width: 205px;
  height: 34px;
  margin-right: 10px;
  border: 1px solid #e5e5e5;
  border-radius: 3px;
  padding: 10px;
  font-size: 12px;
  background-color: #eeeeee;
  cursor: not-allowed;
`;

const HashTags = styled(ReactTags)``;
