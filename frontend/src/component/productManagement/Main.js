import React, { useEffect } from "react";
import { withRouter } from "react-router-dom";
import { YJURL, JMURL } from "src/utils/config";
import PropTypes from "prop-types";
import EnhancedTableHead from "src/component/productManagement/EnhancedTableHead";
import CustomButton from "src/component/common/CustomButton";
import SmallButton from "src/component/common/SmallButton";
import clsx from "clsx";
import { lighten, makeStyles } from "@material-ui/core/styles";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TablePagination from "@material-ui/core/TablePagination";
import TableRow from "@material-ui/core/TableRow";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";
import Checkbox from "@material-ui/core/Checkbox";
import IconButton from "@material-ui/core/IconButton";
import Tooltip from "@material-ui/core/Tooltip";
import DeleteIcon from "@material-ui/icons/Delete";
import Select from "@material-ui/core/Select";
import FilterListIcon from "@material-ui/icons/FilterList";
import DatePicker from "react-date-picker";
import InputLabel from "@material-ui/core/InputLabel";

// select
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";

import style from "src/utils/styles";
import styled, { keyframes, css } from "styled-components";

function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein };
}

const itemRows = [
  createData("Cupcake", 305, 3.7, 67, 4.3),
  createData("Donut", 452, 25.0, 51, 4.9),
  createData("Eclair", 262, 16.0, 24, 6.0),
  createData("Frozen yoghurt", 159, 6.0, 24, 4.0),
  createData("Gingerbread", 356, 16.0, 49, 3.9),
  createData("Honeycomb", 408, 3.2, 87, 6.5),
  createData("Ice cream sandwich", 237, 9.0, 37, 4.3),
  createData("Jelly Bean", 375, 0.0, 94, 0.0),
  createData("KitKat", 518, 26.0, 65, 7.0),
  createData("Lollipop", 392, 0.2, 98, 0.0),
  createData("Marshmallow", 318, 0, 81, 2.0),
  createData("Nougat", 360, 19.0, 9, 37.0),
  createData("Oreo", 437, 18.0, 63, 4.0)
];

function descendingComparator(a, b, orderBy) {
  if (b[orderBy] < a[orderBy]) {
    return -1;
  }
  if (b[orderBy] > a[orderBy]) {
    return 1;
  }
  return 0;
}

const useToolbarStyles = makeStyles(theme => ({
  root: {
    paddingLeft: theme.spacing(0),
    paddingRight: theme.spacing(0)
  },
  highlight:
    theme.palette.type === "light"
      ? {
          color: theme.palette.secondary.main,
          backgroundColor: lighten(theme.palette.secondary.light, 0.85)
        }
      : {
          color: theme.palette.text.primary,
          backgroundColor: theme.palette.secondary.dark
        },
  title: {
    flex: "1 1 100%"
  }
}));

const EnhancedTableToolbar = props => {
  const classes = useToolbarStyles();
  const selectClasses = useStyles();
  const { numSelected } = props;

  return (
    <Toolbar
      className={clsx(classes.root, {
        [classes.highlight]: numSelected > 0
      })}
    >
      {numSelected > 0 ? (
        <Typography
          className={classes.title}
          color="inherit"
          variant="subtitle1"
          component="div"
        >
          {numSelected} selected
        </Typography>
      ) : (
        <Typography
          className={classes.title}
          variant="h6"
          id="tableTitle"
          component="div"
        >
          상품 관리 리스트
        </Typography>
      )}

      {numSelected > 0 ? (
        <Tooltip title="Delete">
          <IconButton aria-label="delete">
            <DeleteIcon />
          </IconButton>
        </Tooltip>
      ) : (
        <Tooltip title="Filter list">
          <IconButton aria-label="filter list">
            <FilterListIcon />
          </IconButton>
        </Tooltip>
      )}
    </Toolbar>
  );
};

EnhancedTableToolbar.propTypes = {
  numSelected: PropTypes.number.isRequired
};

const useStyles = makeStyles(theme => ({
  root: {
    width: "100%"
  },
  paper: {
    width: "100%",
    marginBottom: theme.spacing(2)
  },
  table: {
    minWidth: 1500
  },
  visuallyHidden: {
    border: 0,
    clip: "rect(0 0 0 0)",
    height: 1,
    margin: -1,
    overflow: "hidden",
    padding: 0,
    position: "absolute",
    top: 20,
    width: 1
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120
  },
  selectEmpty: {
    marginTop: theme.spacing(2)
  }
}));

function Main(props) {
  const classes = useStyles();
  const [isLoading, setIsLoading] = React.useState(false);
  const [order, setOrder] = React.useState("asc");
  const [orderBy, setOrderBy] = React.useState("calories");
  const [selected, setSelected] = React.useState([]);
  const [page, setPage] = React.useState(0);
  const [dense, setDense] = React.useState(false);
  const [rowsPerPage, setRowsPerPage] = React.useState(5);
  const [productList, setProductList] = React.useState({ list: [], count: 0 });
  const [sellerCount, setSellerCount] = React.useState(0);
  const [input, setInput] = React.useState();
  const [seller_status, setSellerStatus] = React.useState("");
  const [seller_type_name, setSellerTypeName] = React.useState("");

  // DatePicker value 형식에 맞게 값을 저장하기 위해 별도로 state 생성
  const [dateStart, setDateStart] = React.useState();
  const [dateEnd, setDateEnd] = React.useState();

  // 페이징에 필요한 state
  const [limit, setLimit] = React.useState(10);
  const [offset, setOffset] = React.useState(0);

  // 검색어 필터 input 변경
  const onChangeInput = e => {
    setInput({ ...input, [e.target.name]: e.target.value });
  };

  // 셀러 상태 검색 셀렉트 박스
  const onChangeSellerStatus = e => {
    setSellerStatus(e.target.value);
  };

  const onChangeSellerTypeName = e => {
    setSellerTypeName(e.target.value);
  };

  // 처음 실행 시 전체 셀러 리스트 받아오기
  useEffect(() => {
    getProductList();
  }, []);

  const getProductList = () => {
    console.log("getproduct!!!!");
    fetch(`${JMURL}/product?offset=0&limit=1000`, {
      method: "GET",
      headers: {
        Authorization: localStorage.getItem("token"),
        // 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
        "Content-Type": "application/json"
      }
    })
      // 네트워크 통신 및 인자로 지정한 URL에 대한 문제가 있는지를 검사
      .then(res => {
        console.log("res::? ", res);
        if (res.ok) {
          return res.json();
        } else {
          alert("네트워크 오류");
        }
      })
      .then(res => {
        console.log("get::", res.product_list);
        setProductList({
          ...productList,
          list: res.product_list,
          count: res.product_count
        });
      })
      // 두번째 then에서 지정한 함수의 실행 시에 어떤 문제가 발생하면 catch함수 호출
      .catch(err => {
        console.log("catch error: ", err);
      });
  };

  const handleSelectAllClick = event => {
    if (event.target.checked) {
      const newSelecteds = itemRows.map(n => n.name);
      setSelected(newSelecteds);
      return;
    }
    setSelected([]);
  };

  const handleClick = (event, name) => {
    const selectedIndex = selected.indexOf(name);
    let newSelected = [];

    if (selectedIndex === -1) {
      newSelected = newSelected.concat(selected, name);
    } else if (selectedIndex === 0) {
      newSelected = newSelected.concat(selected.slice(1));
    } else if (selectedIndex === selected.length - 1) {
      newSelected = newSelected.concat(selected.slice(0, -1));
    } else if (selectedIndex > 0) {
      newSelected = newSelected.concat(
        selected.slice(0, selectedIndex),
        selected.slice(selectedIndex + 1)
      );
    }

    setSelected(newSelected);
  };

  const isSelected = name => selected.indexOf(name) !== -1;

  const emptyRows =
    rowsPerPage - Math.min(rowsPerPage, itemRows.length - page * rowsPerPage);

  // 로록 조회 시작일 달력
  const onChangedStartPeriod = e => {
    let year = e.getFullYear();
    let month = e.getMonth() + 1;
    let day = e.getDate();
    let date = year + "-" + month + "-" + day;

    setInput({ ...input, start_time: date });
    setDateStart(e);
  };

  // 등록 조회 종료일 달력
  const onChangedEndPeriod = e => {
    let year = e.getFullYear();
    let month = e.getMonth() + 1;
    let day = e.getDate();
    let date = year + "-" + month + "-" + day;
    setInput({ ...input, close_time: date });
    setDateEnd(e);
  };
  // limit 값 변경시 useEffect 호출
  useEffect(() => {
    console.log("useEffect() limit, offset");
    // onSearch();
  }, [limit, offset, isLoading]);

  // 검색을 했다가 지웠을 때 객체 키와 빈 문자열이 남는 경우가 있어서
  // 빈 문자열만 있는 경우에 아무 검색어도 입력하지 않은 것으로 판단하기 위한 함수
  const isInputEmpty = obj => {
    for (let key in obj) {
      if (obj[key] !== "") return false;
    }
    return true;
  };

  // 필터 검색하기
  const onSearch = () => {
    console.log("onSearch(): ");

    // 검색어
    let queryString = new URLSearchParams();
    for (let key in input) {
      //   if (!input.hasOwnProperty()) continue;
      queryString.append(key, input[key]);
    }
    if (offset) {
      console.log("offset: ", offset * limit);
      queryString.append("offset", offset * limit);
    }
    if (limit) {
      console.log("limit: ", limit);
      queryString.append("limit", limit);
    }

    if (seller_status) {
      queryString.append("seller_status", seller_status);
    }

    if (seller_type_name) {
      queryString.append("seller_type_name", seller_type_name);
    }

    console.log("queryString: ", queryString);
    fetch(`${YJURL}/seller?${queryString}`, {
      method: "GET",
      headers: {
        Authorization: localStorage.getItem("token"),
        // 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
        "Content-Type": "application/json"
      }
    })
      .then(res => res.json())
      .then(res => {
        console.log("onSearch() input:", input);
        console.log("seller_status: ", seller_status);
        console.log("seller_type_name: ", seller_type_name);
        console.log("onSearch() result: ", res);
        setIsLoading(false);

        console.log("122");
        setProductList({
          ...productList,
          list: res.product_list,
          count: res.product_count
        });
      });
  };

  // 한 페이지에 표시할 아이템 수
  const onChangeLimit = (lim, tp) => {
    // 총 페이지 수
    let totalPage = productList.count / lim;
    totalPage = parseInt(totalPage);
    // 총 아이템 수와 limit를 나눠서 나누어떨어지지 않으면 페이지를 하나 추가한다.
    if (productList.count % limit > 0) {
      totalPage++;
    }

    // 현재 총 페이지 수가 새로운 총 페이지수 보다 높으면 첫페이지로 이동
    if (tp > totalPage) {
      setOffset(0);
    }
    console.log("setLimit");
    setLimit(lim);
  };

  // 다음 페이지 버튼 클릭
  const onIncreaseOffset = total => {
    console.log("onIncreaseOffset() total: ", total, "offset: ", offset);
    setIsLoading(true);
    // 현재 페이지가 전체 페이지보다 작을 때만 실행
    if (offset + 1 < parseInt(totalPage)) {
      setOffset(offset + 1);
    }
  };

  // 이전 페이지 버튼 클릭
  const onDecreaseOffset = total => {
    console.log("onDecreaseOffset()", total, "offset: ", offset);
    setIsLoading(true);
    // 현재 페이지가 1보다 낮아지지 않게 하기 위한 조건식
    if (offset + 1 > 1) {
      setOffset(offset - 1);
    }
  };

  // 현재 페이지
  const onChangeOffsetInput = e => {
    console.log("onChangeOffsetInput value: ", e.target.value);
    if (e.key === "Enter") {
      setOffset(e.target.value);
    }
  };

  // 총 페이지 수
  let totalPage = productList.count / limit;
  totalPage = parseInt(totalPage);
  // 총 아이템 수와 limit를 나눠서 나누어떨어지지 않으면 페이지를 하나 추가한다.
  if (productList.count % limit > 0) {
    totalPage++;
  }

  // 검색어
  let queryString = new URLSearchParams();
  for (let key in input) {
    //   if (!input.hasOwnProperty()) continue;
    queryString.append(key, input[key]);
  }
  if (offset) {
    console.log("offset: ", offset * limit);
    queryString.append("offset", offset * limit);
  }
  if (limit) {
    console.log("limit: ", limit);
    queryString.append("limit", limit);
  }

  if (seller_status !== "") {
    console.log("seller_status: ", seller_status);
    queryString.append("seller_status", seller_status);
  }

  if (seller_type_name !== "") {
    console.log("seller_type_name: ", seller_type_name);
    queryString.append("seller_type_name", seller_type_name);
  }

  const moveToProductLink = id => {
    console.log("moveToSellerLink() id: ", id);
    props.history.push(`/productRegist?id=${id}`);
  };

  const onChangeStatus = (statusName, statusId, sellerId) => {
    fetch(`${YJURL}/seller/${sellerId}/status`, {
      method: "PUT",
      headers: {
        Authorization: localStorage.getItem("token"),
        // 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        seller_status_id: statusId
      })
    })
      .then(res => {
        if (res.ok) {
          return res.json();
        } else {
          alert("네트워크 에러");
        }
      })
      .then(res => {
        console.log("onActionClick() res:", res);
        if (res.message === "SUCCESS") {
          alert("정상 처리 되었습니다.");
          onSearch();
        }
      })
      .catch(err => console.log("catch():", err));
  };

  console.log("input: ", input);
  console.log("productList: ", productList);
  return (
    <Container>
      {isLoading && (
        <Heart>
          <HeartDiv></HeartDiv>
        </Heart>
      )}

      <SearchMenuContainer>
        <LeftMenu></LeftMenu>
        <RightMenu></RightMenu>
      </SearchMenuContainer>

      <div className={classes.root}>
        <Paper className={classes.paper}>
          <EnhancedTableToolbar numSelected={selected.length} />
          <TableContainer>
            {isLoading && <LoadingPage />}

            <Table
              className={classes.table}
              aria-labelledby="tableTitle"
              size={dense ? "small" : "small"}
              aria-label="enhanced table"
              stickyHeader
            >
              <EnhancedTableHead
                classes={classes}
                numSelected={selected.length}
                order={order}
                orderBy={orderBy}
                onSelectAllClick={handleSelectAllClick}
                //   onRequestSort={handleRequestSort}
                rowCount={itemRows.length}
              />
              <TableBody>
                {
                  // stableSort(itemRows, getComparator(order, orderBy))
                  //   .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                  productList.list.map((row, index) => {
                    // console.log('index: ', index);
                    const isItemSelected = isSelected(row.product_no);
                    const labelId = `enhanced-table-checkbox-${index}`;

                    // { id: 'created_at', numeric: true, disablePadding: true, label: '등록일' },
                    // {
                    //   id: 'image_url',
                    //   label: '대표이미지',
                    // },
                    // { id: 'product_name', numeric: true, disablePadding: true, label: '상품명' },
                    // { id: 'product_no', numeric: true, disablePadding: true, label: '상품번호' },
                    // {
                    //   id: 'seller_type_name',
                    //   label: '셀러속성',
                    // },
                    // {
                    //   id: 'seller_name',
                    //   label: '셀러명',
                    // },
                    // {
                    //   id: 'sellerStatus',
                    //   label: '판매가',
                    // },
                    // {
                    //   id: 'managerContact',
                    //   label: '할인가',
                    // },
                    // {
                    //   id: 'managerEmail',
                    //   label: '판매여부',
                    // },
                    // {
                    //   id: 'sellerProperty',
                    //   label: '진열여부',
                    // },
                    // {
                    //   id: 'productCount',
                    //   label: '할인여부',
                    // },
                    return (
                      <TableRow
                        hover
                        role="checkbox"
                        aria-checked={isItemSelected}
                        tabIndex={-1}
                        key={row.product_no}
                        selected={isItemSelected}
                      >
                        <TableCell padding="checkbox">
                          <Checkbox
                            checked={isItemSelected}
                            inputProps={{ "aria-labelledby": labelId }}
                            onClick={event =>
                              handleClick(event, row.product_no)
                            }
                          />
                        </TableCell>
                        <TableCell
                          component="th"
                          id={labelId}
                          scope="row"
                          padding="none"
                          align="center"
                        >
                          {row.created_at}
                        </TableCell>
                        <TableCell align="right">
                          <SellerLoginIdLink
                            onClick={() => moveToProductLink(row.product_no)}
                          >
                            <ProductImage src={row.image_url} />
                          </SellerLoginIdLink>
                        </TableCell>
                        <TableCell align="right">{row.product_name}</TableCell>
                        <TableCell align="right">{row.product_no}</TableCell>
                        <TableCell align="right">
                          {row.seller_type_name}
                        </TableCell>
                        <TableCell align="right">{row.seller_name}</TableCell>
                        <TableCell align="right">{row.price}</TableCell>
                        <TableCell align="right">
                          {row.discount_price}
                        </TableCell>
                        <TableCell align="right">
                          {row.is_available ? "판매" : "미판매"}
                        </TableCell>
                        <TableCell align="right">
                          {row.is_on_display ? "진열" : "미진열"}
                        </TableCell>
                        <TableCell align="right">
                          {row.is_discount ? "할인" : "미할인"}
                        </TableCell>
                      </TableRow>
                    );
                  })
                }
                {emptyRows > 0 && (
                  <TableRow style={{ height: (dense ? 33 : 53) * emptyRows }}>
                    <TableCell colSpan={6} />
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </TableContainer>
        </Paper>
        {/* <FormControlLabel
        control={<Switch checked={dense} onChange={handleChangeDense} />}
        label="Dense padding"
      /> */}
      </div>
    </Container>
  );
}

export default withRouter(Main);

const Container = styled.div`
  padding: 10px 20px 20px 20px;
`;

const InputForm = styled.input`
  height: 30px;
  width: 100%;
  border: 1px solid #bdbdbd;
`;

const DatePickerContainer = styled.div`
  display: flex;
  flex-direction: column;
`;

const DatePickerWrapper = styled.div`
  margin-bottom: 5px;
`;

const PaginationContainer = styled.div`
  padding: 0 15px;
  display: flex;
  align-items: center;
`;

const PaginationInputForm = styled.input`
  height: 30px;
  width: 45px;
  border: 1px solid #bdbdbd;
  padding: 6px 10px;
  text-align: center;
`;

const SellerLoginIdLink = styled.div`
  &:hover {
    cursor: pointer;
  }
`;

const LoadingPage = styled.div`
  position: absolute; /* Stay in place */
  z-index: 1; /* Sit on top */
  top: 80;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  background-color: #000;
  opacity: 0.5;
`;

const Heart = styled.div`
  display: inline-block;
  position: absolute;
  width: 80px;
  height: 80px;
  transform: rotate(45deg);
  transform-origin: 40px 40px;
`;

const HeartDiv = styled.div`
  & {
    top: 112px;
    left: 500px;
    position: absolute;
    width: 32px;
    height: 32px;
    background: #fe34c3;

    ${props => {
      return css`
        animation: ${HeartKeyFrames} 1.2s infinite
          cubic-bezier(0.215, 0.61, 0.355, 1);
      `;
    }}
  }
  &:after,
  &:before {
    content: " ";
    position: absolute;
    display: block;
    width: 32px;
    height: 32px;
    background: #fe34c3;
  }
  &:before {
    left: -24px;
    border-radius: 50% 0 0 50%;
  }
  &:after {
    top: -24px;
    border-radius: 50% 50% 0 0;
  }
`;

const HeartKeyFrames = keyframes`
   0% {
    transform: scale(0.95);
  }
  5% {
    transform: scale(1.1);
  }
  39% {
    transform: scale(0.85);
  }
  45% {
    transform: scale(1);
  }
  60% {
    transform: scale(0.95);
  }
  100% {
    transform: scale(0.9);
  }
`;

const ActionButton = styled.div`
  display: inline-block;
  height: 22px;
  background-color: ${props => props.color};
  color: #fff;
  padding: 1px 5px;
  margin: 0 2px;
  border: 1px solid #bdbdbd;
  border-radius: 4px;
  cursor: pointer;
`;

const SearchMenuContainer = styled.div``;
const LeftMenu = styled.div``;
const RightMenu = styled.div``;

const SearchTitle = styled.div``;

const ProductImage = styled.img`
  width: 70px;
  height: 70px;
`;
