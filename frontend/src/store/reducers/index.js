import { combineReducers } from 'redux';

const reducerName = (state = [], action) => {
  switch (action.type) {
    case 'ACTION_NAME':
      //   return [...state, action.payload];
      return state;
    default:
      return state;
  }
};

export default combineReducers({ reducerName });
