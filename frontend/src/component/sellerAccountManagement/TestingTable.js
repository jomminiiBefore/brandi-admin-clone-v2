import React, { useEffect } from 'react';
import { withRouter } from 'react-router-dom';
import { YJURL } from 'src/utils/config';
import PropTypes from 'prop-types';
import EnhancedTableHead from 'src/component/sellerAccountManagement/EnhancedTableHead';
import CustomButton from 'src/component/common/CustomButton';
import SmallButton from 'src/component/common/SmallButton';
import clsx from 'clsx';
import { lighten, makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TablePagination from '@material-ui/core/TablePagination';
import TableRow from '@material-ui/core/TableRow';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Paper from '@material-ui/core/Paper';
import Checkbox from '@material-ui/core/Checkbox';
import IconButton from '@material-ui/core/IconButton';
import Tooltip from '@material-ui/core/Tooltip';
import DeleteIcon from '@material-ui/icons/Delete';
import Select from '@material-ui/core/Select';
import FilterListIcon from '@material-ui/icons/FilterList';
import DatePicker from 'react-date-picker';

// select
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';

import style from 'src/utils/styles';
import styled from 'styled-components';

function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein };
}

const itemRows = [
  createData('Cupcake', 305, 3.7, 67, 4.3),
  createData('Donut', 452, 25.0, 51, 4.9),
  createData('Eclair', 262, 16.0, 24, 6.0),
  createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
  createData('Gingerbread', 356, 16.0, 49, 3.9),
  createData('Honeycomb', 408, 3.2, 87, 6.5),
  createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
  createData('Jelly Bean', 375, 0.0, 94, 0.0),
  createData('KitKat', 518, 26.0, 65, 7.0),
  createData('Lollipop', 392, 0.2, 98, 0.0),
  createData('Marshmallow', 318, 0, 81, 2.0),
  createData('Nougat', 360, 19.0, 9, 37.0),
  createData('Oreo', 437, 18.0, 63, 4.0),
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

const useToolbarStyles = makeStyles((theme) => ({
  root: {
    paddingLeft: theme.spacing(2),
    paddingRight: theme.spacing(1),
  },
  highlight:
    theme.palette.type === 'light'
      ? {
          color: theme.palette.secondary.main,
          backgroundColor: lighten(theme.palette.secondary.light, 0.85),
        }
      : {
          color: theme.palette.text.primary,
          backgroundColor: theme.palette.secondary.dark,
        },
  title: {
    flex: '1 1 100%',
  },
}));

const EnhancedTableToolbar = (props) => {
  const classes = useToolbarStyles();
  const selectClasses = useStyles();
  const { numSelected } = props;

  return (
    <Toolbar
      className={clsx(classes.root, {
        [classes.highlight]: numSelected > 0,
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
          셀러 회원 리스트
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
  numSelected: PropTypes.number.isRequired,
};

const useStyles = makeStyles((theme) => ({
  root: {
    width: '100%',
  },
  paper: {
    width: '100%',
    marginBottom: theme.spacing(2),
  },
  table: {
    minWidth: 3500,
  },
  visuallyHidden: {
    border: 0,
    clip: 'rect(0 0 0 0)',
    height: 1,
    margin: -1,
    overflow: 'hidden',
    padding: 0,
    position: 'absolute',
    top: 20,
    width: 1,
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
}));

function TestingTable(props) {
  const classes = useStyles();
  const [order, setOrder] = React.useState('asc');
  const [orderBy, setOrderBy] = React.useState('calories');
  const [selected, setSelected] = React.useState([]);
  const [page, setPage] = React.useState(0);
  const [dense, setDense] = React.useState(false);
  const [rowsPerPage, setRowsPerPage] = React.useState(5);
  const [sellerList, setSellerList] = React.useState({ list: [], count: 0 });
  const [sellerCount, setSellerCount] = React.useState(0);
  const [input, setInput] = React
    .useState
    //   {
    // seller_account_id: 0,
    // login_id: '',
    // name_en: '',
    // name_kr: '',
    // brandi_app_user_id: 0,
    // manager_name: '',
    // seller_status: '',
    // manager_contact_number: '',
    // manager_email: '',
    // seller_type_name: '',
    // created_at_start: '',
    // created_at_end: '',
    //   }
    ();

  // DatePicker value 형식에 맞게 값을 저장하기 위해 별도로 state 생성
  const [dateStart, setDateStart] = React.useState();
  const [dateEnd, setDateEnd] = React.useState();

  // 페이징에 필요한 state
  const [limit, setLimit] = React.useState(10);
  const [offset, setOffset] = React.useState(0);

  // 검색어 필터 input 변경
  const onChangeInput = (e) => {
    setInput({ ...input, [e.target.name]: e.target.value });
  };

  // 처음 실행 시 전체 셀러 리스트 받아오기
  useEffect(() => {
    getSellerList();
  }, []);

  const getSellerList = () => {
    fetch(`${YJURL}/seller`, {
      method: 'GET',
      headers: {
        Authorization:
          'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
        'Content-Type': 'application/json',
      },
    })
      .then((res) => res.json())
      .then((res) => {
        console.log('get::', res);
        if (input) {
          setSellerList({
            ...sellerList,
            list: res.seller_list,
            count: res.seller_count.filtered_seller_count,
          });
          //   setTotalList(res.seller_count.filtered_seller_count);
        } else {
          setSellerList({
            ...sellerList,
            list: res.seller_list,
            count: res.seller_count.total_seller_count,
          });
          //   setTotalList(res.seller_count.total_seller_count);
        }
      });
  };

  const handleSelectAllClick = (event) => {
    if (event.target.checked) {
      const newSelecteds = itemRows.map((n) => n.name);
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

  const isSelected = (name) => selected.indexOf(name) !== -1;

  const emptyRows =
    rowsPerPage - Math.min(rowsPerPage, itemRows.length - page * rowsPerPage);

  // 등록 조회 시작일 달력
  const onChangedStartPeriod = (e) => {
    let year = e.getFullYear();
    let month = e.getMonth() + 1;
    let day = e.getDate();
    let date = year + '-' + month + '-' + day;

    setInput({ ...input, start_time: date });
    setDateStart(e);
  };

  // 등록 조회 종료일 달력
  const onChangedEndPeriod = (e) => {
    let year = e.getFullYear();
    let month = e.getMonth() + 1;
    let day = e.getDate();
    let date = year + '-' + month + '-' + day;
    setInput({ ...input, close_time: date });
    setDateEnd(e);
  };
  // limit 값 변경시 useEffect 호출
  useEffect(() => {
    console.log('useEffect() limit, offset');
    onSearch();
  }, [limit, offset]);

  // 필터 검색하기
  const onSearch = () => {
    console.log('onSearch(): ');

    // 검색어
    let queryString = new URLSearchParams();
    for (let key in input) {
      //   if (!input.hasOwnProperty()) continue;
      queryString.append(key, input[key]);
    }
    if (offset) {
      console.log('offset: ', offset * limit);
      queryString.append('offset', offset * limit);
    }
    if (limit) {
      console.log('limit: ', limit);
      queryString.append('limit', limit);
    }

    console.log('queryString: ', queryString);
    fetch(`${YJURL}/seller?${queryString}`, {
      method: 'GET',
      headers: {
        Authorization:
          'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
        'Content-Type': 'application/json',
      },
    })
      .then((res) => res.json())
      .then((res) => {
        console.log('onSearch() input:', input);
        console.log('onSearch() result: ', res);
        // 검색어가 있을 경우 필터된 리스트의 총 개수를 가져온다.
        if (input) {
          console.log('122');
          setSellerList({
            ...sellerList,
            list: res.seller_list,
            count: res.seller_count.filtered_seller_count,
          });
          //   setTotalList(res.seller_count.filtered_seller_count);
        } else {
          console.log('222');
          setSellerList({
            ...sellerList,
            list: res.seller_list,
            count: res.seller_count.total_seller_count,
          });
          //   setTotalList(res.seller_count.total_seller_count);
        }
      });
  };

  // 한 페이지에 표시할 아이템 수
  const onChangeLimit = (val, tp) => {
    // 총 페이지 수
    let totalPage = sellerList.count / val;
    totalPage = parseInt(totalPage);
    // 총 아이템 수와 limit를 나눠서 나누어떨어지지 않으면 페이지를 하나 추가한다.
    if (sellerList.count % limit > 0) {
      totalPage++;
    }
    console.log('onChangeLimit() tp: ', tp);
    console.log('onChangeLimit() total: ', totalPage);
    console.log('onChangeLimit() offset:', offset);

    if (tp > totalPage) {
      console.log('bigger');
      setOffset(0);
    }
    console.log('setLimit');
    setLimit(val);
  };

  // 다음 페이지 버튼 클릭
  const onIncreaseOffset = (total) => {
    console.log('onIncreaseOffset() total: ', total, 'offset: ', offset);

    // 현재 페이지가 전체 페이지보다 작을 때만 실행
    if (offset + 1 < parseInt(totalPage)) {
      setOffset(offset + 1);
    }
  };

  // 이전 페이지 버튼 클릭
  const onDecreaseOffset = (total) => {
    console.log('onDecreaseOffset()', total, 'offset: ', offset);

    // 현재 페이지가 1보다 낮아지지 않게 하기 위한 조건식
    if (offset + 1 > 1) {
      setOffset(offset - 1);
    }
  };

  // 현재 페이지
  const onChangeOffsetInput = (e) => {
    console.log('onChangeOffsetInput value: ', e.target.value);
    if (e.key === 'Enter') {
      setOffset(e.target.value);
    }
  };

  // 총 페이지 수
  let totalPage = sellerList.count / limit;
  totalPage = parseInt(totalPage);
  // 총 아이템 수와 limit를 나눠서 나누어떨어지지 않으면 페이지를 하나 추가한다.
  if (sellerList.count % limit > 0) {
    totalPage++;
  }

  // 검색어
  let queryString = new URLSearchParams();
  for (let key in input) {
    //   if (!input.hasOwnProperty()) continue;
    queryString.append(key, input[key]);
  }
  if (offset) {
    console.log('offset: ', offset * limit);
    queryString.append('offset', offset * limit);
  }
  if (limit) {
    console.log('limit: ', limit);
    queryString.append('limit', limit);
  }

  const moveToSellerLink = (id) => {
    console.log('moveToSellerLink() id: ', id);
    props.history.push(`/sellerInfoEdit?id=${id}`);
  };

  const getExcelFile = (queryString) => {
    console.log('query: ', queryString);
    fetch(`http://192.168.1.173:5000/seller?excel=1&${queryString}`, {
      method: 'GET',
      headers: {
        Authorization:
          'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X25vIjoxfQ.uxyTHQNJ5nNf6HQGXZtoq_xK5-ZPYjhpZ_I6MWzuGYw',
        'Content-Type': 'application/json',
      },
    })
      .then((res) => res.json())
      .then((res) => {
        window.location.assign(res.file_url);
      });
  };

  return (
    <Container>
      <div className={classes.root}>
        <Paper className={classes.paper}>
          <EnhancedTableToolbar numSelected={selected.length} />
          <TableContainer>
            <Table
              className={classes.table}
              aria-labelledby="tableTitle"
              size={dense ? 'small' : 'medium'}
              aria-label="enhanced table"
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
                <TableRow>
                  <TableCell align="right"></TableCell>
                  {/* 번호 */}
                  <TableCell
                    component="th"
                    // id={labelId}
                    scope="row"
                    padding="none"
                    align="center"
                  >
                    <InputForm
                      name="seller_account_id"
                      onChange={(e) => onChangeInput(e)}
                    />
                  </TableCell>
                  {/* 셀러 아이디 */}
                  <TableCell align="right">
                    <InputForm
                      name="login_id"
                      onChange={(e) => onChangeInput(e)}
                    />
                  </TableCell>
                  {/* 영문 이름 */}
                  <TableCell align="right">
                    <InputForm
                      name="name_en"
                      onChange={(e) => onChangeInput(e)}
                    />
                  </TableCell>
                  {/* 한글 이름 */}
                  <TableCell align="right">
                    <InputForm
                      name="name_kr"
                      onChange={(e) => onChangeInput(e)}
                    />
                  </TableCell>
                  {/* 셀러 구분 */}
                  <TableCell align="right"></TableCell>
                  {/* 회원 번호 */}
                  <TableCell align="right">
                    <InputForm
                      name="brandi_app_user_id"
                      onChange={(e) => onChangeInput(e)}
                    />
                  </TableCell>
                  {/* 담당자 이름 */}
                  <TableCell align="right">
                    <InputForm
                      name="manager_name"
                      onChange={(e) => onChangeInput(e)}
                    />
                  </TableCell>
                  {/* 셀러 상태 */}
                  <TableCell align="right">
                    <FormControl
                      variant="outlined"
                      className={classes.formControl}
                      margin="dense"
                    >
                      {/* <InputLabel id="demo-simple-select-outlined-label">
                        Select
                      </InputLabel> */}
                      <Select
                        name="seller_status"
                        value=""
                        onChange={(e) => onChangeInput(e)}
                      >
                        <MenuItem value="">
                          <em>Select</em>
                        </MenuItem>
                        <MenuItem value="입점">입점</MenuItem>
                        <MenuItem value="입점대기">입점대기</MenuItem>
                        <MenuItem value="퇴점">퇴점</MenuItem>
                        <MenuItem value="퇴점대기">퇴점대기</MenuItem>
                        <MenuItem value="휴점">휴점</MenuItem>
                      </Select>
                    </FormControl>
                  </TableCell>
                  {/* 담당자 연락처 */}
                  <TableCell align="right">
                    <InputForm
                      name="manager_contact_number"
                      onChange={(e) => onChangeInput(e)}
                    />
                  </TableCell>
                  {/* 담당자 이메일 */}
                  <TableCell align="right">
                    <InputForm
                      name="manager_email"
                      onChange={(e) => onChangeInput(e)}
                    />
                  </TableCell>
                  {/* 셀러 속성 */}
                  <TableCell align="right">
                    <FormControl
                      variant="outlined"
                      className={classes.formControl}
                      margin="dense"
                    >
                      {/* <InputLabel id="demo-simple-select-outlined-label">
                        Select
                      </InputLabel> */}
                      <Select
                        name="seller_type_name"
                        value=""
                        onChange={(e) => onChangeInput(e)}
                      >
                        <MenuItem value="">
                          <em>Select</em>
                        </MenuItem>
                        <MenuItem value="쇼핑몰">쇼핑몰</MenuItem>
                        <MenuItem value="마켓">마켓</MenuItem>
                        <MenuItem value="로드샵">로드샵</MenuItem>
                        <MenuItem value="디자이너브랜드">
                          디자이너브랜드
                        </MenuItem>
                        <MenuItem value="제너럴브랜드">제너럴브랜드</MenuItem>
                        <MenuItem value="내셔널브랜드">내셔널브랜드</MenuItem>
                        <MenuItem value="뷰티">뷰티</MenuItem>
                      </Select>
                    </FormControl>
                  </TableCell>
                  <TableCell align="right"></TableCell>
                  <TableCell align="right"></TableCell>
                  <TableCell align="right">
                    <DatePickerContainer>
                      <DatePickerWrapper>
                        <DatePicker
                          onChange={onChangedStartPeriod}
                          value={dateStart}
                          name="start_time"
                        />
                      </DatePickerWrapper>
                      <div>
                        <DatePicker
                          onChange={onChangedEndPeriod}
                          value={dateEnd}
                          name="close_time"
                        />
                      </div>
                    </DatePickerContainer>
                  </TableCell>
                  <TableCell align="right">
                    <SmallButton
                      name="Search"
                      color="#f0ac4e"
                      textColor="#fff"
                      onClickEvent={onSearch}
                    />
                    <SmallButton
                      name="Reset"
                      color="#d9534f"
                      textColor="#fff"
                      //   onClickEvent={}
                    />
                  </TableCell>
                </TableRow>

                {
                  // stableSort(itemRows, getComparator(order, orderBy))
                  //   .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)

                  sellerList.list.map((row, index) => {
                    // console.log('index: ', index);
                    const isItemSelected = isSelected(row.seller_account_id);
                    const labelId = `enhanced-table-checkbox-${index}`;

                    return (
                      <TableRow
                        hover
                        role="checkbox"
                        aria-checked={isItemSelected}
                        tabIndex={-1}
                        key={row.seller_account_id}
                        selected={isItemSelected}
                      >
                        <TableCell padding="checkbox">
                          <Checkbox
                            checked={isItemSelected}
                            inputProps={{ 'aria-labelledby': labelId }}
                            onClick={(event) =>
                              handleClick(event, row.seller_account_id)
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
                          {row.seller_account_id}
                        </TableCell>
                        <TableCell align="right">
                          <SellerLoginIdLink
                            onClick={() =>
                              moveToSellerLink(row.seller_account_id)
                            }
                          >
                            {row.login_id}
                          </SellerLoginIdLink>
                        </TableCell>
                        <TableCell align="right">{row.name_en}</TableCell>
                        <TableCell align="right">{row.name_kr}</TableCell>
                        <TableCell align="right">일반셀러</TableCell>
                        <TableCell align="right">
                          {row.brandi_app_user_id}
                        </TableCell>
                        <TableCell align="right">{row.manager_name}</TableCell>
                        <TableCell align="right">{row.seller_status}</TableCell>
                        <TableCell align="right">
                          {row.manager_contact_number}
                        </TableCell>
                        <TableCell align="right">{row.manager_email}</TableCell>
                        <TableCell align="right">
                          {row.seller_type_name}
                        </TableCell>
                        <TableCell align="right">{row.product_count}</TableCell>
                        <TableCell align="right">
                          <a href={row.site_url}>{row.site_url}</a>
                        </TableCell>
                        <TableCell align="right">{row.created_at}</TableCell>
                        <TableCell align="right">
                          {/* {console.log('row:: ', row.action)} */}
                          {/* {row.action &&
                            row.action.map((item, key) => {
                              //휴점신청 F0AC4E 퇴점신청처리 D9534F 휴점해제 5CB85B 입점승인 5BC0DE
                              let color;
                              if (item === '휴점 신청') {
                                color = '#f0ac4e';
                              } else if (
                                item === '퇴점 신청 처리' ||
                                item === '입점 거절' ||
                                item === '퇴점 확정 처리'
                              ) {
                                color = '#d9534f';
                              } else if (
                                item === '휴점 해제' ||
                                item === '퇴점 철회 처리'
                              ) {
                                color = '#5cb85b';
                              } else if (item === '입점 승인') {
                                color = '#5bc0d3';
                              }

                              return (
                                <SmallButton
                                  key={key}
                                  name={item}
                                  color={color}
                                  textColor="#fff"
                                  //   onClickEvent={}
                                />
                              );
                            })} */}
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
          <PaginationContainer>
            {offset > 0 && (
              <CustomButton
                name="<"
                onClickEvent={() => onDecreaseOffset(totalPage)}
              />
            )}
            <PaginationInputForm
              type="text"
              onKeyPress={onChangeOffsetInput}
              value={offset + 1}
              placeholder="1"
              onChange={onChangeInput}
            />
            {offset + 1 < parseInt(totalPage) && (
              <CustomButton
                name=">"
                onClickEvent={() => onIncreaseOffset(totalPage)}
              />
            )}
            of {parseInt(totalPage)} | View
            <FormControl
              variant="outlined"
              className={classes.formControl}
              margin="dense"
            >
              {/* <InputLabel id="demo-simple-select-outlined-label">
                        Select
                      </InputLabel> */}
              <Select
                name="limit"
                value={limit}
                onChange={(e) => onChangeLimit(e.target.value, totalPage)}
              >
                <MenuItem value="">
                  <em>Select</em>
                </MenuItem>
                <MenuItem value="10">10</MenuItem>
                <MenuItem value="20">20</MenuItem>
                <MenuItem value="50">50</MenuItem>
                <MenuItem value="100">100</MenuItem>
                <MenuItem value="150">150</MenuItem>
              </Select>
            </FormControl>
            <span>records | Found total {sellerList.count} records</span>
            <CustomButton
              name="엑셀 다운로드"
              color="#5cb85b"
              textColor="#fff"
              onClickEvent={() => getExcelFile(queryString)}
            />
          </PaginationContainer>
        </Paper>
        {/* <FormControlLabel
        control={<Switch checked={dense} onChange={handleChangeDense} />}
        label="Dense padding"
      /> */}
      </div>
    </Container>
  );
}

export default withRouter(TestingTable);

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
