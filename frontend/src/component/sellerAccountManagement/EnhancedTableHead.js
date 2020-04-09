import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import TableSortLabel from '@material-ui/core/TableSortLabel';
import Checkbox from '@material-ui/core/Checkbox';

const headCells = [
  { id: 'index', numeric: true, disablePadding: false, label: '번호' },
  { id: 'sellerId', numeric: true, disablePadding: false, label: '셀러아이디' },
  {
    id: 'englishName',
    numeric: true,
    disablePadding: false,
    label: '영문이름',
  },
  { id: 'koreanName', numeric: true, disablePadding: false, label: '한글이름' },
  { id: 'sellerType', numeric: true, disablePadding: false, label: '셀러구분' },
  {
    id: 'memberNumber',
    numeric: true,
    disablePadding: false,
    label: '회원번호',
  },
  {
    id: 'managerName',
    numeric: true,
    disablePadding: false,
    label: '담당자이름',
  },
  {
    id: 'sellerStatus',
    numeric: true,
    disablePadding: false,
    label: '셀러상태',
  },
  {
    id: 'managerContact',
    numeric: true,
    disablePadding: false,
    label: '담당자연락처',
  },
  {
    id: 'managerEmail',
    numeric: true,
    disablePadding: false,
    label: '담당자이메일',
  },
  {
    id: 'sellerProperty',
    numeric: true,
    disablePadding: false,
    label: '셀러속성',
  },
  {
    id: 'productCount',
    numeric: true,
    disablePadding: false,
    label: '상품개수',
  },
  {
    id: 'siteUrl',
    numeric: true,
    disablePadding: false,
    label: 'URL',
  },
  {
    id: 'RegisterDate',
    numeric: true,
    disablePadding: false,
    label: '등록일시',
  },
  { id: 'actions', numeric: true, disablePadding: false, label: 'Actions' },
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
