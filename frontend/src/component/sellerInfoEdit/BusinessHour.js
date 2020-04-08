import React, { useState } from 'react';
import InfoText from 'src/component/common/InfoText';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import styled from 'styled-components';

// TimePicker
const useStyles = makeStyles((theme) => ({
  container: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    width: 120,
  },
}));

const BusinessHour = ({
  openingName,
  closingName,
  onCheckWeekend,
  onChangeBusinessHour,
}) => {
  // TimePicker
  const classes = useStyles();

  return (
    <Container>
      <TextField
        id={openingName}
        type="time"
        defaultValue="07:30"
        className={classes.textField}
        InputLabelProps={{
          shrink: true,
        }}
        inputProps={{
          step: 300, // 5 min
        }}
        onChange={(e) => onChangeBusinessHour(e)}
      />
      ~
      <TextField
        id={closingName}
        type="time"
        defaultValue="07:30"
        className={classes.textField}
        InputLabelProps={{
          shrink: true,
        }}
        inputProps={{
          step: 300, // 5 min
        }}
        onChange={(e) => onChangeBusinessHour(e)}
      />
      {openingName === 'openingWeekdayTime' && (
        <>
          <InfoText content="주말에도 운영하시는 경우 체크박스를 누르시고 입력해주세요." />
          <WeekendCheckBox
            type="checkbox"
            id="weekend"
            name="weekend"
            onChange={onCheckWeekend}
          />
        </>
      )}
    </Container>
  );
};

export default BusinessHour;

const Container = styled.div`
  display: flex;
`;

const WeekendCheckBox = styled.input`
  align-self: center;
`;
