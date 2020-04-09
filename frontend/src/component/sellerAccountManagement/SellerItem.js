import React from 'react';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import Checkbox from '@material-ui/core/Checkbox';

const SellerItem = () => {
  return (
    <TableRow>
      <TableCell>{this.props.id}</TableCell>
      <TableCell>
        <img src={this.props.image} />
      </TableCell>
      <TableCell>{this.props.name}</TableCell>
      <TableCell>{this.props.birth}</TableCell>
      <TableCell>{this.props.gender}</TableCell>
      <TableCell>{this.props.job}</TableCell>
    </TableRow>
  );
};

export default SellerItem;
