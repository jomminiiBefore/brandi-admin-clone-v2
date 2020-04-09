import React from 'react';
import TableBox from 'src/component/common/TableBox';
import TableItem from 'src/component/common/TableItem';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableHead from '@material-ui/core/TableHead';
import TableBody from '@material-ui/core/TableBody';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import Checkbox from '@material-ui/core/Checkbox';
import { withStyles } from '@material-ui/core/styles';
import style from 'src/utils/styles';
import styled from 'styled-components';
import TestingTable from './TestingTable';

const styles = (theme) => ({
  root: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto',
  },
  table: {
    minWidth: 1500,
  },
});

const Main = (props) => {
  const { classes } = props;
  //	번호	셀러아이디	영문이름	한글이름	셀러구분	회원번호	담당자이름	셀러상태	담당자연락처	담당자이메일	셀러속성	상품개수	URL	등록일시	Actions
  return (
    <Container>
      <TableBox title="셀러 회원 리스트">
        {/* <Paper className={classes.table}> */}
        <Table className={classes.table}>
          <TableHead>
            <TableRow>
              <TableCell>
                <Checkbox></Checkbox>
              </TableCell>
              <TableCell>번호</TableCell>
              <TableCell>셀러아이디</TableCell>
              <TableCell>영문이름</TableCell>
              <TableCell>한글이름</TableCell>
              <TableCell>셀러구분</TableCell>
              <TableCell>회원번호</TableCell>
              <TableCell>담당자이름</TableCell>
              <TableCell>셀러상태</TableCell>
              <TableCell>담당자연락처</TableCell>
              <TableCell>담당자이메일</TableCell>
              <TableCell>셀러속성</TableCell>
              <TableCell>상품개수</TableCell>
              <TableCell>URL 등록일시</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody></TableBody>
        </Table>
        {/* </Paper> */}
      </TableBox>
    </Container>
  );
};

export default withStyles(styles)(Main);

const Container = styled.div`
  padding: 10px 20px 20px 20px;
`;
