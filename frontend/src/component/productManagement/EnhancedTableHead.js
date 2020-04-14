import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableSortLabel from '@material-ui/core/TableSortLabel';
import Checkbox from '@material-ui/core/Checkbox';

// "created_at": "2020-04-14 10:32:36",
//       "discount_price": 15300,
//       "image_url": "https://brandi-intern.s3.ap-northeast-2.amazonaws.com/8cc83e2a-58d5-44ce-beb4-9f737b5595f7",
//       "is_available": 1,
//       "is_discount": 1,
//       "is_on_display": 1,
//       "price": 18000,
//       "product_name": "white_cap",
//       "product_no": 1,
//       "seller_name": "수정윤희철러",
//       "seller_type_name": "쇼핑몰"
const headCells = [
  { id: 'created_at', numeric: true, disablePadding: true, label: '등록일' },
  {
    id: 'image_url',
    numeric: true,
    disablePadding: false,
    label: '대표이미지',
  },
  {
    id: 'product_name',
    numeric: false,
    disablePadding: false,
    label: '상품명',
  },
  { id: 'product_no', numeric: true, disablePadding: true, label: '상품번호' },
  {
    id: 'seller_type_name',
    numeric: true,
    disablePadding: true,
    label: '셀러속성',
  },
  {
    id: 'seller_name',
    numeric: true,
    disablePadding: true,
    label: '셀러명',
  },
  {
    id: 'sellerStatus',
    numeric: true,
    disablePadding: true,
    label: '판매가',
  },
  {
    id: 'managerContact',
    numeric: true,
    disablePadding: true,
    label: '할인가',
  },
  {
    id: 'managerEmail',
    numeric: true,
    disablePadding: true,
    label: '판매여부',
  },
  {
    id: 'sellerProperty',
    numeric: true,
    disablePadding: true,
    label: '진열여부',
  },
  {
    id: 'productCount',
    numeric: true,
    disablePadding: true,
    label: '할인여부',
  },
];

EnhancedTableHead.propTypes = {
  classes: PropTypes.object.isRequired,
  numSelected: PropTypes.number.isRequired,
  //   onRequestSort: PropTypes.func.isRequired,
  onSelectAllClick: PropTypes.func.isRequired,
  order: PropTypes.oneOf(['asc', 'desc']).isRequired,
  orderBy: PropTypes.string.isRequired,
  rowCount: PropTypes.number.isRequired,
};

export default function EnhancedTableHead(props) {
  const {
    classes,
    onSelectAllClick,
    order,
    orderBy,
    numSelected,
    rowCount,
    // onRequestSort,
  } = props;
  //   const createSortHandler = (property) => (event) => {
  //     onRequestSort(event, property);
  //   };

  return (
    <TableHead>
      <TableRow>
        <TableCell padding="checkbox">
          <Checkbox
            indeterminate={numSelected > 0 && numSelected < rowCount}
            checked={rowCount > 0 && numSelected === rowCount}
            onChange={onSelectAllClick}
            inputProps={{ 'aria-label': 'select all desserts' }}
          />
        </TableCell>
        {headCells.map((headCell) => (
          <TableCell
            key={headCell.id}
            // align={headCell.numeric ? 'right' : 'left'}
            align={'center'}
            padding={headCell.disablePadding ? 'none' : 'default'}
            sortDirection={orderBy === headCell.id ? order : false}
          >
            <TableSortLabel
              active={orderBy === headCell.id}
              direction={orderBy === headCell.id ? order : 'asc'}
              //   onClick={createSortHandler(headCell.id)}
            >
              {headCell.label}
              {orderBy === headCell.id ? (
                <span className={classes.visuallyHidden}>
                  {order === 'desc' ? 'sorted descending' : 'sorted ascending'}
                </span>
              ) : null}
            </TableSortLabel>
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
}
